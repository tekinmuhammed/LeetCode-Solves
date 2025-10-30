# 🔢 LeetCode 1526 — Minimum Number of Increments on Subarrays to Form a Target Array

**Difficulty:** Hard  
**Problem Link:** [LeetCode 1526](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/description/)

## 📘 Problem Tanımı  
Bir **hedef dizi (`target`)** veriliyor. Başlangıçta tüm elemanları **0** olan bir dizi üzerinde, **alt diziler (subarray)** seçip bu alt dizinin her elemanını **1 artırabiliyoruz**.  
Amaç, verilen işlemlerle **`target` dizisini oluşturmak** için gereken **minimum işlem sayısını** bulmaktır.

---

## 💡 Örnek

```python
Input: target = [1,2,3,2,1]
Output: 3
```

### Açıklama:

1. `[0,0,0,0,0]` → `[1,1,1,1,1]` (tüm elemanları 1 artır)

2. `[1,1,1,1,1]` → `[1,2,2,2,1]` (2–4 arası artır)

3. `[1,2,2,2,1]` → `[1,2,3,2,1]` (3. eleman artır)

    Toplam 3 işlem gerekir.

## 🧠 Çözüm Mantığı

Her bir eleman `target[i]`, önceki elemana göre ne kadar fazla ise o kadar ek işlem gerekir.

**Ana fikir:**

- İlk eleman (`target[0]`) için doğrudan `target[0]` kadar artırma gerekir.

- Sonraki her eleman için:

- - Eğer `target[i] > target[i-1]` ise, aradaki fark kadar yeni işlem yapılmalıdır.

- - Eğer `target[i] <= target[i-1]` ise, ek bir işlem gerekmez (çünkü daha küçük veya eşit bir değere dönmek, ekstra artırma gerektirmez).

    Bu şekilde, yalnızca artışları toplamak yeterlidir.

### Formül:    **ans=𝑡𝑎𝑟𝑔𝑒𝑡[0]+∑𝑖=1𝑛−1max⁡(0,𝑡𝑎𝑟𝑔𝑒𝑡[𝑖]−𝑡𝑎𝑟𝑔𝑒𝑡[𝑖−1])**

### 🧩 Kod
```python
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        ans = target[0]
        for i in range(1, n):
            ans += max(target[i] - target[i - 1], 0)
        return ans
```

### ⚙️ Çalışma Örneği
**Örnek 1**
```python
Input: target = [1,2,3,2,1]
İşlem adımları:
target[0] = 1 → ans = 1
target[1] - target[0] = 1 → +1 → ans = 2
target[2] - target[1] = 1 → +1 → ans = 3
target[3] - target[2] = -1 → +0 → ans = 3
target[4] - target[3] = -1 → +0 → ans = 3
Output: 3
```

**Örnek 2**
```python
Input: target = [3,1,5,4,2]
ans = 3 (ilk eleman)
+0 (1-3)
+4 (5-1)
+0 (4-5)
+0 (2-4)
Output: 7
```

### ⏱️ Zaman ve Bellek Karmaşıklığı
| Tür        | Karmaşıklık |
| ---------- | ----------- |
| **Zaman**  | O(n)        |
| **Bellek** | O(1)        |

### 🧾 Özet
| Özellik          | Açıklama                                              |
| ---------------- | ----------------------------------------------------- |
| **Problem Türü** | Dizi, Greedy                                          |
| **Zorluk**       | 🟧 Medium                                             |
| **Temel Fikir**  | Sadece artışları toplamak                             |
| **Formül**       | `ans = target[0] + Σ max(0, target[i] - target[i-1])` |
