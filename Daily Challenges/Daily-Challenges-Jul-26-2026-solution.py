# 628. Maximum Product of Three Numbers

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 628](https://leetcode.com/problems/maximum-product-of-three-numbers/description/)

# 🧠 Problem Description
# [Github LeetCode 628. Maximum Product of Three Numbers](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/628.%20Maximum%20Product%20of%20Three%20Numbers)

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        (a, b, c), (x, y) = nlargest(3, nums), nsmallest(2, nums)
        return max(a * b * c, a * x * y)