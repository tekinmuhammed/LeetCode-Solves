# 🟨 LeetCode 2257 - Count Unguarded Cells in the Grid

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2257](https://leetcode.com/problems/count-unguarded-cells-in-the-grid)

# 🧠 Problem Description
# [Github LeetCode 2257 - Count Unguarded Cells in the Grid](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2257.%20Count%20Unguarded%20Cells%20in%20the%20Grid)


class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [[0] * n for _ in range(m)]
        for r, c in walls:
            grid[r][c] = 1
        for r, c in guards:
            grid[r][c] = 2
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0<= nc < n and grid[nr][nc] != 1 and grid[nr][nc] != 2:
                    grid [nr][nc] = 3
                    nr += dr
                    nc += dc
        unguarded_count = sum(1 for r in range(m) for c in range(n) if grid[r][c] == 0)
        return unguarded_count