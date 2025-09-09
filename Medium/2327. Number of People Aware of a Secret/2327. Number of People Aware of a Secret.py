class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0] * (n + 1)   # dp[i] = i. günde sırrı öğrenen kişi sayısı
        dp[1] = 1            # 1. gün 1 kişi öğreniyor
        
        for day in range(1, n + 1):
            for share in range(day + delay, min(day + forget, n + 1)):
                dp[share] = (dp[share] + dp[day]) % MOD
        
        # Sırrı unutmayanlar
        ans = 0
        for day in range(n - forget + 1, n + 1):
            ans = (ans + dp[day]) % MOD
        
        return ans