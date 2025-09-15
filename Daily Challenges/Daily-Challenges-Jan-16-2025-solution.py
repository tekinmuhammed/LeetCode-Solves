# ⚡ LeetCode 2429 - Minimize XOR

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2429](https://leetcode.com/problems/minimize-xor/)

# 🧠 Problem Description 
# [Github LeetCode 2429 - Minimize XOR](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2429.%20Minimize%20XOR)

class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        set_bits_count = bin(num2).count('1')
        result = 0

        for i in xrange(31, -1, -1):
            if set_bits_count > 0 and (num1 & (1 << i)):
                result |= (1 << i)
                set_bits_count -= 1
        for i in xrange(32):
            if set_bits_count > 0 and not (result & (1 << i)):
                result |= (1 << i)
                set_bits_count -= 1
        return result