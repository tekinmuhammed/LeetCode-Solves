## 3315. Construct the Minimum Bitwise Array II

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3243](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i)

---

### Problem Özeti

Her `nums[i] = x` için, aşağıdaki koşulu sağlayan **en küçük** `a` değerini bul:

a OR (a + 1) = x

Eğer böyle bir değer yoksa sonuç `-1` olmalı.

---

### Temel Gözlemler

- `x = 2` için çözüm yoktur.
  - 2 = `10` (binary) → koşulu sağlayan hiçbir `a` yok
- Problemdeki sayılar asal olduğu için:
  - `2` hariç tüm sayılar **tek** sayıdır
- Tek sayıların binary gösterimi:
  - En az bir adet `1` ile biter  
    Örnek: `23 = 10111`

Amaç:
> `x`’in sondaki `1` bloğunun **en soldaki 1’ini 0 yapan** en küçük sayıyı bulmak.

---

### Bitwise Mantık

1. `x + 1` yapılır  
   - Sondaki tüm `1`’ler `0` olur
   - Bir solundaki `0` → `1`

   Örnek:
   ```python
    23 (10111) → 24 (11000)
    ```

2. En sağdaki `1` biti (lowbit) bulunur:
```python
lowbit = (x + 1) & -(x + 1)
```

3. `lowbit / 2` değeri `x`’ten çıkarılır:
```python
23 - (8 >> 1) = 19
```

4. Kontrol:
```python
19 | 20 = 23 ✅
```

---

### Python Kodu

```python
class Solution:
 def minBitwiseArray(self, nums: list[int]) -> list[int]:
     ans = []
     for x in nums:
         if x == 2:
             ans.append(-1)
         else:
             next_val = x + 1
             lowbit = next_val & -next_val
             ans.append(x - (lowbit >> 1))
     return ans
```

### Zaman ve Alan Karmaşıklığı
- **Zaman:** `O(n)`

- **Alan:** `O(1)` (çıktı hariç)