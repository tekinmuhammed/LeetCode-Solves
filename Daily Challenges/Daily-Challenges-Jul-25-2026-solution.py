# 3536. Maximum Product of Two Digits

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 3536](https://leetcode.com/problems/maximum-product-of-two-digits/description/)

# 🧠 Problem Description
# [Github LeetCode 3536. Maximum Product of Two Digits ](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3536.%20Maximum%20Product%20of%20Two%20Digits)

class Solution:
    def maxProduct(self, n: int) -> int:
        first, second = 0, 0
        while n > 0:
            x = n % 10
            if x > first:
                first, second = x, first
            elif x > second:
                second = x
            n //= 10
        return first * second