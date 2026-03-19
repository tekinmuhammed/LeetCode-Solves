# 3212. Count Submatrices With Equal Frequency of X and Y 
 
# **Difficulty:** Medium   
# **Problem Link:** [LeetCode 3212](https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/)

# 🧠 Problem Description 
# [Github LeetCode 3070. Count Submatrices with Top-Left Element and Sum Less Than k](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3212.%20Count%20Submatrices%20With%20Equal%20Frequency%20of%20X%20and%20Y) 


class Solution(object):
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        
        diff = [[0]*n for _ in range(m)]
        countX = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                val = 0
                if grid[i][j] == 'X':
                    val = 1
                elif grid[i][j] == 'Y':
                    val = -1
                
                diff[i][j] = val
                countX[i][j] = 1 if grid[i][j] == 'X' else 0
                
                if i > 0:
                    diff[i][j] += diff[i-1][j]
                    countX[i][j] += countX[i-1][j]
                if j > 0:
                    diff[i][j] += diff[i][j-1]
                    countX[i][j] += countX[i][j-1]
                if i > 0 and j > 0:
                    diff[i][j] -= diff[i-1][j-1]
                    countX[i][j] -= countX[i-1][j-1]
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if diff[i][j] == 0 and countX[i][j] > 0:
                    res += 1
        
        return res