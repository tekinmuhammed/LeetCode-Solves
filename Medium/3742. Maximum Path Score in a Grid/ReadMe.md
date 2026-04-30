# 3742. Maximum Path Score in a Grid 

**Difficulty:** Medium
**Problem Link:** [LeetCode 3742](https://leetcode.com/problems/maximum-path-score-in-a-grid/description/)

---

## Problem Description 

You are given an `m x n` integer `grid` and an integer `k`. You start at the top-left cell `(0, 0)` and want to reach the bottom-right cell `(m - 1, n - 1)`. You can only move **right** or **down** at any point in time.

The score of a path is the sum of the values of the cells visited. However, there is a constraint: visiting a cell with a **non-zero** value costs 1 unit. You can have a total path cost of at most `k`.

Return the **maximum possible path score**. If it is impossible to reach the destination within the constraint, return `-1`.

---

## Approach: 3D Dynamic Programming 

Standard pathfinding on a grid usually requires 2D DP. Because we need to track a secondary constraint (the number of non-zero cells visited), we introduce a third dimension to our DP table to represent the current "cost" spent.

### Key Ideas:
1.  **State Definition:** `dp[i][j][c]` represents the maximum path score to reach cell `(i, j)` using exactly `c` units of cost (non-zero cells).
2.  **Transitions:** At any cell `(i, j)`, you check the potential next move (Down or Right):
    - If the target cell is `0`, the cost remains `c`.
    - If the target cell is `> 0`, the cost increases to `c + 1`.
    - We only update the state if the new cost `c + cost <= k`.
3.  **Initialization:** We start at `(0, 0)` with a score of `0` and `0` cost spent (assuming the starting cell's value is handled during transitions or doesn't count towards the initial cost in this specific implementation).
4.  **Final Result:** After filling the table, the maximum value in `dp[m-1][n-1][0...k]` gives our answer.



---

## Code 
```python
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        # INF for unreachable paths
        INF = float("-inf")
        # dp[row][col][cost_used]
        dp = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        
        # Base case: Starting at (0,0) with 0 score and 0 non-zero cells counted
        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for c in range(k + 1):
                    # Skip if this state hasn't been reached
                    if dp[i][j][c] == INF:
                        continue

                    # Move Down
                    if i + 1 < m:
                        val = grid[i + 1][j]
                        cost = 0 if val == 0 else 1
                        if c + cost <= k:
                            dp[i + 1][j][c + cost] = max(
                                dp[i + 1][j][c + cost], 
                                dp[i][j][c] + val
                            )

                    # Move Right
                    if j + 1 < n:
                        val = grid[i][j + 1]
                        cost = 0 if val == 0 else 1
                        if c + cost <= k:
                            dp[i][j + 1][c + cost] = max(
                                dp[i][j + 1][c + cost], 
                                dp[i][j][c] + val
                            )

        # Get the maximum score at the destination among all valid costs
        ans = max(dp[m - 1][n - 1])
        return -1 if ans < 0 else ans
```

---

## Complexity Analysis 

* **Time Complexity:** $O(m \times n \times k)$
    - We visit each cell in the grid and, for each cell, iterate through $k+1$ possible costs.
* **Space Complexity:** $O(m \times n \times k)$
    - To store the 3D DP table. 
    - *Note: This could be reduced to $O(n \times k)$ by only keeping the current and previous row's data.*

---

## Tags 
`Dynamic-Programming`, `Matrix`, `Path-Finding`, `Grid`, `Medium-Logic`
