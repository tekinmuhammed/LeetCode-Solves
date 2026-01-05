# 1975. Maximum Matrix Sum

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1975](https://leetcode.com/problems/maximum-matrix-sum/description/)

# 🧠 Problem Description
# [Github LeetCode 1975. Maximum Matrix Sum](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1975.%20Maximum%20Matrix%20Sum-2)

class Solution(object):
    def maxMatrixSum(self, matrix):
        total = 0
        neg_count = 0
        min_abs = float('inf')
        
        for row in matrix:
            for val in row:
                if val < 0:
                    neg_count += 1
                total += abs(val)
                min_abs = min(min_abs, abs(val))
        
        if neg_count % 2 == 1:
            total -= 2 * min_abs
        
        return total