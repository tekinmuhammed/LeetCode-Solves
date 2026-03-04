# 1582. Special Positions in a Binary Matrix

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 1582](https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/)

# 🧠 Problem Description
# [Github LeetCode 1582. Special Positions in a Binary Matrix](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1582.%20Special%20Positions%20in%20a%20Binary%20Matrix)

class Solution(object):
    def numSpecial(self, mat):
        m = len(mat)
        n = len(mat[0])
        
        row_sum = [0] * m
        col_sum = [0] * n
        
        # count 1s in rows and columns
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_sum[i] += 1
                    col_sum[j] += 1
        
        count = 0
        
        # check special positions
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    count += 1
        
        return count