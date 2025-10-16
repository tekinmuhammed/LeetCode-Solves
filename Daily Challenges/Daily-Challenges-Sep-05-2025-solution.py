# 2749. Minimum Operations to Make the Integer Zero

# **Difficulty:** Medium  
# **Link:** [LeetCode 2749](https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/)

# 🧠 Problem Description 
# [Github LeetCode 2749. Minimum Operations to Make the Integer Zero](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2749.%20Minimum%20Operations%20to%20Make%20the%20Integer%20Zero)

class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        for k in range(1, 61):  # en fazla 60 adım çünkü 2^i ≤ 2^60
            target = num1 - k * num2
            if target < 0:
                return -1
            # target ikilikte yazılabilir ve en az k bit gerekir
            if bin(target).count("1") <= k <= target:
                return k
        return -1