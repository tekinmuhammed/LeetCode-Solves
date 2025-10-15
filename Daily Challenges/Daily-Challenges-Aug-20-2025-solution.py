# 1277. Count Square Submatrices with All Ones  

# **Difficulty:** Medium  
# **Link:** [LeetCode 1277](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)  

# 🧠 Problem Description 
# [Github LeetCode 1277. Count Square Submatrices with All Ones ](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1277.%20Count%20Square%20Submatrices%20with%20All%20Ones-2)

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        total = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:   # ilk satır veya ilk sütun
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    total += dp[i][j]

        return total