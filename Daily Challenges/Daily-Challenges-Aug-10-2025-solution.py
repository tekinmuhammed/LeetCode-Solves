# LeetCode 869 - Reordered Power of 2

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 869](https://leetcode.com/problems/reordered-power-of-2/description/)

# 🧠 Problem Description 
# [Github LeetCode 869 - Reordered Power of 2](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/869.%20Reordered%20Power%20of%202)

class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power_of_two_digits = {"".join(sorted(str(1 << i))) for i in range(31)}

        return "".join(sorted(str(n)))  in power_of_two_digits