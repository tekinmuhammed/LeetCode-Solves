# 3606. Coupon Code Validator — Explanation & Analysis

**Difficulty:** Easy  
**Link:** [LeetCode 3606](https://leetcode.com/problems/coupon-code-validator/description/)

## 🧾 Problem Summary
Elimizde üç paralel liste var:

- `code`: Kupon kodları
- `businessLine`: Kuponun ait olduğu iş kolu
- `isActive`: Kuponun aktif olup olmadığı

Amaç: **Geçerli kuponları filtreleyip**, belirli bir sıraya göre **liste halinde döndürmek**.

---

## ✅ Geçerlilik Kuralları
Bir kuponun **geçerli** sayılabilmesi için:

1. `isActive == True` olmalı
2. `code`:
   - Boş olmamalı
   - Sadece **harf, rakam ve `_`** içermeli  
     → Regex: `^[A-Za-z0-9_]+$`
3. `businessLine`, aşağıdaki listede olmalı:
```text
electronics → grocery → pharmacy → restaurant
```

### 🔢 Sıralama Kuralları

Geçerli kuponlar şu önceliklerle sıralanır:

1. **businessLine sırası** (yukarıdaki listeye göre)

2. Aynı businessLine içindekiler için:

- **Lexicographical (alfabetik)** `code` sırası

### 🧠 Solution Strategy
1. **Business Line sırasını sayısallaştırma**
```python
order = {
    "electronics": 0,
    "grocery": 1,
    "pharmacy": 2,
    "restaurant": 3
}
```

Bu sayede kolayca sıralama yapılır.

2. **Regex ile code doğrulama**
```python
pattern = re.compile(r'^[A-Za-z0-9_]+$')
```
- Tüm karakterlerin izinli olup olmadığı kontrol edilir.

3. **Filtreleme**

Her kupon için:

- Aktif mi?

- Kod geçerli mi?

- Business line geçerli mi?

Hepsi sağlanıyorsa:

```python
(order[businessLine], code)
```
şeklinde listeye eklenir.

4. **Sıralama**
```python
valid_coupons.sort(key=lambda x: (x[0], x[1]))
```
- Önce businessLine sırası

- Sonra code alfabetik

### 🧮 Time Complexity
- Filtreleme: **O(n)**

- Sıralama: **O(n log n)**

Toplam: **O(n log n)**

### ✅ Your Code (Clean & Correct)
```python
class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        import re

        valid_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
        order = {name: i for i, name in enumerate(valid_lines)}
        pattern = re.compile(r'^[A-Za-z0-9_]+$')

        valid_coupons = []

        for c, b, a in zip(code, businessLine, isActive):
            if not a:
                continue
            if not c or not pattern.match(c):
                continue
            if b not in order:
                continue
            valid_coupons.append((order[b], c))

        # Sort by businessLine order, then lexicographically by code
        valid_coupons.sort(key=lambda x: (x[0], x[1]))

        return [c for _, c in valid_coupons]
```