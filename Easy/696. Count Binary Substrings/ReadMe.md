# 696. Count Binary Substrings

**Difficulty:** Easy  
**Link:** [LeetCode 696](https://leetcode.com/problems/count-binary-substrings/description/)

---

## Problem Özeti

Binary bir string `s` veriliyor.

Amaç:

- İçinde eşit sayıda `0` ve `1` bulunan
- Ve tüm `0`'ların ve `1`'lerin blok halinde olduğu

alt string'lerin sayısını bulmak.

---

## Geçerli Alt String Örnekleri

```
"0011"  ✅
"01"    ✅
"1100"  ✅
```

Geçersiz:

```
"0101"  ❌ (blok yapısı yok)
"00101" ❌
```

---

# Kritik Gözlem

Önemli olan şey:

Ardışık karakter gruplarının uzunluklarıdır.

Örneğin:

s = "001110011"

Gruplar:

00 → 2  
111 → 3  
00 → 2  
11 → 2  

Yani grup uzunlukları:

[2, 3, 2, 2]

Her komşu iki grup için:

```
min(grup1, grup2)
```

kadar geçerli substring üretilebilir.

---

# Neden `min(prev, curr)`?

Örneğin:

"000111"

3 tane 0  
3 tane 1  

Oluşabilecek substringler:

"01"  
"0011"  
"000111"

Toplam: min(3, 3) = 3

---

# Kod Analizi

```python
class Solution(object):
    def countBinarySubstrings(self, s):
        prev = 0      # bir önceki grubun uzunluğu
        curr = 1      # mevcut grubun uzunluğu
        result = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                result += min(prev, curr)
                prev = curr
                curr = 1

        result += min(prev, curr)
        return result
```

---

# Nasıl Çalışıyor?

- `curr` → şu anki karakter grubunun uzunluğu
- `prev` → bir önceki grubun uzunluğu
- Grup değiştiğinde:
  - `result += min(prev, curr)`
  - `prev = curr`
  - `curr = 1`

En sonda da son grubu eklemeyi unutmuyoruz.

---

# Örnek

s = "00110011"

Gruplar:

2, 2, 2, 2

Hesap:

min(0,2) → 0  
min(2,2) → 2  
min(2,2) → 2  
min(2,2) → 2  

Toplam: 6

---

# Zaman Karmaşıklığı

Tek geçiş:

**O(n)**

---

# Alan Karmaşıklığı

Sadece 3 değişken:

**O(1)**
