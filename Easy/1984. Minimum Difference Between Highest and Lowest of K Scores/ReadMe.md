## 1984. Minimum Difference Between Highest and Lowest of K Scores

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1984](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/)

---

### Problem Özeti

Bir tamsayı dizisi `nums` ve bir tamsayı `k` veriliyor.

Amaç:
- `nums` içinden **k adet eleman seç**
- Bu k eleman arasındaki  
  **maksimum − minimum** farkını **en küçük** yap

Seçilen elemanların **ardışık olması gerekmez**, sadece fark önemli.

---

## Temel Fikir

Bu problem doğrudan şu gözleme dayanır:

> Bir kümede max − min farkını minimize etmek istiyorsan,  
> **sıralı dizide ardışık k eleman seçmek yeterlidir.**

Neden?
- Sıralama sonrası herhangi bir optimal k kümesi, dizide bir aralığa karşılık gelir
- Araya başka eleman girmesi farkı ancak büyütür

---

## Algoritma

1. Eğer `k == 1` ise:
   - Tek elemanın farkı `0` → direkt dön
2. Diziyi sırala
3. Kaydırmalı pencere (sliding window) uygula:
   - Her `i` için:
     - `nums[i + k - 1] - nums[i]`
4. En küçük farkı bul ve döndür

---

## Python Kodu

```python
class Solution(object):
    def minimumDifference(self, nums, k):
        if k == 1:
            return 0

        nums.sort()
        res = float('inf')

        for i in range(len(nums) - k + 1):
            res = min(res, nums[i + k - 1] - nums[i])

        return res
```

### Örnek
```python
nums = [9,4,1,7]
k = 2

Sıralı: [1,4,7,9]

Pencereler:
[1,4] → 3
[4,7] → 3
[7,9] → 2

Cevap = 2 ✅
```

### Karmaşıklık Analizi
- **Zaman:**
- - Sıralama → `O(n log n)`
- - Tek geçiş → `O(n)`

- **Alan:**
- - `O(1)` (yerinde sıralama)