## 3510. Minimum Pair Removal to Sort Array II

**Difficulty:** Hard
**Link:** [LeetCode 3510](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/description/)

# 🧠 Problem Description
# [Github LeetCode 3510. Minimum Pair Removal to Sort Array II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/3510.%20Minimum%20Pair%20Removal%20to%20Sort%20Array%20II)

import heapq

class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        # Diziyi ve bağlı liste yapısını simüle edecek diziler
        curr_vals = list(nums)
        left_neighbor = [-1] * n   # i. elemanın sol komşusunun indeksi
        right_neighbor = [-1] * n  # i. elemanın sağ komşusunun indeksi
        valid = [True] * n         # Eleman hala dizide mi yoksa silindi/birleşti mi?
        
        inv_count = 0  # Terslik sayısı (Sıralı olma kontrolü için)
        pq = []        # Min-Heap: (toplam, sol_indeks)
        
        # Başlangıç durumunu oluştur
        for i in range(n):
            if i > 0:
                left_neighbor[i] = i - 1
            if i < n - 1:
                right_neighbor[i] = i + 1
                
                # Terslik kontrolü (nums[i] > nums[i+1] ise sıralı değil)
                if nums[i] > nums[i+1]:
                    inv_count += 1
                
                # Çifti heap'e ekle
                heapq.heappush(pq, (nums[i] + nums[i+1], i))
        
        # Eğer başta zaten sıralıysa 0 döndür
        if inv_count == 0:
            return 0
            
        ops = 0
        
        # Dizi sıralı olana kadar (terslik kalmayana kadar) devam et
        while inv_count > 0:
            # Heap'ten geçerli en küçük toplamlı çifti çıkar
            while True:
                if not pq: break
                s, idx = heapq.heappop(pq)
                
                # Lazy Deletion kontrolü:
                # 1. Sol eleman hala geçerli mi?
                if not valid[idx]: continue
                
                r_idx = right_neighbor[idx]
                # 2. Sağ eleman hala geçerli mi?
                if r_idx == -1 or not valid[r_idx]: continue
                
                # 3. Heap'teki toplam güncel mi? (Değerler değişmiş olabilir)
                if s != curr_vals[idx] + curr_vals[r_idx]: continue
                    
                break
            
            # --- Birleştirme İşlemi (Merge) ---
            # L = idx (Sol), R = r_idx (Sağ).
            # R, L'nin içine birleşecek.
            L, R = idx, r_idx
            
            # 1. Terslik Sayısını Güncelle (Eski Bağlantıları Kaldır)
            prev = left_neighbor[L]
            next_node = right_neighbor[R]
            
            # L ve R arasındaki ilişki
            if curr_vals[L] > curr_vals[R]:
                inv_count -= 1
            # Prev ve L arasındaki ilişki
            if prev != -1 and curr_vals[prev] > curr_vals[L]:
                inv_count -= 1
            # R ve Next arasındaki ilişki
            if next_node != -1 and curr_vals[R] > curr_vals[next_node]:
                inv_count -= 1
                
            # 2. Değerleri ve Yapıyı Güncelle
            new_val = curr_vals[L] + curr_vals[R]
            curr_vals[L] = new_val
            valid[R] = False  # R elemanı artık yok (L ile birleşti)
            
            # Bağlantıları güncelle (R'yi aradan çıkar)
            right_neighbor[L] = next_node
            if next_node != -1:
                left_neighbor[next_node] = L
            
            # 3. Terslik Sayısını Güncelle (Yeni Bağlantıları Ekle)
            # Prev ve Yeni L
            if prev != -1 and curr_vals[prev] > curr_vals[L]:
                inv_count += 1
            # Yeni L ve Next
            if next_node != -1 and curr_vals[L] > curr_vals[next_node]:
                inv_count += 1
                
            # 4. Yeni oluşan çiftleri Heap'e ekle
            # Sol taraftaki yeni çift (Prev + L)
            if prev != -1:
                heapq.heappush(pq, (curr_vals[prev] + curr_vals[L], prev))
            
            # Sağ taraftaki yeni çift (L + Next)
            if next_node != -1:
                heapq.heappush(pq, (curr_vals[L] + curr_vals[next_node], L))
            
            ops += 1
            
        return ops