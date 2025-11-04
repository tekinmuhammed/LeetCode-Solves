# 🧮 LeetCode 3318 — Find X-Sum of All K-Long Subarrays I

## 🔗 Problem Link
[LeetCode 3318 - Find X-Sum of All K-Long Subarrays I](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/)

## 📘 Problem Tanımı  
Bir `nums` dizisi veriliyor.  
Her **uzunluğu `k` olan alt dizi (subarray)** için, o alt dizideki **en sık görülen `x` eleman** seçilir.  
Bu `x` elemanın her biri için `eleman * frekansı` çarpımı alınır ve hepsi toplanır.  

Sonuç olarak, her alt dizi için hesaplanan bu toplamları içeren bir liste döndürülür.

---

## 💡 Örnek

```python
Input: nums = [1,1,2,2,3], k = 3, x = 2
Output: [5, 8, 7]
```

**Açıklama:**

1. `[1,1,2]` → En sık 2 eleman: (1,2 kez), (2,1 kez) → 1×2 + 2×1 = 4

2. `[1,2,2]` → En sık 2 eleman: (2,2 kez), (1,1 kez) → 2×2 + 1×1 = 5

3. `[2,2,3]` → En sık 2 eleman: (2,2 kez), (3,1 kez) → 2×2 + 3×1 = 7

    Sonuç: `[4, 5, 7]`

### 🧠 Çözüm Mantığı

Her bir **k uzunluğundaki alt dizi** için:

1. `Counter` ile frekansları say.

2. Frekansları önce azalan frekans, sonra azalan değer sırasına göre sırala.

3. İlk `x` elemanı seç.

4. `num * frequency` çarpımlarını topla.

    Bu işlemi her alt dizi için tekrarla.

### 🧩 Kod
```python
from collections import Counter

class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = []

        for i in range(n - k + 1):
            sub = nums[i:i + k]
            freq = Counter(sub)
            
            # En sık görülen x elemanı bul (önce frekansa, sonra değere göre)
            most_common = sorted(freq.items(), key=lambda a: (-a[1], -a[0]))[:x]
            
            # Bu elemanların toplam katkısını hesapla
            s = 0
            for num, count in most_common:
                s += num * count
            ans.append(s)

        return ans
```

### ⚙️ Çalışma Örneği
**Örnek 1**
```python
nums = [1,1,2,2,3]
k = 3
x = 2

Alt diziler:
[1,1,2] → (1,2), (2,1) → 1×2 + 2×1 = 4
[1,2,2] → (2,2), (1,1) → 2×2 + 1×1 = 5
[2,2,3] → (2,2), (3,1) → 2×2 + 3×1 = 7

Output = [4, 5, 7]
```

### ⏱️ Zaman ve Bellek Karmaşıklığı
| Tür        | Karmaşıklık          |
| ---------- | -------------------- |
| **Zaman**  | O((n−k+1) × k log k) |
| **Bellek** | O(k)                 |

### 🧾 Özet
| Özellik             | Açıklama                                                    |
| ------------------- | ----------------------------------------------------------- |
| **Problem Türü**    | Frekans Sayımı, Sliding Window                              |
| **Zorluk**          | 🟩 Easy / 🟧 Medium                                         |
| **Temel Fikir**     | En sık görülen `x` eleman için `num * freq` toplamını almak |
| **Kullanılan Yapı** | `collections.Counter`, `sorted()`                           |

## 📌 Tags

`sliding-window`, `frequency-count`, `sorting`, `array`, `python`