# 3070. Count Submatrices with Top-Left Element and Sum Less Than k 

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 3070](https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/)

# 🧠 Problem Description
# [Github LeetCode 3070. Count Submatrices with Top-Left Element and Sum Less Than k](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3070.%20Count%20Submatrices%20with%20Top-Left%20Element%20and%20Sum%20Less%20Than%20k) 

class Solution(object):
    def countSubmatrices(self, grid, k):
        m, n = len(grid), len(grid[0])
        
        # prefix sum in-place
        for i in range(m):
            for j in range(n):
                if i > 0:
                    grid[i][j] += grid[i-1][j]
                if j > 0:
                    grid[i][j] += grid[i][j-1]
                if i > 0 and j > 0:
                    grid[i][j] -= grid[i-1][j-1]
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] <= k:
                    res += 1
        
        return res