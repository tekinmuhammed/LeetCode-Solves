# 3418. Maximum Amount of Money Robot Can Earn

**Difficulty:** Medium 
**Problem Link:** [LeetCode 3418](https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/description/)

---

## Problem Description

You are given an $m \times n$ grid `coins`. A robot starts at the top-left corner `(0, 0)` and wants to reach the bottom-right corner `(m-1, n-1)`. The robot can only move **right** or **down**.
 
Each cell contains a value:
- A positive value represents coins the robot gains.
- A negative value represents a robber who takes coins from the robot.

The robot has a special ability: it can **neutralize at most 2 robbers**, reducing their negative value to **0**.

Return the **maximum amount of money** the robot can have at the end of the journey.

---

## Approach: 3D Dynamic Programming

The problem has a "state" that depends not just on the position $(i, j)$ but also on how many times the robot has used its neutralization ability.

### Key Ideas:
1.  **State Definition:** We use a 3D DP table `dp[i][j][k]`, which represents the maximum coins the robot can have at cell `(i, j)` after using the neutralization ability exactly `k` times (where $k \in \{0, 1, 2\}$).
2.  **Transitions:** For each cell `(i, j)`, the robot can arrive from the top `(i-1, j)` or from the left `(i, j-1)`.
3.  **Handling Robbers (Negative Values):**
    - **Option 1 (Normal):** The robot takes the cell value as it is: `dp[prev] + coins[i][j]`.
    - **Option 2 (Neutralize):** If the value is negative and the robot has at least one neutralization left ($k > 0$), it can treat the cell as `0`: `dp[prev_with_k-1] + 0`.
4.  **Initialization:** Start at `(0, 0)`. If the first cell is negative, we can either take the penalty ($k=0$) or use one of our two abilities to start with $0$ ($k=1, 2$).

---

## Code

```python
class Solution(object):
    def maximumAmount(self, coins):
        """
        :type coins: List[List[int]]
        :rtype: int
        """
        m, n = len(coins), len(coins[0])
        
        # dp[i][j][k]: max coins at (i,j) using k neutralizations (k = 0, 1, 2)
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # Base Case: Starting point (0,0)
        val0 = coins[0][0]
        # k=0: No neutralization used
        dp[0][0][0] = val0
        # k=1 or 2: Use one neutralization if the first cell is a robber
        if val0 < 0:
            dp[0][0][1] = 0
            dp[0][0][2] = 0
        else:
            dp[0][0][1] = val0
            dp[0][0][2] = val0
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                val = coins[i][j]
                for k in range(3):
                    # Potential paths: from top or from left
                    options = []
                    if i > 0: options.append(dp[i-1][j])
                    if j > 0: options.append(dp[i][j-1])
                    
                    for prev_dp in options:
                        # Case A: Standard move (add the current coin/robber value)
                        if prev_dp[k] != -float('inf'):
                            dp[i][j][k] = max(dp[i][j][k], prev_dp[k] + val)
                        
                        # Case B: Use neutralization (only if val < 0 and k > 0)
                        if val < 0 and k > 0 and prev_dp[k-1] != -float('inf'):
                            dp[i][j][k] = max(dp[i][j][k], prev_dp[k-1])
                            
        return max(dp[m-1][n-1])
```

---

## Example Walkthrough 

**Input:** `coins = [[0,1,-1],[1,-2,3],[2,-3,4]]`

1.  **At (0,0):** Starting with 0. `dp[0][0] = [0, 0, 0]`.
2.  **Moving to (1,1) with val = -2:**
    - To have `k=0` at (1,1): Must take the -2.
    - To have `k=1` at (1,1): Can neutralize the -2 using a save from the previous step.
3.  **End Goal:** The result at `dp[m-1][n-1]` will hold the maximum of three scenarios: having used 0, 1, or 2 saves.

---

## Complexity Analysis 

* **Time Complexity:** $O(m \times n \times 3) \approx O(m \times n)$
    - We iterate through each cell once, and for each cell, we perform a constant number of operations (checking 3 states).
* **Space Complexity:** $O(m \times n \times 3) \approx O(m \times n)$
    - We store the max coins for 3 states at every cell in the grid.

---

## Tags
`Dynamic-Programming`, `Matrix`, `Grid-Search`, `Optimization`