# 2110. Number of Smooth Descent Periods of a Stock

**Difficulty:** Medium
**Problem Link:** [LeetCode 2110](https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/description/)

## 🧩 Problem Summary
Bir hisse senedinin günlük fiyatları `prices` dizisiyle veriliyor.

Bir **smooth descent period** şu şekilde tanımlanır:
- Ardışık günlerde fiyat **her gün tam olarak 1 azalmalı**
- Tek bir gün de **geçerli bir descent period** sayılır

👉 Amaç: Tüm **smooth descent period** sayısını bulmak.

---

## 🧠 Temel Gözlem
Her gün:
- En az **1** tane descent period vardır (kendisi)
- Eğer bir önceki güne göre fiyat **tam 1 azalmışsa**,  
  önceki descent dizisini **uzatabiliriz**

Bu yüzden:
- Ardışık düzgün inişin uzunluğunu takip etmek yeterlidir.

---

## 🧮 Değişkenlerin Anlamı

```python
total   # Şu ana kadar bulunan tüm smooth descent period sayısı
length  # Mevcut günde biten smooth descent dizisinin uzunluğu
```

### 🔁 Algoritma Adımları
1. İlk gün:

- `length = 1`

- `total = 1`

2. Her yeni gün için:

- Eğer `prices[i-1] - prices[i] == 1` ise
→ düzgün iniş devam ediyor → `length += 1`

- Aksi halde
→ yeni bir iniş başlar → `length = 1`

3. Her adımda:

- `total += length`

### 🧪 Küçük Örnek
```python
prices = [3, 2, 1, 4]
```
| Gün | Fiyat | length | total |
| --- | ----- | ------ | ----- |
| 0   | 3     | 1      | 1     |
| 1   | 2     | 2      | 3     |
| 2   | 1     | 3      | 6     |
| 3   | 4     | 1      | 7     |

- **📌 Sonuç: `7`**

### ✅ Kodunun Doğruluğu
```python
class Solution(object):
    def getDescentPeriods(self, prices):
        total = 1        # at least one period (first day)
        length = 1       # current smooth descent length

        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                length += 1
            else:
                length = 1
            total += length

        return total
```

- ✔️ Zaman karmaşıklığı: `O(n)`
- ✔️ Alan karmaşıklığı: `O(1)`
- ✔️ Optimal ve sade çözüm
- ✔️ LeetCode editorial ile birebir uyumlu