# 498. Diagonal Traverse

# **Difficulty:** Medium
# **Link:** [LeetCode 498](https://leetcode.com/problems/diagonal-traverse/)  

# 🧠 Problem Description
# [Github LeetCode 498. Diagonal Traverse](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/498.%20Diagonal%20Traverse)

class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        direction = 1  # 1: yukarı sağa, -1: aşağı sola

        for _ in range(m * n):
            result.append(mat[row][col])
            
            # yön yukarı sağa
            if direction == 1:
                if col == n - 1:
                    row += 1
                    direction = -1
                elif row == 0:
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1
            
            # yön aşağı sola
            else:
                if row == m - 1:
                    col += 1
                    direction = 1
                elif col == 0:
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1
        
        return result