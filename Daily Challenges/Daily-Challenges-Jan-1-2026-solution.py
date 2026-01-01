# 66. Plus One

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 66](https://leetcode.com/problems/plus-one)

# 🧠 Problem Description
# [Github LeetCode 66. Plus One](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/66.%20Plus%20One-2)

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits