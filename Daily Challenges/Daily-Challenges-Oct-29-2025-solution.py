# 🧮 LeetCode 3370 — Smallest Number With All Set Bits

# **Difficulty:** Easy
# **Link:** [LeetCode 3370](https://leetcode.com/problems/smallest-number-with-all-set-bits/description/)

# 🧠 Problem Description
# [Github LeetCode 3370 — Smallest Number With All Set Bits](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3370.%20Smallest%20Number%20With%20All%20Set%20Bits)

class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 1
        while (1 << k) - 1 < n:
            k += 1
        return (1 << k) - 1