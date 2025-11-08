# 🧩 1611. Minimum One Bit Operations to Make Integers Zero

# **Difficulty:** Hard  
# **Problem Link:** [LeetCode 1611](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/)

# 🧠 Problem Description 
# [Github LeetCode 1611. Minimum One Bit Operations to Make Integers Zero](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/1611.%20Minimum%20One%20Bit%20Operations%20to%20Make%20Integers%20Zero1611.%20Minimum%20One%20Bit%20Operations%20to%20Make%20Integers%20Zero)

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        
        k = 0
        curr = 1
        while (curr * 2) <= n:
            curr *= 2
            k += 1

        return 2 ** (k + 1) - 1 - self.minimumOneBitOperations(n ^ curr)