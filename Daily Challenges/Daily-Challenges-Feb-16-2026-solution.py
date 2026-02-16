# 190. Reverse Bits

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 190](https://leetcode.com/problems/reverse-bits/description/)

# 🧠 Problem Description
# [Github LeetCode 190. Reverse Bits](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/190.%20Reverse%20Bits)

class Solution(object):
    def reverseBits(self, n):
        result = 0
        
        for _ in range(32):
            result <<= 1        # sola kaydır
            result |= (n & 1)   # son biti ekle
            n >>= 1             # n'i sağa kaydır
        
        return result