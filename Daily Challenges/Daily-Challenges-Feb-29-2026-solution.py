# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1689](https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/)

# 🧠 Problem Description
# [Github LeetCode 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1689.%20Partitioning%20Into%20Minimum%20Number%20Of%20Deci-Binary%20Numbers)

class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        # Verilen n stringi içindeki her bir karakteri (rakamı) gez,
        # en büyük olanı bul ve tamsayıya çevirerek döndür.
        # Örneğin n = "82734" ise içindeki en büyük rakam 8'dir.
        # Bu durumda en az 8 tane deci-binary sayıya ihtiyaç duyulur.
        return int(max(n))
        