# 3459. Length of Longest V-Shaped Diagonal Segment

# **Difficulty:** Hard
# **Link:** [LeetCode 3459](https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/)  

# 🧠 Problem Description
# [Github LeetCode 3459. Length of Longest V-Shaped Diagonal Segment](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/3459.%20Length%20of%20Longest%20V-Shaped%20Diagonal%20Segment)

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(cx, cy, direction, turn, target):
            nx, ny = cx + DIRS[direction][0], cy + DIRS[direction][1]
            # If it goes beyond the boundary or the next node's value is not the target value, then return
            if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != target:
                return 0
            turn_int = 1 if turn else 0
            # Continue walking in the original direction.
            max_step = dfs(nx, ny, direction, turn, 2 - target)
            if turn:
                # Clockwise rotate 90 degrees turn
                max_step = max(
                    max_step,
                    dfs(nx, ny, (direction + 1) % 4, False, 2 - target),
                )
            return max_step + 1

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for direction in range(4):
                        res = max(res, dfs(i, j, direction, True, 2) + 1)
        return res