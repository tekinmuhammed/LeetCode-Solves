# 1356. Sort Integers by The Number of 1 Bits

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 1356](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/)

# 🧠 Problem Description
# [Github LeetCode 1356. Sort Integers by The Number of 1 Bits](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1356.%20Sort%20Integers%20by%20The%20Number%20of%201%20Bits)

class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # arr dizisini yerinde (in-place) sıralıyoruz.
        # Sıralama kriteri olarak bir tuple veriyoruz: 
        # 1. Eleman: Sayının ikili gösterimindeki '1'lerin sayısı
        # 2. Eleman: Sayının kendi değeri (eşitlik durumunda tie-breaker olarak kullanılır)
        arr.sort(key=lambda x: (bin(x).count('1'), x))
        
        return arr

        # Not: Python 3.10 ve üzeri sürümlerde bin(x).count('1') yerine 
        # doğrudan x.bit_count() kullanılarak daha performanslı bir çözüm de yazılabilir:
        # arr.sort(key=lambda x: (x.bit_count(), x))
        # return arr