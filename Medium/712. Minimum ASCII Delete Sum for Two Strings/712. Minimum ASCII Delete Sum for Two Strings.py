class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        m, n = len(s1), len(s2)
        
        # dp[i][j]: s1[i:] ve s2[j:] eşit yapmak için minimum ASCII silme maliyeti
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # s1 bitmişse, s2'nin kalanını sil
        for j in range(n - 1, -1, -1):
            dp[m][j] = dp[m][j + 1] + ord(s2[j])
        
        # s2 bitmişse, s1'in kalanını sil
        for i in range(m - 1, -1, -1):
            dp[i][n] = dp[i + 1][n] + ord(s1[i])
        
        # DP doldurma
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(
                        ord(s1[i]) + dp[i + 1][j],
                        ord(s2[j]) + dp[i][j + 1]
                    )
        
        return dp[0][0]