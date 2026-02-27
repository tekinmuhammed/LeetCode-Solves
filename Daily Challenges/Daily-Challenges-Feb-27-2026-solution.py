# 3666. Minimum Operations to Equalize Binary String

# **Difficulty:** Hard
# **Link:** [LeetCode 3666](https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/description/)

# 🧠 Problem Description
# [Github LeetCode 3666. Minimum Operations to Equalize Binary String](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/3666.%20Minimum%20Operations%20to%20Equalize%20Binary%20String)

import math

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        cnt_0 = s.count('0')
        
        # 1. Durum: Eğer dizide hiç '0' yoksa sıfır işlemle zaten hedefe ulaşılmıştır.
        if cnt_0 == 0:
            return 0
            
        # 2. Durum: k dizinin boyutuna eşitse, ya tümünü tek hamlede çevirebiliriz ya da imkansızdır.
        if k == n:
            if cnt_0 == n:
                return 1
            else:
                return -1
                
        # 3. Durum: k çiftse, m*k her zaman çifttir. Bu yüzden sıfırların sayısı (cnt_0) tek olamaz.
        if k % 2 == 0 and cnt_0 % 2 != 0:
            return -1
            
        # O(1) Formülüzasyonu: Gerekli minimum m'yi matematiksel olarak bulma
        if k % 2 == 1:
            # k tekse: m * k % 2 == cnt_0 % 2 olmalıdır.
            # Yani m'nin tek/çift durumu, cnt_0'ın tek/çift durumuna tamamen bağlıdır.
            
            if cnt_0 % 2 == 0:
                # m kesinlikle ÇİFT olmalı.
                m = max((cnt_0 + k - 1) // k, (cnt_0 + (n - k) - 1) // (n - k))
                if m % 2 != 0:
                    m += 1 # Eğer tek çıktıysa, sıradaki ilk çift sayıya yükselt
                return m
            else:
                # m kesinlikle TEK olmalı.
                m = max((cnt_0 + k - 1) // k, ((n - cnt_0) + (n - k) - 1) // (n - k))
                if m % 2 == 0:
                    m += 1 # Eğer çift çıktıysa, sıradaki ilk tek sayıya yükselt
                return m
                
        else:
            # k çiftse: m herhangi bir (tek veya çift) değere sahip olabilir.
            # Hem olası tek m'leri hem olası çift m'leri hesaplayıp en küçüğünü (minimum) alırız.
            
            # En küçük olası ÇİFT m değeri:
            m_even = max((cnt_0 + k - 1) // k, (cnt_0 + (n - k) - 1) // (n - k))
            if m_even % 2 != 0:
                m_even += 1
                
            # En küçük olası TEK m değeri:
            m_odd = max((cnt_0 + k - 1) // k, ((n - cnt_0) + (n - k) - 1) // (n - k))
            if m_odd % 2 == 0:
                m_odd += 1
                
            return min(m_even, m_odd)