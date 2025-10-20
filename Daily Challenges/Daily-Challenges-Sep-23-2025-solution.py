# 165. Compare Version Numbers

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 165](https://leetcode.com/problems/compare-version-numbers/description/)

# 🧠 Problem Description 
# [Github LeetCode 165. Compare Version Numbers](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/165.%20Compare%20Version%20Numbers)

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))

        # Uzunlukları eşitle (eksik yerlere 0 ekle)
        max_len = max(len(v1), len(v2))
        v1.extend([0] * (max_len - len(v1)))
        v2.extend([0] * (max_len - len(v2)))

        # Karşılaştırma
        for a, b in zip(v1, v2):
            if a < b:
                return -1
            elif a > b:
                return 1
        return 0