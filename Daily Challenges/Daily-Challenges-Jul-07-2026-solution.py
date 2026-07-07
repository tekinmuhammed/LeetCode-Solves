# 3754. Concatenate Non-Zero Digits and Multiply by Sum I

**Difficulty:** Easy
**Problem Link:** [LeetCode 3754](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/description/)

# 🧠 Problem Description  
# [Github LeetCode 3558. Number of Ways to Assign Edge Weights I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3558.%20Number%20of%20Ways%20to%20Assign%20Edge%20Weights%20I)

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