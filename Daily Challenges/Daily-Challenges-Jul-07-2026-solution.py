# 3754. Concatenate Non-Zero Digits and Multiply by Sum I

# **Difficulty:** Easy 
# **Problem Link:** [LeetCode 3754](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/description/)

# 🧠 Problem Description
# [Github LeetCode 3754. Concatenate Non-Zero Digits and Multiply by Sum I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3754.%20Concatenate%20Non-Zero%20Digits%20and%20Multiply%20by%20Sum%20I)

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        sum = 0
        for c in str(n):
            d = int(c)
            sum += d
            if d > 0:
                x = x * 10 + d
        return x * sum