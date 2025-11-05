# 💡 LeetCode 3321 — Find X-Sum of All K-Long Subarrays II

**Difficulty:** Hard
**Problem Link:** [LeetCode 3321](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/description/)

## 📘 Problem Tanımı  
Bu problem, **3318. Find X-Sum of All K-Long Subarrays I** probleminin optimize edilmiş sürümüdür.  
Amaç yine aynı:  
Her **k uzunluğundaki alt dizi (subarray)** için **en sık görülen `x` elemanı** bulup, bu elemanların  
`num * frequency` çarpımlarının toplamını almak.  

Ancak burada, çözüm **verimli bir şekilde** (O(n log n)) yapılmalıdır.  
Bunun için **kayar pencere (sliding window)** ve **SortedList** kullanılır.

---

## 🧩 Temel Fikir

1. `nums` üzerinde kayan bir pencere (uzunluk = `k`) hareket eder.
2. Her yeni eleman pencereye eklenir, eski eleman çıkarılır.
3. Pencere içindeki elemanların frekansları `Helper` sınıfı tarafından yönetilir.
4. `Helper`:
   - Elemanları frekans ve değere göre sıralar.
   - En sık görülen `x` elemanı `large` listesinde tutar.
   - Kalan elemanları `small` listesinde saklar.
   - `result`, şu anda en sık görülen `x` elemanın `num * frequency` toplamını temsil eder.

---

## 🧠 Çözüm Mantığı

- `Helper.insert(num)`  
  → Yeni elemanı pencereye ekler, frekansını günceller.  
- `Helper.remove(num)`  
  → Pencereden çıkan elemanı siler, frekansını azaltır.  
- `Helper.get()`  
  → Şu anda en sık görülen `x` elemanların `num * freq` toplamını döndürür.

Bu sayede her kaydırma adımında (O(log n) karmaşıklıkla) toplam hesaplanır.

---

## 🧩 Kod

```python
from sortedcontainers import SortedList
from collections import defaultdict

class Helper:
    def __init__(self, x):
        self.x = x
        self.result = 0
        self.large = SortedList()  # En sık görülen x eleman
        self.small = SortedList()  # Diğer elemanlar
        self.occ = defaultdict(int)  # Eleman frekansları

    def insert(self, num):
        if self.occ[num] > 0:
            self.internal_remove((self.occ[num], num))
        self.occ[num] += 1
        self.internal_insert((self.occ[num], num))

    def remove(self, num):
        self.internal_remove((self.occ[num], num))
        self.occ[num] -= 1
        if self.occ[num] > 0:
            self.internal_insert((self.occ[num], num))

    def get(self):
        return self.result

    def internal_insert(self, p):
        # Eğer large dolu değilse veya eleman large'taki en küçük elemandan büyükse, large'a ekle
        if len(self.large) < self.x or p > self.large[0]:
            self.result += p[0] * p[1]
            self.large.add(p)
            if len(self.large) > self.x:
                to_remove = self.large[0]
                self.result -= to_remove[0] * to_remove[1]
                self.large.remove(to_remove)
                self.small.add(to_remove)
        else:
            self.small.add(p)

    def internal_remove(self, p):
        # Eleman large içindeyse çıkar
        if self.large and p >= self.large[0]:
            self.result -= p[0] * p[1]
            self.large.remove(p)
            if self.small:
                to_add = self.small[-1]
                self.result += to_add[0] * to_add[1]
                self.small.remove(to_add)
                self.large.add(to_add)
        else:
            self.small.remove(p)


class Solution:
    def findXSum(self, nums, k, x):
        helper = Helper(x)
        ans = []

        for i in range(len(nums)):
            helper.insert(nums[i])
            if i >= k:
                helper.remove(nums[i - k])
            if i >= k - 1:
                ans.append(helper.get())

        return ans
```

### 📊 Örnek
```python
nums = [1, 2, 2, 3, 1]
k = 3
x = 2

# Alt diziler:
# [1,2,2] → (2,2 kez), (1,1 kez) → 2*2 + 1*1 = 5
# [2,2,3] → (2,2 kez), (3,1 kez) → 2*2 + 3*1 = 7
# [2,3,1] → (2,1 kez), (3,1 kez) → 2*1 + 3*1 = 5

Output = [5, 7, 5]
```

### ⏱️ Zaman ve Bellek Karmaşıklığı
| Tür        | Karmaşıklık |
| ---------- | ----------- |
| **Zaman**  | O(n log n)  |
| **Bellek** | O(n)        |


### 🧾 Özet
| Özellik          | Açıklama                                        |
| ---------------- | ----------------------------------------------- |
| **Problem Türü** | Sliding Window, Frequency Counting              |
| **Zorluk**       | 🟧 Medium / 🟥 Hard                             |
| **Yapı**         | SortedList, defaultdict                         |
| **Avantaj**      | Önceki O(n·k·log k) çözümü O(n log n)’e indirir |