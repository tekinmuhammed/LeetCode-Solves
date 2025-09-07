# 🟦 LeetCode 1975 - Maximum Matrix Sum

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1975](https://leetcode.com/problems/maximum-matrix-sum)

# 🧠 Problem Description
# [Github LeetCode 1975 - Maximum Matrix Sum](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1975.%20Maximum%20Matrix%20Sum)

class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total_sum = 0
        min_abs = float('inf')
        negative_count = 0

        for row in matrix:
            for num in row:
                total_sum += abs(num)
                min_abs = min(min_abs, abs(num))
                if num < 0:
                    negative_count += 1
        if negative_count % 2 == 0:
            return total_sum
        else:
            return total_sum - 2 * min_abs