# 🎲 LeetCode 837 - New 21 Game

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 368](https://leetcode.com/problems/new-21-game/description/)

# 🧠 Problem Description 
# [Github LeetCode 837 - New 21 Game](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/837.%20New%2021%20Game)

class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        # Eğer Alice hiç kart çekmeden (k == 0) veya
        # maksimum puan n'yi geçemiyorsa -> kesin kazanır
        if k == 0 or n >= k + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)  # dp[x] = x puanla başlarsak kazanma olasılığı
        dp[0] = 1.0
        window_sum = 1.0  # sliding window toplamı
        result = 0.0

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts
            if i < k:
                window_sum += dp[i]   # hala kart çekebilir
            else:
                result += dp[i]       # artık duruyor
            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]

        return result