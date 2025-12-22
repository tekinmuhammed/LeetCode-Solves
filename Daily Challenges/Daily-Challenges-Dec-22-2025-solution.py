# 960. Delete Columns to Make Sorted III

# **Difficulty:** Hard  
# **Problem Link:** [LeetCode 960](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/description/)

# 🧠 Problem Description
# [Github LeetCode 960. Delete Columns to Make Sorted III](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/960.%20Delete%20Columns%20to%20Make%20Sorted%20III)

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