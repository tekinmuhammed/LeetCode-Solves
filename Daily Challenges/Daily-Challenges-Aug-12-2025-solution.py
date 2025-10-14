# 2787. Ways to Express an Integer as Sum of Powers

# **Difficulty:** Medium 
# **Problem Link:** [LeetCode 2787](https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/description/)

# 🧠 Problem Description 
# [Github LeetCode 2787. Ways to Express an Integer as Sum of Powers](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2787.%20Ways%20to%20Express%20an%20Integer%20as%20Sum%20of%20Powers)

class Solution(object):
    def numberOfWays(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # Kullanılabilecek tüm kuvvetler
        powers = []
        i = 1
        while i**x <= n:
            powers.append(i**x)
            i += 1

        # dp[s] = s toplamını oluşturmanın yolları
        dp = [0] * (n + 1)
        dp[0] = 1  # 0 toplamını oluşturmanın 1 yolu (hiç sayı seçmemek)

        # Her kuvveti yalnızca bir kez kullan (unique integers)
        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD

        return dp[n]