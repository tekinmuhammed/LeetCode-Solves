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