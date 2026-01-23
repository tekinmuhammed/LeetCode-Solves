## 3510. Minimum Pair Removal to Sort Array II

**Difficulty:** Hard  
**Link:** [LeetCode 3510](https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/)

---

### Problem Özeti

Bir dizi `nums` veriliyor.  
Aşağıdaki işlemi istediğin kadar yapabilirsin:

- Yan yana duran iki elemanı seç
- Bu iki elemanı diziden sil
- Yerlerine **toplamlarını** tek bir eleman olarak koy

Amaç:
> Diziyi **non-decreasing (artan veya eşit)** hale getirmek için gereken **minimum işlem sayısını** bulmak.

⚠️ **Problem I’den farkı:**  
Bu versiyonda `n` çok daha büyük olduğu için **O(n²)** çözümler TLE olur.  
Daha verimli bir yapı şart.

---

## Temel Fikir

Bu çözüm üç ana yapı üzerine kurulu:

1. **Min-Heap (Priority Queue)**  
   - Yan yana çiftlerin `(toplam, sol_indeks)` bilgisi tutulur
   - Her adımda **en küçük toplamlı çift** seçilir (greedy)

2. **Bağlı Liste Simülasyonu (Arrays ile)**  
   - `left_neighbor[i]`, `right_neighbor[i]`
   - Eleman silme / birleştirme işlemleri **O(1)**

3. **Inversion Count (Terslik Sayısı)**  
   - Dizi sıralı mı kontrolü için
   - `nums[i] > nums[i+1]` olan her durum bir tersliktir
   - `inv_count == 0` → dizi sıralı

---

## Neden Inversion Count?

Her adımda tüm diziyi kontrol etmek pahalı olur.  
Bunun yerine:

- Başta toplam terslik sayısını hesaplıyoruz
- Her merge işleminde:
  - Eski ilişkilerden gelen terslikleri **çıkar**
  - Yeni oluşan ilişkilerden gelen terslikleri **ekle**
- Böylece sıralı olup olmadığını **O(1)** kontrol ediyoruz

---

## Lazy Deletion (Heap Optimizasyonu)

Heap’te eski (artık geçersiz) çiftler kalabilir.  
Bu yüzden heap’ten eleman alırken şu kontroller yapılır:

- Sol indeks hâlâ geçerli mi?
- Sağ komşu hâlâ var mı?
- Heap’teki toplam güncel mi?

Geçerli değilse → **atla**

---

## Algoritma Adımları

1. Başlangıçta:
   - Heap’e tüm yan yana çiftleri ekle
   - `inv_count` hesapla
2. `inv_count > 0` iken:
   - Heap’ten geçerli en küçük toplamlı çifti al
   - Bu iki elemanı birleştir
   - Bağlı listeyi güncelle
   - `inv_count`’u lokal olarak güncelle
   - Yeni oluşan komşu çiftleri heap’e ekle
   - `ops += 1`
3. `inv_count == 0` olduğunda sonucu döndür

---

## Python Kodu

```python
import heapq

class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        curr_vals = list(nums)
        left_neighbor = [-1] * n
        right_neighbor = [-1] * n
        valid = [True] * n
        
        inv_count = 0
        pq = []
        
        for i in range(n):
            if i > 0:
                left_neighbor[i] = i - 1
            if i < n - 1:
                right_neighbor[i] = i + 1
                if nums[i] > nums[i + 1]:
                    inv_count += 1
                heapq.heappush(pq, (nums[i] + nums[i + 1], i))
        
        if inv_count == 0:
            return 0
        
        ops = 0
        
        while inv_count > 0:
            while True:
                s, idx = heapq.heappop(pq)
                if not valid[idx]:
                    continue
                r_idx = right_neighbor[idx]
                if r_idx == -1 or not valid[r_idx]:
                    continue
                if s != curr_vals[idx] + curr_vals[r_idx]:
                    continue
                break
            
            L, R = idx, r_idx
            prev = left_neighbor[L]
            next_node = right_neighbor[R]
            
            if curr_vals[L] > curr_vals[R]:
                inv_count -= 1
            if prev != -1 and curr_vals[prev] > curr_vals[L]:
                inv_count -= 1
            if next_node != -1 and curr_vals[R] > curr_vals[next_node]:
                inv_count -= 1
            
            curr_vals[L] += curr_vals[R]
            valid[R] = False
            
            right_neighbor[L] = next_node
            if next_node != -1:
                left_neighbor[next_node] = L
            
            if prev != -1 and curr_vals[prev] > curr_vals[L]:
                inv_count += 1
            if next_node != -1 and curr_vals[L] > curr_vals[next_node]:
                inv_count += 1
            
            if prev != -1:
                heapq.heappush(pq, (curr_vals[prev] + curr_vals[L], prev))
            if next_node != -1:
                heapq.heappush(pq, (curr_vals[L] + curr_vals[next_node], L))
            
            ops += 1
        
        return ops
Karmaşıklık Analizi
Zaman:

Heap işlemleri → O(n log n)

Her eleman en fazla bir kez merge edilir
→ O(n log n)

Alan:

Yardımcı diziler + heap
→ O(n)

