class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        # DP[i][j][r]: (0, 0)'dan (i, j)'ye kadar, yol toplamının k'ya bölümünden kalanı r olan yolların sayısı.
        # DP dizisinin boyutları: m x n x k
        # Tüm değerler başlangıçta 0'dır.
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]

        # --- Temel Durum (Base Case): (0, 0) ---
        r0 = grid[0][0] % k
        dp[0][0][r0] = 1

        # --- DP Hesaplanması ---
        for i in range(m):
            for j in range(n):
                g_val = grid[i][j] % k  # Mevcut hücre değeri
                
                # Mevcut hücredeki DP değerlerini hesaplamak için tüm olası kalanları (r) kontrol et
                for r in range(k):
                    
                    # 1. Üstteki hücreden (i-1, j) gelme: Aşağı hareket
                    if i > 0:
                        # (i-1, j)'deki kalan r_prev olsun. r = (r_prev + g_val) % k
                        # r_prev = (r - g_val + k) % k
                        r_prev = (r - g_val + k) % k
                        dp[i][j][r] = (dp[i][j][r] + dp[i-1][j][r_prev]) % MOD

                    # 2. Soldaki hücreden (i, j-1) gelme: Sağa hareket
                    if j > 0:
                        # (i, j-1)'deki kalan r_prev olsun.
                        r_prev = (r - g_val + k) % k
                        dp[i][j][r] = (dp[i][j][r] + dp[i][j-1][r_prev]) % MOD

        # --- Sonuç ---
        # Sağ alt köşeye (m-1, n-1) ulaşıldığında, yol toplamının k'ya bölümünden kalanının 0 olduğu yollar.
        return dp[m-1][n-1][0]