# 📝 LeetCode 326. Power of Three

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 326](https://leetcode.com/problems/power-of-three/description/)

# 🧠 Problem Description 
# [Github LeetCode 326. Power of Three](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/326.%20Power%20of%20Three)

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1