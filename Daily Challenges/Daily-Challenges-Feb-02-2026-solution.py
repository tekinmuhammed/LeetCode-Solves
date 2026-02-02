## 3013. Divide an Array Into Subarrays With Minimum Cost II

**Difficulty:** Hard  
**Problem Link:** [LeetCode 3013](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/description/)

# 🧠 Problem Description
# [Github LeetCode 3010. Divide an Array Into Subarrays With Minimum Cost I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3010.%20Divide%20an%20Array%20Into%20Subarrays%20With%20Minimum%20Cost%20I)

import heapq
from collections import defaultdict

class Solution:
    def minimumCost(self, nums: list[int], k: int, dist: int) -> int:
        n = len(nums)
        # nums[0] her zaman maliyete dahildir.
        base_cost = nums[0]
        
        # Geriye kalan k-1 elemanı seçmemiz gerekiyor.
        # İlk seçilen eleman (pivot) i olsun. Geriye k-2 eleman kalır.
        K = k - 2
        
        # Eğer K=0 ise (yani k=2), sadece 1 tane daha eleman seçmeliyiz.
        # Pivot i, constraint'i (i - i <= dist) her zaman sağlar.
        # Bu yüzden nums[1:] içindeki en küçük elemanı alırız.
        if K == 0:
            return base_cost + min(nums[1:])
        
        # --- Veri Yapıları ---
        L = []  # Max-Heap (En küçük K elemanı tutar, -val olarak saklanır)
        R = []  # Min-Heap (Geri kalan elemanları tutar, val olarak saklanır)
        L_sum = 0
        L_size = 0 # L içindeki geçerli (silinmemiş) eleman sayısı
        
        # Lazy Removal (Tembel Silme) için sayaçlar
        rem_L = defaultdict(int)
        rem_R = defaultdict(int)
        
        # Heap'lerin tepesindeki silinmiş elemanları temizleyen fonksiyonlar
        def clean_L():
            while L and rem_L[-L[0]] > 0:
                rem_L[-L[0]] -= 1
                heapq.heappop(L)
        
        def clean_R():
            while R and rem_R[R[0]] > 0:
                rem_R[R[0]] -= 1
                heapq.heappop(R)
        
        # Eleman ekleme fonksiyonu
        def add(val):
            nonlocal L_sum, L_size
            # Önce L'ye eklemeyi dene (En küçüklerin arasına girebilir mi?)
            heapq.heappush(L, -val)
            L_sum += val
            L_size += 1
            
            # Eğer L'nin boyutu K'yı aşarsa, en büyüğünü R'ye at
            if L_size > K:
                clean_L()
                out = -heapq.heappop(L)
                L_sum -= out
                L_size -= 1
                heapq.heappush(R, out)
            
            # Dengeleme: L'nin en büyüğü R'nin en küçüğünden büyük olmamalı
            clean_L()
            clean_R()
            if L and R and -L[0] > R[0]:
                l_val = -heapq.heappop(L)
                r_val = heapq.heappop(R)
                L_sum = L_sum - l_val + r_val
                heapq.heappush(L, -r_val)
                heapq.heappush(R, l_val)

        # Eleman çıkarma fonksiyonu
        def remove(val):
            nonlocal L_sum, L_size
            clean_L()
            
            # Elemanın hangi heap'te olduğuna karar ver (tahmini)
            # Eğer val <= max(L) ise L'dedir.
            is_in_L = False
            if L and val <= -L[0]:
                is_in_L = True
            
            if is_in_L:
                rem_L[val] += 1
                L_sum -= val
                L_size -= 1
            else:
                rem_R[val] += 1
            
            # Eğer L'den eleman sildiysek ve eksildiyse, R'den takviye yap
            if L_size < K:
                clean_R()
                if R:
                    in_val = heapq.heappop(R)
                    heapq.heappush(L, -in_val)
                    L_sum += in_val
                    L_size += 1

        # --- Algoritma ---
        
        # Başlangıç Penceresi: nums[2 ... dist+1]
        # i=1 (pivot) için, havuz [2, dist+1] aralığıdır.
        # Bu aralığı heap'lere doldur.
        for idx in range(2, min(n, dist + 2)):
            add(nums[idx])
            
        min_total_cost = float('inf')
        
        # i (pivot) 1'den başlar, sona doğru kayar
        # i, seçilen alt dizilerin ilkinin (nums[0] hariç) başlangıcıdır.
        for i in range(1, n - K):
            
            # Eğer havuzda yeterince (K tane) eleman varsa maliyeti hesapla
            if L_size == K:
                current_cost = base_cost + nums[i] + L_sum
                if current_cost < min_total_cost:
                    min_total_cost = current_cost
            
            # Pencereyi Kaydır (Sliding Window)
            
            # 1. Eski pivotun hemen sağındaki eleman (nums[i+1]) artık havuzdan çıkmalı.
            # Çünkü bir sonraki adımda (i+1) o eleman pivot olacak.
            if i + 1 < n:
                remove(nums[i+1])
            
            # 2. Pencerenin sağına yeni giren elemanı (nums[i+dist+1]) havuza ekle.
            if i + dist + 1 < n:
                add(nums[i + dist + 1])
                
        return min_total_cost