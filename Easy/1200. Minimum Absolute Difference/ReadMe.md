## 1200. Minimum Absolute Difference

**Difficulty:** Easy
**Link:** [LeetCode 1200](https://leetcode.com/problems/minimum-absolute-difference/description/)

---

### Problem Özeti

Bir tamsayı dizisi `arr` veriliyor.

Amaç:
- Dizideki **iki farklı eleman** arasındaki **mutlak farkı minimum** yapan değeri bulmak
- Bu **minimum farka sahip olan tüm çiftleri** artan sırayla döndürmek

> Çiftler `[a, b]` şeklinde olmalı ve `a < b` olmalı.

---

## Temel Gözlem

> **Minimum mutlak fark**, sıralı dizide **yalnızca yan yana elemanlar** arasında olabilir.

Neden?
- Sıralamadan sonra araya başka sayı giren iki elemanın farkı,
  yan yana olanlardan her zaman **daha büyük veya eşit** olur.

Bu yüzden:
- Tüm `O(n²)` çiftleri denemeye gerek yok 🚀

---

## Algoritma

1. Diziyi sırala
2. Yan yana elemanlar arasındaki farklardan:
   - En küçüğünü (`min_diff`) bul
3. Tekrar yan yana elemanları dolaş:
   - Farkı `min_diff` olan çiftleri listeye ekle

---

## Python Kodu

```python
class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_diff = float('inf')
        result = []

        # Minimum farkı bul
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            min_diff = min(min_diff, diff)

        # Minimum farka sahip çiftleri topla
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_diff:
                result.append([arr[i], arr[i + 1]])

        return result
```

### Örnek
```python
arr = [4,2,1,3]

Sıralı: [1,2,3,4]

Farklar:
2 - 1 = 1
3 - 2 = 1
4 - 3 = 1

Minimum fark = 1

Sonuç:
[[1,2], [2,3], [3,4]]
```

### Karmaşıklık Analizi
- **Zaman**
- - Sıralama: `O(n log n)`
- - Tek geçiş: `O(n)`

- **Alan**
- - `O(1)` (çıktı hariç)