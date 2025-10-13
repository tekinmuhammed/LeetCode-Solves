# LeetCode 2438 - Range Product Queries of Powers

# **Difficulty:** Medium 
# **Problem Link:** [LeetCode 2438](https://leetcode.com/problems/range-product-queries-of-powers/description)

# 🧠 Problem Description 
# [Github LeetCode 2438 - Range Product Queries of Powers](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2438.%20Range%20Product%20Queries%20of%20Powers)

class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        powers = []
        bit = 0

        while n > 0:
            if n & 1:
                powers.append(1 << bit)
            bit += 1
            n >>= 1

        result = []
        for left, right in queries:
            prod = 1
            for i in range(left, right + 1):
                prod = (prod * powers[i]) % MOD
            result.append(prod)
        return result