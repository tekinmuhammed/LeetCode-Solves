# 3000. Maximum Area of Longest Diagonal Rectangle

# **Difficulty:** Easy
# **Link:** [LeetCode 3000](https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/)  

# 🧠 Problem Description
# [Github LeetCode 3000. Maximum Area of Longest Diagonal Rectangle](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3000.%20Maximum%20Area%20of%20Longest%20Diagonal%20Rectangle)

import math

class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        max_diag = 0
        max_area = 0

        for l, w in dimensions:
            diag = math.sqrt(l*l + w*w)
            area = l * w

            if diag > max_diag:
                max_diag = diag
                max_area = area
            elif diag == max_diag:
                max_area = max(max_area, area)

        return max_area