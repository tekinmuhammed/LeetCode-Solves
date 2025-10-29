# 🧮 LeetCode 3370 — Smallest Number With All Set Bits

**Difficulty:** Easy
**Link:** [LeetCode 3370](https://leetcode.com/problems/smallest-number-with-all-set-bits/description/)

## 📘 Problem Tanımı  
Bir **pozitif tam sayı `n`** veriliyor. Görev, **bütün bitleri 1 olan** ve **`n`’den büyük veya eşit** olan **en küçük sayıyı** bulmaktır.  

Başka bir deyişle, `n`'den küçük olmayan ve binary (ikili) gösteriminde **sadece 1’lerden** oluşan en küçük sayıyı döndürmeliyiz.  

---

## 💡 Örnek

```python
Input: n = 10
Output: 15
```

**Açıklama:**

- `10`’un binary karşılığı: `1010`

- `15`’in binary karşılığı: `1111`

- `15`, hem `10`’dan büyük hem de tüm bitleri 1 olan en küçük sayıdır.

### 🧠 Çözüm Mantığı

Bu problemde:

- Sadece `1` bitlerinden oluşan sayılar `1, 3, 7, 15, 31, 63, ...` şeklindedir.

- Bu sayıların genel formülü:

    **(1<<𝑘)−1**

    Burada `k`, bit uzunluğunu temsil eder.

**Adımlar:**

1. `k = 1` ile başla.

2. `(1 << k) - 1 < n` olduğu sürece `k`’yi artır.

3. Döngü bittiğinde `(1 << k) - 1` değeri, tüm bitleri 1 olan ve `n`’den büyük veya eşit olan en küçük sayıdır.

### 🧩 Kod
```python
class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 1
        while (1 << k) - 1 < n:
            k += 1
        return (1 << k) - 1
```

### ⚙️ Çalışma Örneği
**Örnek 1:**
```python
Input: n = 10
Çalışma:
k=1 → (1<<1)-1 = 1
k=2 → 3
k=3 → 7
k=4 → 15 (>=10)

Output: 15
```

**Örnek 2:**
```python
Input: n = 5
k=1 → 1
k=2 → 3
k=3 → 7 (>=5)

Output: 7
```

### ⏱️ Zaman ve Bellek Karmaşıklığı
- **Zaman Karmaşıklığı:** `O(log n)`
    (Çünkü her iterasyonda `k` sadece birer birer artıyor.)

- **Bellek Karmaşıklığı:** `O(1)`

### 🧾 Özet
| Özellik          | Açıklama              |
| ---------------- | --------------------- |
| **Problem Türü** | Bit Manipülasyonu     |
| **Zorluk**       | 🟩 Easy               |
| **Kavramlar**    | Binary, Bitwise Shift |
| **Formül**       | `(1 << k) - 1`        |
