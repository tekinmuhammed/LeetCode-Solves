## 1877. Minimize Maximum Pair Sum in Array

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1877](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/)

---

### Problem Özeti

Bir dizi `nums` veriliyor (eleman sayısı **çift**).  
Amaç:

- Dizideki elemanları **ikili eşleştir**
- Her eşleşme için `pair_sum = a + b`
- Bu eşleşmeler arasındaki **en büyük pair sum** değerini **minimum** yap

Sonuç olarak:
> Oluşabilecek **en küçük maksimum ikili toplamı** döndür.

---

## Temel Fikir (Greedy)

Bu problem klasik ve çok net bir **greedy + sorting** sorusu.

### Neden sıralama?

- En **küçük** elemanı en **büyük** elemanla eşleştirirsen:
  - Büyük sayının etkisini dengelersin
  - Aksi halde (büyük + büyük) çok daha büyük maksimum değerler oluşur

📌 Optimal strateji:
- En küçük + en büyük
- İkinci küçük + ikinci büyük
- …

---

## Algoritma

1. Diziyi sırala
2. İki pointer kullan:
   - `l` → baştan
   - `r` → sondan
3. Her adımda:
   - `nums[l] + nums[r]` hesapla
   - Maksimum sonucu güncelle
   - `l++`, `r--`
4. Tüm eşleşmeler bitince sonucu döndür

---

## Neden Doğru?

- En büyük sayı mutlaka bir çiftte yer alacak
- Onu **en küçük** ile eşleştirmek, maksimum değeri minimize eder
- Bu strateji global optimum sağlar (exchange argument)

---

## Python Kodu
```python
class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        res = 0
        l, r = 0, len(nums) - 1

        while l < r:
            res = max(res, nums[l] + nums[r])
            l += 1
            r -= 1

        return res
```

### Örnek
```python
nums = [3,5,2,3]

Sıralı: [2,3,3,5]

Eşleşmeler:
2 + 5 = 7
3 + 3 = 6

Maksimum = 7 ✅
```

### Karmaşıklık Analizi
- **Zaman:**
- - Sıralama → `O(n log n)`
- - Tek geçiş → `O(n)`
- - Toplam: `O(n log n)`

- **Alan:**
- - Yerinde sıralama → `O(1)` (Python Timsort hariç)

