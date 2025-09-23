# 🔁 LeetCode 3335 - Total Characters in String After Transformations I

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 3335](https://leetcode.com/problems/total-characters-in-string-after-transformations-i)

# 🧠 Problem Description 
# [Github LeetCode 3335 - Total Characters in String After Transformations I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3335.%20Total%20Characters%20in%20String%20After%20Transformations%20I)

class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0] * 26
        for i in range(26):
            dp[i] = 1
        for _ in range(t):
            new_dp = [0] * 26
            for i in range(26):
                if i == 25:
                    new_dp[i] = (dp[0] + dp[1]) % MOD
                else:
                    new_dp[i] = dp[i + 1]
            dp = new_dp
        total = 0
        for ch in s:
            idx = ord(ch) - ord('a')
            total = (total + dp[idx]) % MOD
        return total