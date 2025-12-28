# 1351. Count Negative Numbers in a Sorted Matrix

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 1351](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/)

# 🧠 Problem Description
# [Github LeetCode 1351. Count Negative Numbers in a Sorted Matrix](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1351.%20Count%20Negative%20Numbers%20in%20a%20Sorted%20Matrix)

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        row, col = m - 1, 0
        count = 0

        while row >= 0 and col < n:
            if grid[row][col] < 0:
                count += (n - col)
                row -= 1
            else:
                col += 1

        return count