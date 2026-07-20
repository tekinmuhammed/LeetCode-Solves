# 1260. Shift 2D Grid

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 1260](https://leetcode.com/problems/shift-2d-grid/description/)

# 🧠 Problem Description 
# [Github LeetCode 1260. Shift 2D Grid](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1260.%20Shift%202D%20Grid)

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not k: return grid
        r, c = len(grid), len(grid[0])
        n = r * c
        k %= n
        if not k: return grid

        def shift(i, j):
            while i < j:
                grid[i // c][i % c], grid[j // c][j % c] = grid[j // c][j % c], grid[i // c][i % c]
                i += 1
                j -= 1

        shift(0, n - 1)
        shift(0, k - 1)
        shift(k, n - 1)
        
        return grid 