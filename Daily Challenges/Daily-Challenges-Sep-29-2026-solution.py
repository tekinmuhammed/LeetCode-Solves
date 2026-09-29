# 2267. Check if There Is a Valid Parentheses String Path

# **Difficulty:** Hard
# **Problem Link:** [LeetCode 2267](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/description/)

# 🧠 Problem Description 
# [Github LeetCode 2267. Check if There Is a Valid Parentheses String Path](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/2267.%20Check%20if%20There%20Is%20a%20Valid%20Parentheses%20String%20Path)

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