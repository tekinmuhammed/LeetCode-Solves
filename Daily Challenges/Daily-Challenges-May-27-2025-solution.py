# 🔢 LeetCode 2894 - Divisible and Non-divisible Sums Difference

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 2894](https://leetcode.com/problems/divisible-and-non-divisible-sums-difference)

# 🧠 Problem Description 
# [Github LeetCode 2894 - Divisible and Non-divisible Sums Difference](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2894.%20Divisible%20and%20Non-divisible%20Sums%20Difference)

class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        num1 = 0
        num2 = 0

        for i in range(1, n + 1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        
        return num1 - num2