# 120. Triangle

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 120](https://leetcode.com/problems/triangle/description/)

# 🧠 Problem Description
# [Github LeetCode 120. Triangle](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/120.%20Triangle)

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Son satırdan başlayarak yukarıya doğru hesaplama yap
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

        return triangle[0][0]