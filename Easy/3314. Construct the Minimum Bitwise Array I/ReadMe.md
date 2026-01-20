# 🧩 3314. Construct the Minimum Bitwise Array I

**Difficulty:** Easy  
**Problem Link:** [LeetCode 3314](https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/description/)

---

## 🔍 Problem Özeti
- Bir `nums` dizisi veriliyor.
- Her `nums[i]` için, aşağıdaki şartı sağlayan **en küçük** `ans[i]` bulunmalı:

```python
ans[i] OR (ans[i] + 1) == nums[i]
```
- Eğer böyle bir sayı yoksa, `-1` döndürülmeli.

### 🧠 Temel Gözlem
**🔴 Özel Durum:** `x = 2`
- `2 = 10 (binary)`
- Hiçbir `a` için:
```python
a | (a + 1) = 2
```
olamaz.
**➡️ Sonuç:** `x == 2` → `-1`

### 🔎 Genel Mantık (x ≠ 2)

> LeetCode testlerine göre `nums[i]` değerleri **asal** (prime) sayılardır.

- 2 hariç tüm asal sayılar **tektir**
- Binary gösterimleri mutlaka **1 ile biter**
**Örnek:**
```python
x = 11 → 1011
x = 7  → 0111
```

### 💡 Kritik Bitwise Fikir
**Amaç:**
```python
a | (a + 1) = x
```
Bu eşitliği sağlamak için:
- `a` ve `a+1` sadece **sondaki 1 bloğunda** farklı olmalı
- `x`’in **en sağdaki 1 bloğunu kontrollü biçimde küçültmeliyiz**

### 🛠️ Adım Adım Çözüm
1️⃣ `x + 1` **Hesapla**
- Sondaki tüm `1`’ler `0` olur
- Bir üst bitten `1` taşar
```python
x = 11 (1011)
x+1 = 12 (1100)
```

**2️⃣ En Sağdaki 1 Bit’i Bul (Lowbit)**
```python
lowbit = (x + 1) & -(x + 1)
```
Bu:
- `(x + 1)`’deki **en küçük 2^k** değerini verir
**Örnek:**
```python
12 (1100) → lowbit = 4 (100)
```

**3️⃣ Cevabı Hesapla**
```python
ans = x - (lowbit / 2)
```
**Örnek:**
```python
x = 11
lowbit = 4
ans = 11 - 2 = 9
```
**Kontrol:**
```python
9 | 10 = 1011 = 11 ✅
```

### ✅ Kodun Mantığı
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

### ⏱️ Zaman & Alan Karmaşıklığı
- **Zaman**
```python
O(n)
```
- - Her sayı için sabit bit işlemleri

- **Alan**
```python
O(1) (çıktı hariç)
```