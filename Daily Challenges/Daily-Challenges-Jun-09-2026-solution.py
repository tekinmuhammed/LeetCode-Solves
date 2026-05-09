# 1914. Cyclically Rotating a Grid

# **Difficulty:** Medium 
# **Problem Link:** [LeetCode 1914](https://leetcode.com/problems/cyclically-rotating-a-grid/description/)

# 🧠 Problem Description 
# [Github LeetCode 1914. Cyclically Rotating a Grid](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1914.%20Cyclically%20Rotating%20a%20Grid) 

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        nlayer = min(m // 2, n // 2)  # level count
        # enumerate each layer counterclockwise starting from the top-left corner
        for layer in range(nlayer):
            r = []  # row index of each element
            c = []  # column index of each element
            val = []  # value of each element
            for i in range(layer, m - layer - 1):  # left
                r.append(i)
                c.append(layer)
                val.append(grid[i][layer])
            for j in range(layer, n - layer - 1):  # down
                r.append(m - layer - 1)
                c.append(j)
                val.append(grid[m - layer - 1][j])
            for i in range(m - layer - 1, layer, -1):  # right
                r.append(i)
                c.append(n - layer - 1)
                val.append(grid[i][n - layer - 1])
            for j in range(n - layer - 1, layer, -1):  # up
                r.append(layer)
                c.append(j)
                val.append(grid[layer][j])
            total = len(val)  # total number of elements in each layer
            kk = k % total  # equivalent number of rotations
            # find the value at each index after rotation
            for i in range(total):
                idx = (
                    i + total - kk
                ) % total  # the index corresponding to the value after rotation
                grid[r[i]][c[i]] = val[idx]
        return grid