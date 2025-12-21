# 955. Delete Columns to Make Sorted II

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 955](https://leetcode.com/problems/delete-columns-to-make-sorted-ii/description/)

# 🧠 Problem Description
# [Github LeetCode 955. Delete Columns to Make Sorted II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/955.%20Delete%20Columns%20to%20Make%20Sorted%20II)

class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        m = len(strs[0])

        # pairs[i] = strs[i] and strs[i+1] kesin olarak sıralandı mı?
        sorted_pairs = [False] * (n - 1)
        deletions = 0

        for col in range(m):
            # Bu sütun sıralamayı bozuyor mu?
            bad = False
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break

            if bad:
                deletions += 1
                continue

            # Bu sütun bazı çiftleri kesin sıralı hale getirir
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_pairs[i] = True

            # Eğer tüm çiftler sıralandıysa erken çıkabiliriz
            if all(sorted_pairs):
                break

        return deletions