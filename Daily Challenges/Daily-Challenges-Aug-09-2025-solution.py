# LeetCode 231 - Power of Two

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 231](https://leetcode.com/problems/power-of-two/description/)

# 🧠 Problem Description 
# [Github LeetCode 231 - Power of Two](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/231.%20Power%20of%20Two)

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return  n > 0 and (n & (n - 1)) == 0