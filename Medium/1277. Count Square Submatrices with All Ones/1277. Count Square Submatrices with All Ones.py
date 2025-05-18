class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        count = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:    
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    count += dp[i][j]
        return count
matrix = [
    [0,1,1,1],
    [1,1,1,1],
    [0,1,1,1]
]

solution = Solution()
result = solution.countSquares(matrix)
print(result)