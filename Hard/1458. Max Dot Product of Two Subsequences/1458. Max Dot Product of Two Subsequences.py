class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)

        # dp[i][j]: nums1[0..i-1] ve nums2[0..j-1] kullanılarak
        # elde edilebilecek maksimum dot product
        dp = [[-10**18] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                product = nums1[i - 1] * nums2[j - 1]

                dp[i][j] = max(
                    product,                       # sadece bu çifti başlat
                    dp[i - 1][j - 1] + product,    # önceki subsequence'e ekle
                    dp[i - 1][j],                  # nums1'den atla
                    dp[i][j - 1]                   # nums2'den atla
                )

        return dp[n][m]