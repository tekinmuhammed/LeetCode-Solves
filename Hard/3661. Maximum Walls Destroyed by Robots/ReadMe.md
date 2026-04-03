# 3661. Maximum Walls Destroyed by Robots

**Difficulty:** Hard  
**Problem Link:** [LeetCode 3661](https://leetcode.com/problems/maximum-walls-destroyed-by-robots/description/)

---

## Problem Description

You are given three integer arrays: `robots`, `distance`, and `walls`.
- `robots[i]` represents the position of the $i^{th}$ robot.
- `distance[i]` is the maximum distance the $i^{th}$ robot can travel.
- `walls` contains the positions of various walls on a 1D line.

Each robot can move either **Left** or **Right** from its starting position. 
- If a robot moves **Left**, it destroys all walls in the range $[robots[i] - distance[i], robots[i]]$.
- If a robot moves **Right**, it destroys all walls in the range $[robots[i], robots[i] + distance[i]]$.

Each wall can be destroyed at most once. Your goal is to determine the optimal direction for each robot to maximize the total number of destroyed walls.

---

## Approach: Binary Search + Dynamic Programming

The problem involves making a binary decision (Left or Right) for each robot while considering the overlap with neighboring robots.

### Key Ideas:
1.  **Preprocessing & Sorting:** - We sort both `robots` and `walls` to enable efficient range queries using binary search (`bisect`).
    - We map each robot to its distance for quick lookup after sorting.
2.  **Wall Counting with Binary Search:**
    - For each robot $i$, we calculate:
        - `left[i]`: Number of walls it can destroy by moving Left, without crossing the previous robot's starting position.
        - `right[i]`: Number of walls it can destroy by moving Right, without crossing the next robot's starting position.
        - `num[i]`: Total number of walls located between robot $i-1$ and robot $i$.
3.  **Dynamic Programming (DP):**
    - We maintain two states for each step $i$:
        - `sub_left`: Maximum walls destroyed by the first $i$ robots, where the $i^{th}$ robot moves **Left**.
        - `sub_right`: Maximum walls destroyed by the first $i$ robots, where the $i^{th}$ robot moves **Right**.
    - **Transitions:**
        - When moving the $i^{th}$ robot Left, we consider if the $(i-1)^{th}$ robot moved Left or Right. If the previous robot moved Right, we handle the potential overlap in the gap between them using the `num[i]` pre-calculated value.
        - When moving the $i^{th}$ robot Right, it doesn't conflict with the previous robot's Right move (as they move away from each other or cover independent segments).

---

## Code

```python
import bisect

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        left = [0] * n
        right = [0] * n
        num = [0] * n
        robots_to_distance = {}

        # Map robots to their respective distances
        for i in range(n):
            robots_to_distance[robots[i]] = distance[i]

        robots.sort()
        walls.sort()

        # Step 1: Pre-calculate wall counts in reachable ranges
        for i in range(n):
            pos1 = bisect.bisect_right(walls, robots[i])

            # Walls to the Left
            if i >= 1:
                left_bound = max(robots[i] - robots_to_distance[robots[i]], robots[i - 1] + 1)
                left_pos = bisect.bisect_left(walls, left_bound)
            else:
                left_pos = bisect.bisect_left(walls, robots[i] - robots_to_distance[robots[i]])
            left[i] = pos1 - left_pos

            # Walls to the Right
            if i < n - 1:
                right_bound = min(robots[i] + robots_to_distance[robots[i]], robots[i + 1] - 1)
                right_pos = bisect.bisect_right(walls, right_bound)
            else:
                right_pos = bisect.bisect_right(walls, robots[i] + robots_to_distance[robots[i]])
            pos2 = bisect.bisect_left(walls, robots[i])
            right[i] = right_pos - pos2

            # Gap walls between current and previous robot
            if i > 0:
                pos3 = bisect.bisect_left(walls, robots[i - 1])
                num[i] = pos1 - pos3

        # Step 2: DP to find the maximum destroyed walls
        sub_left, sub_right = left[0], right[0]
        for i in range(1, n):
            # Transition for current robot moving Left
            current_left = max(
                sub_left + left[i], 
                sub_right - right[i - 1] + min(left[i] + right[i - 1], num[i])
            )
            # Transition for current robot moving Right
            current_right = max(sub_left + right[i], sub_right + right[i])
            
            sub_left, sub_right = current_left, current_right

        return max(sub_left, sub_right)
```

---

## Complexity Analysis

* **Time Complexity:** $O(W \log W + R \log R + R \log W)$
    - Sorting `walls` ($W$): $O(W \log W)$.
    - Sorting `robots` ($R$): $O(R \log R)$.
    - For each robot, we perform `bisect` operations (binary search on walls): $O(R \log W)$.
    - DP pass: $O(R)$.
* **Space Complexity:** $O(R + W)$
    - To store the `left`, `right`, and `num` arrays, as well as the sorted versions of input arrays.

---

## Tags
`Dynamic-Programming`, `Binary-Search`, `Greedy`, `Sorting`, `Coordinate-Geometry`