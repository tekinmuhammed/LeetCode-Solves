# 3225. Maximum Score From Grid Operations

**Difficulty:** Hard  
**Problem Link:** [LeetCode 3225](https://leetcode.com/problems/maximum-score-from-grid-operations/)

---

## Problem Description

You are given an $n \times n$ grid of non-negative integers. Your goal is to maximize the score by selecting a height $h_c$ (ranging from $0$ to $n$) for each column $c$. 

When a column $c$ has height $h_c$, the first $h_c$ cells of that column are "blacked out." A cell at $(r, c)$ contributes to the score if:
1. It is **not** blacked out ($r \ge h_c$).
2. It is **adjacent** to at least one blacked-out cell in an adjacent column ($c-1$ or $c+1$).

Return the **maximum possible score**.

---

## Approach: Optimized 3D Dynamic Programming

The core challenge is that the score of column $c$ depends on its own height $h_c$ AND the heights of its neighbors $h_{c-1}$ and $h_{c+1}$. This local dependency suggests a DP where we process the grid column by column.

### Key Ideas:
1.  **State Definition:** `dp[i][curr_h][prev_h]` represents the maximum score accumulated up to column $i$, where the $i$-th column has height `curr_h` and the $(i-1)$-th column has height `prev_h`.
2.  **Column Prefix Sums:** To calculate the score in $O(1)$, we pre-compute `col_sum[c][r]`, which stores the sum of the first $r$ elements in column $c$.
3.  **Score Logic:**
    - If $h_{i-1} > h_i$, column $i$ gains points from row $h_i$ to $h_{i-1}$.
    - If $h_i > h_{i-1}$, column $i-1$ gains points from row $h_{i-1}$ to $h_i$ (calculated during the transition to column $i$).
4.  **Optimization:** A naive transition would be $O(N^4)$ (for each column, iterate through $h_i$, $h_{i-1}$, and $h_{i-2}$). By using **prefix/suffix maximums** (`prev_max`, `prev_suffix_max`), we reduce the complexity of transitions to $O(N^3)$.
5.  **Base Case:** If $n=1$, no column has neighbors, so the score is $0$.

---

## Code

```python
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        if n == 1:
            return 0

        # dp[i][curr_h][prev_h]
        dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n)]
        prev_max = [[0] * (n + 1) for _ in range(n + 1)]
        prev_suffix_max = [[0] * (n + 1) for _ in range(n + 1)]
        col_sum = [[0] * (n + 1) for _ in range(n)]

        # Step 1: Pre-compute column prefix sums
        for c in range(n):
            for r in range(1, n + 1):
                col_sum[c][r] = col_sum[c][r - 1] + grid[r - 1][c]

        # Step 2: Iterate through columns
        for i in range(1, n):
            for curr_h in range(n + 1):
                for prev_h in range(n + 1):
                    if curr_h <= prev_h:
                        # Column i gets points because neighbor i-1 is taller
                        extra_score = col_sum[i][prev_h] - col_sum[i][curr_h]
                        dp[i][curr_h][prev_h] = max(
                            dp[i][curr_h][prev_h],
                            prev_suffix_max[prev_h][0] + extra_score,
                        )
                    else:
                        # Column i-1 gets points because current i is taller
                        extra_score = (
                            col_sum[i - 1][curr_h] - col_sum[i - 1][prev_h]
                        )
                        dp[i][curr_h][prev_h] = max(
                            dp[i][curr_h][prev_h],
                            prev_suffix_max[prev_h][curr_h],
                            prev_max[prev_h][curr_h] + extra_score,
                        )

            # Step 3: Update optimization tables for the next column
            for curr_h in range(n + 1):
                prev_max[curr_h][0] = dp[i][curr_h][0]
                for prev_h in range(1, n + 1):
                    penalty = (
                        col_sum[i][prev_h] - col_sum[i][curr_h]
                        if prev_h > curr_h
                        else 0
                    )
                    prev_max[curr_h][prev_h] = max(
                        prev_max[curr_h][prev_h - 1],
                        dp[i][curr_h][prev_h] - penalty,
                    )

                prev_suffix_max[curr_h][n] = dp[i][curr_h][n]
                for prev_h in range(n - 1, -1, -1):
                    prev_suffix_max[curr_h][prev_h] = max(
                        prev_suffix_max[curr_h][prev_h + 1],
                        dp[i][curr_h][prev_h],
                    )

        # Step 4: Find the maximum score in the final states
        ans = 0
        for k in range(n + 1):
            ans = max(ans, dp[n - 1][n][k], dp[n - 1][0][k])

        return ans
```

---

## Complexity Analysis

* **Time Complexity:** $O(n^3)$
    - We iterate through $n$ columns.
    - For each column, we have two nested loops of size $n+1$ for `curr_h` and `prev_h`.
    - Prefix/suffix maximum updates are also $O(n^2)$.
* **Space Complexity:** $O(n^3)$
    - The 3D DP table `dp` stores $n \times (n+1) \times (n+1)$ states.
    - *Note: This could be optimized to $O(n^2)$ since we only use the previous column's state.*

---

## Tags
Dynamic-Programming, Matrix, Prefix-Sum, Optimization, Hard-Logic