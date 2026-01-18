# 🧩 1895. Largest Magic Square

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1895](https://leetcode.com/problems/largest-magic-square/description/)

# 🧠 Problem Description
# [Github LeetCode 3047. Find the Largest Area of Square Inside Two Rectangles](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3047.%20Find%20the%20Largest%20Area%20of%20Square%20Inside%20Two%20Rectangles)

class Solution(object):
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])

        # Prefix sums for rows and columns
        row_ps = [[0] * (n + 1) for _ in range(m)]
        col_ps = [[0] * n for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row_ps[i][j + 1] = row_ps[i][j] + grid[i][j]
                col_ps[i + 1][j] = col_ps[i][j] + grid[i][j]

        # Try square sizes from largest to smallest
        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):

                    target = row_ps[i][j + k] - row_ps[i][j]
                    ok = True

                    # Check rows
                    for r in range(i, i + k):
                        if row_ps[r][j + k] - row_ps[r][j] != target:
                            ok = False
                            break

                    # Check columns
                    for c in range(j, j + k):
                        if col_ps[i + k][c] - col_ps[i][c] != target:
                            ok = False
                            break

                    # Check diagonals
                    if ok:
                        d1 = d2 = 0
                        for t in range(k):
                            d1 += grid[i + t][j + t]
                            d2 += grid[i + t][j + k - 1 - t]
                        if d1 != target or d2 != target:
                            ok = False

                    if ok:
                        return k

        return 1