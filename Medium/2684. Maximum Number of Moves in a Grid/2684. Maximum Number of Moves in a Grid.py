class Solution(object):
    def maxMoves(self, grid):
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        for j in range(cols - 2, -1, -1):
            for i in range(rows):
                if i > 0 and grid [i][j] < grid[i - 1][j + 1]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i - 1][j + 1])
                if grid [i][j] < grid[i][j + 1]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i][j + 1])
                if i < rows - 1 and grid [i][j] < grid[i + 1][j + 1]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i + 1][j + 1])
        return max(dp[i][0] for i in range(rows))