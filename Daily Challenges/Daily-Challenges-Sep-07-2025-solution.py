# 1304. Find N Unique Integers Sum up to Zero

# **Difficulty:** Easy  
# **Link:** [LeetCode 1304](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/)

# 🧠 Problem Description 
# [Github LeetCode 1304. Find N Unique Integers Sum up to Zero](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1304.%20Find%20N%20Unique%20Integers%20Sum%20up%20to%20Zero)

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)
        if n % 2 == 1:
            res.append(0)
        return res