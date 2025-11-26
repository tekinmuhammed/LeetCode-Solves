# 2435. Paths in Matrix Whose Sum Is Divisible by K — Explanation & Analysis

**Difficulty:** Hard  
**Link:** [LeetCode 2435](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/description/)

## 🧩 Problem Summary
Count the number of paths from **(0,0)** to **(m−1,n−1)** in a grid such that:

- You may move **only right or down**
- The **sum of the path** is **divisible by k**
- Return the count modulo **10⁹ + 7**

---

## 💡 Key Insight
We only care about the **sum modulo k**, not the full sum.  
Therefore we use:
```python
dp[i][j][r] = number of paths to cell (i, j) with sum % k == r
```

**We transition from:**

- Top → (i−1, j)
- Left → (i, j−1)

And apply modulo transitions.

---

## 🧠 Why This Works

Instead of checking all paths (which is exponential), we track only the possible **k remainders** at each cell.

- Time: **O(m × n × k)**
- Space: **O(m × n × k)**

Efficient and optimal.

---

## ✅ Code (Your Solution)

```python
class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        dp = [[[0] * k for _ in range(n)] for _ in range(m)]

        r0 = grid[0][0] % k
        dp[0][0][r0] = 1

        for i in range(m):
            for j in range(n):
                g_val = grid[i][j] % k
                
                for r in range(k):

                    if i > 0:
                        prev = (r - g_val + k) % k
                        dp[i][j][r] = (dp[i][j][r] + dp[i-1][j][prev]) % MOD

                    if j > 0:
                        prev = (r - g_val + k) % k
                        dp[i][j][r] = (dp[i][j][r] + dp[i][j-1][prev]) % MOD

        return dp[m-1][n-1][0]
```

### 📘 Approach Summary

- Each cell tracks counts for all possible remainders.

- Transitions use reverse modulo arithmetic:
```python
previous = (current - grid[i][j] + k) % k
```

- Final answer is:
```python
dp[m-1][n-1][0]
```