# 🧩 2943. Maximize Area of Square Hole in Grid

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2943](https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/description/)

# 🧠 Problem Description
# [Github LeetCode 2943. Maximize Area of Square Hole in Grid](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2943.%20Maximize%20Area%20of%20Square%20Hole%20in%20Grid)

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        # En uzun ardışık çubuk dizisini bulmak için yardımcı fonksiyon
        def get_max_gap(bars):
            if not bars:
                return 1
            
            # Sıralama önemli çünkü ardışıklığı kontrol edeceğiz
            bars.sort()
            
            max_len = 1
            current_len = 1
            
            for i in range(1, len(bars)):
                # Eğer şimdiki çubuk bir öncekinin tam 1 fazlasıysa ardışıktır
                if bars[i] == bars[i-1] + 1:
                    current_len += 1
                else:
                    # Ardışıklık bozuldu, max'ı güncelle ve sıfırla
                    max_len = max(max_len, current_len)
                    current_len = 1
            
            # Döngü bittiğinde son zinciri de kontrol et
            max_len = max(max_len, current_len)
            
            # Gap (Boşluk) uzunluğu, ardışık çubuk sayısının 1 fazlasıdır.
            # Örn: [2] -> Gap 2 (1. ve 3. çubuklar sabit, 2. kalkınca arada 2 birim olur)
            # Örn: [2, 3] -> Gap 3
            return max_len + 1

        # Yatay ve dikeydeki maksimum boşlukları hesapla
        max_h = get_max_gap(hBars)
        max_v = get_max_gap(vBars)
        
        # Kare olacağı için en küçük kenarı al
        side = min(max_h, max_v)
        
        return side * side