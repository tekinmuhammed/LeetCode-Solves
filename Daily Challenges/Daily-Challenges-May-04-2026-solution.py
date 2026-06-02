# 48. Rotate Image 

# **Zorluk:** Medium 
# **Problem Linki:** [LeetCode 48](https://leetcode.com/problems/rotate-image/description/?)

# 🧠 Problem Description
# [Github LeetCode 48. Rotate Image](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/48.%20Rotate%20Image) 

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None (Matrisi yerinde değiştirir)
        """
        n = len(matrix)
        
        # 1. Adım: Transpoz (Diyagonal üzerinden yansıtma)
        for i in range(n):
            # j'yi i + 1'den başlatarak sadece üst üçgeni dolaşırız
            # Böylece elemanları bir kez takas etmiş oluruz
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 2. Adım: Her satırı ters çevirme (Yatay yansıtma)
        for row in matrix:
            row.reverse()