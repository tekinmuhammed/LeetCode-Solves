# 2751. Robot Collisions

**Difficulty:** Hard  
**Problem Link:** [LeetCode 2751](https://leetcode.com/problems/robot-collisions/)

---

## Problem Description

There are $n$ robots, each with a position, health, and direction ('L' for left, 'R' for right). All robots move at the same speed. When two robots collide:
1.  The robot with **lower health** is removed from the line, and the other robot's health **decreases by 1**.
2.  If both robots have the **same health**, both are removed.

Return an array containing the health of the surviving robots in the **same order** they were given in the input.

---

## Approach: Sorting and Stack-Based Simulation

Since collisions only happen between a robot moving **Right ('R')** and a robot to its right moving **Left ('L')'**, we can simulate this efficiently using a stack.

### Key Ideas:
1.  **Order of Processing:** We must process robots based on their positions. We create an `indices` list and sort it according to the `positions` array.
2.  **The Stack Mechanism:**
    - We use a stack to keep track of robots moving to the **Right**.
    - When we encounter a robot moving to the **Left**:
        - It will potentially collide with the most recent 'R' robot (the top of the stack).
        - We compare their health values and apply the collision rules.
        - If the 'L' robot survives, it continues to collide with the *next* 'R' robot in the stack.
    - Robots moving to the **Right** are simply pushed onto the stack as they won't collide with anyone already processed (since we move from left to right).
3.  **Preserving Original Order:** After the simulation, we iterate through the original indices and collect the health values of robots that still have `health > 0`.

---

## Code

```python
from collections import deque

class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        n = len(positions)
        indices = list(range(n))
        stack = deque()

        # Sort indices based on positions to process robots from left to right
        indices.sort(key=lambda x: positions[x])

        for current_index in indices:
            if directions[current_index] == "R":
                # Right-moving robots are potential candidates for future collisions
                stack.append(current_index)
            else:
                # Left-moving robot: check for collisions with right-moving robots in the stack
                while stack and healths[current_index] > 0:
                    top_index = stack.pop()

                    if healths[top_index] > healths[current_index]:
                        # Right robot survives, Left robot destroyed
                        healths[top_index] -= 1
                        healths[current_index] = 0
                        stack.append(top_index)
                    elif healths[top_index] < healths[current_index]:
                        # Left robot survives, Right robot destroyed
                        healths[current_index] -= 1
                        healths[top_index] = 0
                    else:
                        # Both robots destroyed
                        healths[current_index] = 0
                        healths[top_index] = 0

        # Collect healths of survivors in their original input order
        return [h for h in healths if h > 0]
```

---

## Example Walkthrough

**Input:** `positions = [3, 5, 2, 6], healths = [10, 10, 15, 12], directions = "RLRL"`

1.  **Sorted Indices by Position:** `[2(Pos:2, Dir:L), 0(Pos:3, Dir:R), 1(Pos:5, Dir:L), 3(Pos:6, Dir:R)]`
2.  **Index 2 (L):** Stack is empty. Robot 2 survives (for now).
3.  **Index 0 (R):** Push to stack. `stack = [0]`
4.  **Index 1 (L):** Collides with Top (Index 0).
    - `healths[0] == healths[1] == 10`. Both are destroyed.
    - `stack = []`
5.  **Index 3 (R):** Push to stack. `stack = [3]`
6.  **Survivors:** Robot 2 (Health 15) and Robot 3 (Health 12).

**Output:** `[15, 12]`

---

## Complexity Analysis

* **Time Complexity:** $O(n \log n)$
    - Sorting the indices takes $O(n \log n)$.
    - The simulation loop runs $n$ times, and each robot is pushed/popped from the stack at most once, making the simulation $O(n)$.
* **Space Complexity:** $O(n)$
    - Required for the `indices` list and the `stack`.

---

## Tags
Stack, Simulation, Sorting, Array