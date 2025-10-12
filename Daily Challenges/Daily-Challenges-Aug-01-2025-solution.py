# 118. Pascal's Triangle

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 118](https://leetcode.com/problems/pascals-triangle/)

# 🧠 Problem Description 
# [Github LeetCode 118. Pascal's Triangle](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/118.%20Pascal's%20Triangle)

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            result.append(row)
        return result