# 🟩 LeetCode 1475 - Final Prices With a Special Discount in a Shop

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 1475](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/)

# 🧠 Problem Description 
# [Github LeetCode 1475 - Final Prices With a Special Discount in a Shop](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1475.%20Final%20Prices%20With%20a%20Special%20Discount%20in%20a%20Shop)

class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                prices[j] -= prices[i]
            stack.append(i)
        return prices