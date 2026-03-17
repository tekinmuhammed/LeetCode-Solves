# 1727. Largest Submatrix With Rearrangements 
 
# **Difficulty:** Medium 
# **Problem Link:** [LeetCode 1727](https://leetcode.com/problems/largest-submatrix-with-rearrangements/description/) 
 
# 🧠 Problem Description
# [Github LeetCode 1727. Largest Submatrix With Rearrangements](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1727.%20Largest%20Submatrix%20With%20Rearrangements) 
 
class Solution(object):
    def largestSubmatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        
        # build heights 
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        res = 0
        
        for i in range(m):
            row = sorted(matrix[i], reverse=True)
            
            for j in range(n):
                res = max(res, row[j] * (j + 1))
        
        return res