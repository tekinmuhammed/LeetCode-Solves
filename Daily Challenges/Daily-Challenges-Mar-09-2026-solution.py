# 3129. Find All Possible Stable Binary Arrays I

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 3129](https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/)

# 🧠 Problem Description
# [Github LeetCode 3129. Find All Possible Stable Binary Arrays I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3129.%20Find%20All%20Possible%20Stable%20Binary%20Arrays%20I)

class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        """
        :type zero: int
        :type one: int
        :type limit: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # dp[i][j][k]: i tane 0, j tane 1 kullanılarak oluşturulan 
        # ve k (0 veya 1) ile biten kararlı dizilerin sayısı.
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Temel durumlar: Sadece bir rakamdan oluşan ve limiti aşmayan diziler
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
            
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # 0 ile bitenleri hesapla:
                # Bir önceki adımda 0 veya 1 ile biten her şeye 0 ekleyebiliriz.
                # dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1]
                # Ancak ardışık 0 sayısı limit+1 olduysa o durumu çıkarmalıyız.
                # Çıkarılacak durum: dp[i-limit-1][j][1] (limit tane 0 eklemeden önceki durum)
                
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                if i > limit:
                    dp[i][j][0] = (dp[i][j][0] - dp[i-limit-1][j][1] + MOD) % MOD
                
                # 1 ile bitenleri hesapla (aynı mantık):
                dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                if j > limit:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j-limit-1][0] + MOD) % MOD
                    
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD