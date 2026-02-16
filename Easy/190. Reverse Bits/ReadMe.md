# 190. Reverse Bits

**Difficulty:** Easy  
**Problem Link:** [LeetCode 190](https://leetcode.com/problems/reverse-bits/description/)

---

## Problem Özeti

32 bitlik unsigned integer `n` veriliyor.

**Amaç:**

Bu sayının bitlerini ters çevirip sonucu döndürmek.

Örneğin:

Input:
00000010100101000001111010011100

Output:
00111001011110000010100101000000

Yani:

En sağdaki bit → en sola  
En soldaki bit → en sağa  

---

# Ana Fikir

Binary seviyesinde düşünelim:

Her adımda:

- `n`'in en sağdaki bitini al
- `result`'i sola kaydır
- o biti `result`'e ekle
- `n`'i sağa kaydır

Bu işlemi 32 kez yaparsak,
tüm bitler ters sırayla `result`’e yerleşmiş olur.

---

# Kod

```python
class Solution(object):
    def reverseBits(self, n):
        result = 0
        
        for _ in range(32):
            result <<= 1        # result'i sola kaydır
            result |= (n & 1)   # n'in en sağ bitini ekle
            n >>= 1             # n'i sağa kaydır
        
        return result
```

---

# Adım Adım Mantık

Diyelim:

n = 1011  (4-bit örnek)

İterasyonlar:

1️⃣ result = 0  
   bit = 1  
   result = 1  

2️⃣ result = 10  
   bit = 1  
   result = 11  

3️⃣ result = 110  
   bit = 0  
   result = 110  

4️⃣ result = 1100  
   bit = 1  
   result = 1101  

Sonuç:

1101

Yani terslenmiş hali.

---

# Bit Operasyonları Açıklaması

- `n & 1`
  → en sağdaki biti alır

- `n >> 1`
  → n’i sağa kaydırır

- `result << 1`
  → result’i sola kaydırır

- `result |= bit`
  → son biti ekler

---

# Zaman Karmaşıklığı

32 iterasyon:

O(1)

(Sabit süre)

---

# Alan Karmaşıklığı

O(1)