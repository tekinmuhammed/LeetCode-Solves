# 2463. Minimum Total Distance Traveled

**Difficulty:** Hard  
**Problem Link:** [LeetCode 2463](https://leetcode.com/problems/minimum-total-distance-traveled/description/)

---

## Problem Description

There are some robots and factories on a 1D line. You are given an integer array `robot` (positions) and a 2D integer array `factory` where `factory[j] = [position_j, capacity_j]`.

Each factory has a limit on the number of robots it can repair. Each robot should be repaired by exactly one factory. The total distance traveled is the sum of the absolute differences between the position of each robot and the factory it is assigned to.

Return the **minimum total distance** traveled by all robots to be repaired.

---

## Approach: Sorting + Memoization (Top-Down DP)

The core insight for this problem is that if we sort both the robots and the factories, the optimal assignment will not result in any "crossings." This means the relative order of robots and the factory slots they use remains the same, allowing us to solve it using Dynamic Programming.

### Key Ideas:
1.  **Sorting:** Sorting ensures that we can use a pointer-based matching strategy.
2.  **Factory Expansion:** Since each factory has a capacity, we can "flatten" the factories into individual slots. For example, a factory at position 10 with capacity 2 becomes two distinct slots: `[10, 10]`.
3.  **State Definition:** `dp[robot_idx][factory_idx]` represents the minimum distance to repair all robots starting from `robot_idx` using factory slots starting from `factory_idx`.
4.  **Transitions:**
    - **Assign:** The current robot takes the current factory slot: `abs(robot[i] - factory[j]) + dp(i+1, j+1)`.
    - **Skip:** The current robot skips the current factory slot to be assigned to a later one: `dp(i, j+1)`.
5.  **Base Cases:**
    - If all robots are assigned (`robot_idx == len(robot)`), cost is 0.
    - If robots remain but no factory slots are left (`factory_idx == len(factory_slots)`), we return a value representing infinity.

---

## Code

```python
import sys

# Increase recursion depth for deep DP trees
sys.setrecursionlimit(10000)

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        # Step 1: Sorting ensures the no-crossing property for optimal matching
        robot.sort()
        factory.sort(key=lambda x: x[0])
        
        # Step 2: Expand factory capacities into a flat list of positions
        factory_positions = []
        for pos, cap in factory:
            factory_positions.extend([pos] * cap)
            
        robot_count = len(robot)
        factory_count = len(factory_positions)

        # Step 3: Memoization table
        dp = [[None] * (factory_count + 1) for _ in range(robot_count + 1)]

        def _calculate_min_distance(robot_idx, factory_idx):
            # Base Case: All robots have been assigned
            if robot_idx == robot_count:
                return 0
            # Base Case: No more factory slots available
            if factory_idx == factory_count:
                return float('inf')
            
            if dp[robot_idx][factory_idx] is not None:
                return dp[robot_idx][factory_idx]

            # Option 1: Assign current robot to current factory slot
            assign = abs(robot[robot_idx] - factory_positions[factory_idx]) + \
                     _calculate_min_distance(robot_idx + 1, factory_idx + 1)

            # Option 2: Skip current factory slot
            skip = _calculate_min_distance(robot_idx, factory_idx + 1)

            # Memoize and return the minimum of the two choices
            dp[robot_idx][factory_idx] = min(assign, skip)
            return dp[robot_idx][factory_idx]

        return _calculate_min_distance(0, 0)
```

---

## Complexity Analysis

* **Time Complexity:** $O(R \times F)$
    - $R$ is the number of robots and $F$ is the total capacity across all factories.
    - We compute each state in the $R \times F$ DP table once.
* **Space Complexity:** $O(R \times F)$
    - To store the memoization table and the recursion stack.

---

## Tags
`Dynamic-Programming`, `Memoization`, `Sorting`, `Greedy-Property`, `Matrix`