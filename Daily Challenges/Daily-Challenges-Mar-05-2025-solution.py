# 🟩 LeetCode 2579 - Count Total Number of Colored Cells

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 2579](https://leetcode.com/problems/count-total-number-of-colored-cells)

# 🧠 Problem Description
# [Github LeetCode 2579 - Count Total Number of Colored Cells](https://github.com/tekinmuhammed/LeetCode-Solves/edit/main/Medium/2579.%20Count%20Total%20Number%20of%20Colored%20Cells/ReadMe.md)

class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 1 + 4 * ((n - 1) * n) // 2