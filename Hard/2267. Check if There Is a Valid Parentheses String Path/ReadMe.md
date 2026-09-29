# 2267. Check if There Is a Valid Parentheses String Path

**Difficulty:** Hard  
**Problem Link:** [LeetCode 2267](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/description/)

---

## Problem
A parentheses string is a **valid parentheses string** (denoted VPS) if it meets standard parentheses matching rules (e.g., `"(())"` and `"()()"` are valid, while `")("` and `"(()"` are not).

You are given an `m x n` matrix `grid` of characters `grid[i][j]` consisting of `'('` and `')'`.

A path from the top-left cell `(0, 0)` to the bottom-right cell `(m - 1, n - 1)` is considered valid if:
1. You can only move **down** or **right**.
2. The sequence of characters along the path forms a valid parentheses string.

Return `true` if there exists a valid parentheses string path in the grid. Otherwise, return `false`.

---

# Approach

A naïve approach of exploring all paths and tracking the number of open parentheses can lead to a state explosion. However, the maximum number of unmatched open parentheses at any point cannot exceed the length of the path (which is `n + m - 1`). 

To optimize this, we can use **Dynamic Programming (DP) with Bitmasking**. 
Instead of storing a list or set of possible unmatched open parentheses counts for each cell, we can represent these possibilities as bits in a single large integer. 
* If the $k$-th bit of `dp[i][j]` is `1`, it means there is a valid path to cell `(i, j)` with exactly $k$ unmatched `'('`s.

Steps:
1. **Early Terminations**: 
   * A valid parentheses string must have an even length. The path length is exactly `n + m - 1`. If this is odd, return `False`.
   * A valid string must start with `'('` and end with `')'`. If `grid[0][0] == ')'` or `grid[n-1][m-1] == '('`, return `False`.
2. **DP Initialization**: Create a 2D array `dp` initialized to 0. 
   Set `dp[0][0] = 1 << 1` (which equals `2`). This sets the 1st bit to `1`, meaning we start with exactly 1 unmatched `'('`.
3. **State Transitions**: Iterate through every cell.
   * If the current cell is `'('`, it increases our unmatched count by 1. This corresponds to a **left bit-shift** (`<< 1`) of the bitmasks from the cells above and to the left.
   * If the current cell is `')'`, it decreases our unmatched count by 1 (matching an open parenthesis). This corresponds to a **right bit-shift** (`>> 1`).
   * We combine the reachable states from the top and left using the bitwise OR operator (`|`).
4. **Final Check**: At the destination `dp[n-1][m-1]`, we check if the 0-th bit is set by performing a bitwise AND with `1` (`dp[n-1][m-1] & 1`). If it is, a path exists that leaves 0 unmatched parentheses.

---

# Code

```python
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        path_len = n + m - 1

        if path_len % 2 == 1:
            return False
        if grid[0][0] != "(" or grid[n - 1][m - 1] != ")":
            return False

        dp = [[0] * m for _ in range(n)]

        dp[0][0] = 1 << 1

        for i in range(n):
            for j in range(m):
                change = 1 if grid[i][j] == "(" else -1

                if i > 0:
                    if change == 1:
                        dp[i][j] |= dp[i - 1][j] << 1
                    else:
                        dp[i][j] |= dp[i - 1][j] >> 1

                if j > 0:
                    if change == 1:
                        dp[i][j] |= dp[i][j - 1] << 1
                    else:
                        dp[i][j] |= dp[i][j - 1] >> 1

        return bool(dp[n - 1][m - 1] & 1)
```

---

# Example Walkthrough

Consider a 3x2 grid:
```text
(  (
(  )
)  )
```
Path length = `3 + 2 - 1 = 4` (Even, proceed).
Starts with `(`, ends with `)` (Valid, proceed).

**Tracing DP (Bit representations):**

* **`(0, 0)` is `(`**: `dp[0][0] = 2` (Binary `10` -> 1 unmatched)
* **`(0, 1)` is `(`**: Comes from left. `change = 1` (left shift). `2 << 1 = 4` (Binary `100` -> 2 unmatched).
* **`(1, 0)` is `(`**: Comes from top. `change = 1` (left shift). `2 << 1 = 4` (Binary `100` -> 2 unmatched).
* **`(1, 1)` is `)`**: Comes from top & left. Both are `4`. `change = -1` (right shift). `4 >> 1 = 2` (Binary `10` -> 1 unmatched).
* **`(2, 0)` is `)`**: Comes from top. `4 >> 1 = 2`.
* **`(2, 1)` is `)`** (Destination): Comes from top `(2, 0)` and left `(1, 1)`. Both are `2`. `change = -1` (right shift). `2 >> 1 = 1` (Binary `01` -> 0 unmatched).

At `(2, 1)`, the value is `1`. `1 & 1` evaluates to `True`. The path is valid!

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(M \times N)$

We visit each cell in the `M x N` grid exactly once. The bitwise shift operations and OR operations take $\mathcal{O}(1)$ time natively in Python for reasonably sized integers (the maximum bit length is the path length, which is $M+N$, max 200, well within Python's efficient large integer handling). 

Space Complexity

$\mathcal{O}(M \times N)$

We allocate a 2D list `dp` of size `M x N` to store the bitmasks. This could theoretically be optimized to $\mathcal{O}(N)$ by only keeping the previous row, but $\mathcal{O}(M \times N)$ is perfectly acceptable and allows for clean state tracking.