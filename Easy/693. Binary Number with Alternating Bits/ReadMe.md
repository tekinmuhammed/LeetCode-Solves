# 693. Binary Number with Alternating Bits

**Difficulty:** Easy  
**Problem Link:** [LeetCode 693](https://leetcode.com/problems/binary-number-with-alternating-bits/description/)

---

## Problem Özeti

Bir pozitif tam sayı `n` veriliyor.

Amaç:

Binary gösterimindeki bitlerin
ardışık olarak birbirinden farklı olup olmadığını kontrol etmek.

Yani:

- 101010 ✅
- 010101 ✅
- 111000 ❌
- 1001 ❌

---

## Ana Fikir (Bit Manipülasyonu)

Alternating bit yapısında şu özellik vardır:

Eğer `n` alternating ise:

```
n ^ (n >> 1)
```

sonucu **tüm bitleri 1 olan bir sayı** olur.

---

## Neden Çalışıyor?

Örnek:

n = 5

Binary:
101

Sağa kaydır:
010

XOR:
101
010
---
111

Gördüğün gibi tüm bitler 1 oldu.

Alternating olmayan örnek:

n = 7
111

Sağa kaydır:
011

XOR:
111
011
---
100   ❌ (Tüm bitler 1 değil)

---

## Tüm Bitlerin 1 Olduğunu Nasıl Anlarız?

Eğer bir sayı şu formdaysa:

```
111...111
```

O zaman:

```
x & (x + 1) == 0
```

Çünkü:

Örnek:

x = 111 (7)
x+1 = 1000 (8)

0111
1000
----
0000

Sonuç 0 olur.

---

## Kod

```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """
        Bit Manipülasyonu Yöntemi (O(1) Karmaşıklık)
        """
        # 1. XOR ile dönüşümlülük testi
        x = n ^ (n >> 1)
        
        # 2. x tüm bitleri 1 mi?
        return (x & (x + 1)) == 0
```

---

## Zaman Karmaşıklığı

Bit işlemleri sabit sürelidir.

O(1)

---

## Alan Karmaşıklığı

O(1)

---

## Alternatif (String Yöntemi)

Daha basit ama daha yavaş:

```python
def hasAlternatingBits(self, n: int) -> bool:
    bits = bin(n)
    return "00" not in bits and "11" not in bits
```