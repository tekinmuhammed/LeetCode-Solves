# 🔐 LeetCode 1404. Number of Steps to Reduce a Number in Binary Representation to One

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1404](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/)

---

## Problem Özeti

Binary (ikili) gösterimi verilen bir sayı `s` var.

Amaç:

Bu sayıyı **1’e düşürmek** için gereken **minimum adım sayısını** bulmak.

Kurallar:

- Eğer sayı **çiftse** → `2`’ye böl
- Eğer sayı **tekse** → `1` ekle

İşlemler **binary string üzerinde** düşünülmelidir, sayıyı doğrudan integer’a çevirmeden çözüm beklenir.

---

## Temel Gözlem

Binary sayıyı **sağdan sola** (LSB → MSB) incelersek:

- `0` → çift sayı → sadece **bölme**
- `1` → tek sayı → **1 ekle + böl** (2 adım)

Ancak burada kritik nokta **carry (elde)** yönetimidir.

---

## Neden Carry Gerekli?

Örnek:

```
s = "111"
```

Sağdan:

- 1 → tek → +1 → 10 → carry = 1
- Sonraki bit: 1 + carry = 2 → çift
- carry etkisi yukarı taşınır

Yani binary toplama simülasyonu yapıyoruz.

---

## Algoritma Fikri

1. `steps` → toplam adım sayısı
2. `carry` → elde (0 veya 1)
3. Binary string’i **sağdan sola**, ama **en soldaki bit hariç** tara
4. Her bit için:
   - `current_bit = bit + carry`
   - Eğer `current_bit == 1`:
     - Tek sayı → `+1` ve `/2` → **2 adım**
     - `carry = 1`
   - Aksi halde (`0` veya `2`):
     - Çift sayı → sadece `/2` → **1 adım**
5. Döngü bitince:
   - Eğer `carry == 1` ise → **1 ek adım**

---

## Kod

```python
class Solution(object):
    def numSteps(self, s):
        steps = 0
        carry = 0
        
        # Sağdan sola, en soldaki bit hariç
        for i in range(len(s) - 1, 0, -1):
            current_bit = int(s[i]) + carry
            
            if current_bit == 1:
                # Tek → +1 ve /2
                steps += 2
                carry = 1
            else:
                # Çift → /2
                steps += 1
        
        # En soldaki bit için carry kontrolü
        return steps + carry
```

---

## Örnek Üzerinden Anlayalım

```
s = "1101"
```

Adımlar:

| Bit | Carry | current | İşlem | Steps |
|----|------|---------|-------|-------|
| 1 | 0 | 1 | +1,/2 | +2 |
| 0 | 1 | 1 | +1,/2 | +2 |
| 1 | 1 | 2 | /2 | +1 |
| MSB | 1 | — | /2 | +1 |

Toplam: **6**

---

## Zaman Karmaşıklığı

```
O(n)
```

- `n` = binary string uzunluğu
- Tek geçiş

---

## Alan Karmaşıklığı

```
O(1)
```

- Sadece sabit değişkenler kullanılır