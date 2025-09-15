# 🖌️ LeetCode 2661 - First Completely Painted Row or Column

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2661](https://leetcode.com/problems/first-completely-painted-row-or-column)

# 🧠 Problem Description 
# [Github LeetCode 2661 - First Completely Painted Row or Column](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2661.%20First%20Completely%20Painted%20Row%20or%20Column)

class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        row_count = [0] * m
        col_count = [0] * n
        position = {}
        for i in range(m):
            for j in range(n):
                position[mat[i][j]] = (i, j)
        for idx, num in enumerate(arr):
            r, c = position[num]
            row_count[r] += 1
            col_count[c] += 1
            if row_count[r] == n or col_count[c] ==m:
                return idx
        return -1