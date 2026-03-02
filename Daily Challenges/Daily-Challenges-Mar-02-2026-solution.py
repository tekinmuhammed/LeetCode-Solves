# 1536. Minimum Swaps to Arrange a Binary Grid

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1536](https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/description/)

# 🧠 Problem Description
# [Github LeetCode 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1689.%20Partitioning%20Into%20Minimum%20Number%20Of%20Deci-Binary%20Numbers)

class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        # Her satır için sondaki ardışık sıfır sayısını hesapla
        trailing_zeros = []
        for row in grid:
            count = 0
            for i in range(n - 1, -1, -1):
                if row[i] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        
        res = 0
        for i in range(n):
            # i. satır için gereken minimum sıfır sayısı n - 1 - i
            target = n - 1 - i
            
            # Bu koşulu sağlayan en yakın satırı bul
            found = -1
            for j in range(i, n):
                if trailing_zeros[j] >= target:
                    found = j
                    break
            
            # Eğer uygun satır yoksa imkansızdır
            if found == -1:
                return -1
            
            # Bulunan satırı i. pozisyona kadar kaydır (swap simülasyonu)
            # j'den i'ye kadar olan her bir adım bir swap işlemidir
            res += (found - i)
            
            # Listede satırların yerini kaydırarak güncelle
            val = trailing_zeros.pop(found)
            trailing_zeros.insert(i, val)
            
        return res