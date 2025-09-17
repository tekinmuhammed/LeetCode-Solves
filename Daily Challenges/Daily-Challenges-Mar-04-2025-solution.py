# 🔢 LeetCode 1780 - Check if Number is a Sum of Powers of Three

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1780](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three)

# 🧠 Problem Description
# [Github LeetCode 1780 - Check if Number is a Sum of Powers of Three](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1780.%20Check%20if%20Number%20is%20a%20Sum%20of%20Powers%20of%20Three)

class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 0:
            if n % 3 ==2:
                return False
            n //= 3
        return True