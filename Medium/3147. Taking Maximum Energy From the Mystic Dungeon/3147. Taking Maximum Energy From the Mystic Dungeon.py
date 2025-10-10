class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(energy)
        dp = [0] * n
        
        # dp[i] = i'den başlayıp i+k, i+2k ... ilerleyerek toplanabilecek maksimum enerji
        # Son elemanlardan başa doğru hesaplanır.
        for i in range(n - 1, -1, -1):
            if i + k < n:
                dp[i] = energy[i] + dp[i + k]
            else:
                dp[i] = energy[i]
        
        # En yüksek enerjiyi döndür
        return max(dp)