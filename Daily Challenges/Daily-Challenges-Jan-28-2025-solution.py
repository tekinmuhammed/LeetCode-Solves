# 🐟 LeetCode 2658 - Maximum Number of Fish in a Grid

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2658](https://leetcode.com/problems/maximum-number-of-fish-in-a-grid)

# 🧠 Problem Description 
# [Github LeetCode 2658 - Maximum Number of Fish in a Grid](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2658.%20Maximum%20Number%20of%20Fish%20in%20a%20Grid)

class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            fish = grid[r][c]
            grid[r][c] = 0
            fish += dfs(r + 1, c)
            fish += dfs(r - 1, c)
            fish += dfs(r, c + 1)
            fish += dfs(r, c - 1)
            return fish
        max_fish = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    max_fish = max(max_fish, dfs(r, c))
        return max_fish