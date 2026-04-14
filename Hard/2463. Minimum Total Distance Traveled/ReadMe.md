# 2463. Minimum Total Distance Traveled

**Difficulty:** Hard  
**Problem Link:** [LeetCode 2463](https://leetcode.com/problems/minimum-total-distance-traveled/)

---

## Problem Description

There are some robots and factories on a 1D line. You are given an integer array `robot` (positions) and a 2D integer array `factory` where `factory[j] = [position_j, capacity_j]`.

Each factory has a limit on the number of robots it can repair. Each robot should be repaired by exactly one factory. The total distance traveled is the sum of the absolute differences between the position of each robot and the factory it is assigned to.

Return the **minimum total distance** traveled by all robots to be repaired.

---

## Approach: Sorting + Memoization (Top-Down DP)

The key observation is that if we sort both the robots and the factories, the optimal assignment will preserve the relative order. That is, if robot $A$ is to the left of robot $B$, robot $A$ will be repaired by a factory slot that is at the same position or to the left of robot $B$'s factory slot.

### Key Ideas:
1.  **Sorting:** We sort both `robot` and `factory` by position to ensure the "no-crossing" optimal matching property.
2.  **Factory Expansion:** To simplify the capacity constraint, we expand the `factory` array into a linear list of `factory_positions`, where each position appears as many times as its capacity.
3.  **State Definition:** `dp[robot_idx][factory_idx]` represents the minimum distance to repair robots from `robot_idx` onwards using factory slots from `factory_idx` onwards.
4.  **Transitions:**
    - **Assign:** Assign the current robot to the current factory slot: 
      `dist(robot[i], factory[j]) + dp(i+1, j+1)`.
    - **Skip:** Skip the current factory slot to potentially use a better one later: 
      `dp(i, j+1)`.
5.  **Base Cases:**
    - If all robots are repaired (`robot_idx == robot_count`), cost is `0`.
    - If robots are left but no factory slots remain (`factory_idx == factory_count`), return a very large value (infinity).



---

## Code

```python
import sys

# Increase recursion depth for deep DP trees
sys.setrecursionlimit(2000)

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        # Step 1: Sort positions to ensure optimal ordering
        robot.sort()
        factory.sort(key=lambda x: x[0])
        
        # Step 2: Expand factory capacities into individual slots
        factory_positions = []
        for pos, cap in factory:
            factory_positions.extend([pos] * cap)
            
        robot_count = len(robot)
        factory_count = len(factory_positions)

        # Step 3: Initialize DP table for memoization
        dp = [[None] * (factory_count + 1) for _ in range(robot_count + 1)]

        def _calculate_min_distance(robot_idx, factory_idx):
            # Base Case: All robots repaired
            if robot_idx == robot_count:
                return 0
            # Base Case: Out of factory slots
            if factory_idx == factory_count:
                return int(1e15) # Use a safe infinity
            
            if dp[robot_idx][factory_idx] is not None:
                return dp[robot_idx][factory_idx]

            # Option 1: Assign current robot to current factory slot
            assign = abs(robot[robot_idx] - factory_positions[factory_idx]) + \
                     _calculate_min_distance(robot_idx + 1, factory_idx + 1)

            # Option 2: Skip current factory slot
            skip = _calculate_min_distance(robot_idx, factory_idx + 1)

            # Memoize and return the minimum of two choices
            dp[robot_idx][factory_idx] = min(assign, skip)
            return dp[robot_idx][factory_idx]

        return _calculate_min_distance(0, 0)