# 🎮 LeetCode 2017 - Grid Game

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2017](https://leetcode.com/problems/grid-game/)

# 🧠 Problem Description 
# [Github LeetCode 2017 - Grid Game](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2017.%20Grid%20Game)

class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        top_prefix = [0] * n
        bottom_prefix = [0] * n
        top_prefix[0] = grid[0][0]
        bottom_prefix[0] = grid[1][0]

        for i in range(1, n):
            top_prefix[i] = top_prefix[i - 1] + grid[0][i]
            bottom_prefix[i] = bottom_prefix[i - 1] + grid[1][i]
        result = float("inf")
        for i in range(n):
            top_points = top_prefix[-1] - top_prefix[i]
            bottom_points = bottom_prefix[i - 1] if i > 0 else 0
            result = min(result, max(top_points, bottom_points))
        return result