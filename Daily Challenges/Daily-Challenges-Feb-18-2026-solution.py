# 693. Binary Number with Alternating Bits

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 693](https://leetcode.com/problems/binary-number-with-alternating-bits/description/)

# 🧠 Problem Description
# [Github LeetCode 693. Binary Number with Alternating Bits](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/693.%20Binary%20Number%20with%20Alternating%20Bits)

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """
        Bit Manipülasyonu Yöntemi (O(1) Karmaşıklık)
        """
        # 1. Adım: Sayıyı bir sağa kaydır ve kendisiyle XORla.
        # Eğer n = 5 (101) ise:
        # n >> 1 = 2 (010)
        # x = 101 ^ 010 = 111 (Tüm bitler 1 oldu)
        x = n ^ (n >> 1)
        
        # 2. Adım: Oluşan x sayısının tüm bitlerinin 1 olup olmadığını kontrol et.
        # Eğer x = 111 (7) ise, x + 1 = 1000 (8) olur.
        # 0111 & 1000 = 0000 (0) sonucunu verir.
        # Eğer dönüşümlü olmasaydı (örn n=7, 111), x içinde 0 bitleri olurdu ve bu işlem 0 dönmezdi.
        return (x & (x + 1)) == 0

    # --- Alternatif Basit Yöntem (String) ---
    # def hasAlternatingBits(self, n: int) -> bool:
    #     bits = bin(n) # Örn: '0b101'
    #     return "00" not in bits and "11" not in bits