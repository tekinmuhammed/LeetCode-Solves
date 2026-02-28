# 1680. Concatenation of Consecutive Binary Numbers

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1680](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/description/)

# 🧠 Problem Description
# [Github LeetCode 3666. Minimum Operations to Equalize Binary String](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/3666.%20Minimum%20Operations%20to%20Equalize%20Binary%20String)

class Solution(object):
    def concatenatedBinary(self, n):
        MOD = 10**9 + 7
        result = 0
        bit_length = 0

        for i in range(1, n + 1):
            # i power of two ise bit sayısı artar
            if i & (i - 1) == 0:
                bit_length += 1

            result = ((result << bit_length) | i) % MOD

        return result