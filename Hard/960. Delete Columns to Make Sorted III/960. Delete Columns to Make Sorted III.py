class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        m = len(strs[0])

        # dp[j] = j. sütun SON seçilen sütun olacak şekilde
        # maksimum tutulabilecek sütun sayısı
        dp = [1] * m

        for j in range(m):
            for i in range(j):
                # i -> j geçişi mümkün mü? (tüm satırlar için)
                valid = True
                for r in range(n):
                    if strs[r][i] > strs[r][j]:
                        valid = False
                        break
                if valid:
                    dp[j] = max(dp[j], dp[i] + 1)

        # tutulabilecek maksimum sütun sayısı
        keep = max(dp)

        # silinecek minimum sütun sayısı
        return m - keep