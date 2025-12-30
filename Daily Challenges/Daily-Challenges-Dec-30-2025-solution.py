# 840. Magic Squares In Grid

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 840](https://leetcode.com/problems/magic-squares-in-grid/description/)

# 🧠 Problem Description
# [Github LeetCode 840. Magic Squares In Grid](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/840.%20Magic%20Squares%20In%20Grid)

class Solution(object):
    def numMagicSquaresInside(self, grid):
        rows, cols = len(grid), len(grid[0])
        
        def isMagic(r, c):
            # Center must be 5
            if grid[r+1][c+1] != 5:
                return False
            
            nums = []
            for i in range(r, r+3):
                for j in range(c, c+3):
                    nums.append(grid[i][j])
            
            # Must contain exactly numbers 1 to 9
            if set(nums) != set(range(1, 10)):
                return False
            
            s = sum(grid[r][c:c+3])
            
            # Check rows
            for i in range(r, r+3):
                if sum(grid[i][c:c+3]) != s:
                    return False
            
            # Check columns
            for j in range(c, c+3):
                if grid[r][j] + grid[r+1][j] + grid[r+2][j] != s:
                    return False
            
            # Check diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
                return False
            
            return True
        
        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagic(i, j):
                    count += 1
        
        return count