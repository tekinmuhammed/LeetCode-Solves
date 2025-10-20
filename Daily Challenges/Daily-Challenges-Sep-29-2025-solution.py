# 1039. Minimum Score Triangulation of Polygon

# **Difficulty:** Medium
# **Link:** [LeetCode 1039](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description/)

# 🧠 Problem Description
# [Github LeetCode 1039. Minimum Score Triangulation of Polygon](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1039.%20Minimum%20Score%20Triangulation%20of%20Polygon)

class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        
        # Uzunluk 3'ten başlayarak artar
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float("inf")
                for k in range(i+1, j):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + values[i]*values[j]*values[k]
                    )
        
        return dp[0][n-1]