# 1009. Complement of Base 10 Integer

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 1009](https://leetcode.com/problems/complement-of-base-10-integer/)

# 🧠 Problem Description
# [Github LeetCode 1009. Complement of Base 10 Integer](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1009.%20Complement%20of%20Base%2010%20Integer)

class Solution(object):
    def bitwiseComplement(self, n):
        if n == 0:
            return 1
        
        mask = 0
        temp = n
        
        while temp > 0:
            mask = (mask << 1) | 1
            temp >>= 1
        
        return n ^ mask