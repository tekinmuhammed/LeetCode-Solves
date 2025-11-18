# 717. 1-bit and 2-bit Characters

# **Difficulty:** Easy  
# **Link:** [LeetCode 717](https://leetcode.com/problems/1-bit-and-2-bit-characters/description/)

# 🧠 Problem Description 
# [Github LeetCode 717. 1-bit and 2-bit](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/717.%201-bit%20and%202-bit%20Characters)

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        n = len(bits)

        while i < n - 1:  # last bit is checked separately
            if bits[i] == 1:
                i += 2   # 2-bit character
            else:
                i += 1   # 1-bit character

        return i == n - 1