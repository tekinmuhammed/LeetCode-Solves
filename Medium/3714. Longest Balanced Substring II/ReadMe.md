# 3714. Longest Balanced Substring II

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3714](https://leetcode.com/problems/longest-balanced-substring-ii/description/)

---

## Problem Özeti

String `s` yalnızca şu karakterlerden oluşur:

a, b, c

Bir substring **balanced** kabul edilir eğer:

Substring içinde bulunan tüm karakterlerin frekansları eşitse.

Örneğin:

"abcabc"  
a → 2  
b → 2  
c → 2  
✅ balanced

"aaabbbcc"  
a → 3  
b → 3  
c → 2  
❌ balanced değil

Amaç:
En uzun balanced substring uzunluğunu bulmak.

---

# Ana Fikir

Balanced demek:

count(a) = count(b) = count(c)

Bu doğrudan kontrol edilirse O(n²) olur.

Ama bunu şu şekilde dönüştürebiliriz:

count(b) - count(a) = 0  
count(c) - count(a) = 0  

Yani:

Relative differences = 0

Bu artık bir prefix-sum state problemine dönüşür.

---

# Kritik Trick: Mask Kullanımı

Bu çözümün en güçlü kısmı burada 👇

Her balanced substring tüm harfleri içermek zorunda değil.

Örneğin:

"aaa" → sadece a var → balanced  
"abab" → sadece a ve b var → balanced  

Bu yüzden:

Mask 1 → sadece a  
Mask 2 → sadece b  
Mask 3 → a,b  
Mask 7 → a,b,c  

Toplam 1..7 arası tüm kombinasyonlar denenir.

---

# State Tanımı

counts = [count_a, count_b, count_c]

Aktif harfleri seçiyoruz (mask’e göre).

Sonra:

İlk aktif harfi base alıyoruz.

Diğerleri için:

state[k] = count[k] - base

Örneğin:

a = 5  
b = 5  
c = 5  

state = (0, 0)

Balanced olduğunda state hep aynı kalır.

---

# Neden Çalışıyor?

Eğer iki index arasında:

state aynıysa

Bu demektir ki:

Aradaki substring’de
aktif harflerin artış miktarı eşittir.

Yani balanced’tır.

Bu tam olarak:

Prefix difference equal mantığıdır.

---

# "Wall" Mekanizması

Eğer mask dışında bir karakter gelirse:

Bu substring devam edemez.

O yüzden:

counts sıfırlanır  
map resetlenir  

Bu karakter bir duvar (wall) gibi davranır.

---

# Kod

```python
class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0

        # Iterate through masks 1 to 7
        for mask in range(1, 8):

            # State -> first index
            idx_map = {tuple([0] * (bin(mask).count('1') - 1)): -1}
            counts = [0, 0, 0]

            for i, char in enumerate(s):
                val = ord(char) - ord('a')

                # If char not in mask → reset
                if not ((mask >> val) & 1):
                    counts = [0, 0, 0]
                    idx_map = {
                        tuple([0] * (bin(mask).count('1') - 1)): i
                    }
                    continue

                counts[val] += 1

                # Build state
                active_counts = [
                    counts[j] for j in range(3) if (mask >> j) & 1
                ]

                state = []
                if active_counts:
                    base = active_counts[0]
                    for k in range(1, len(active_counts)):
                        state.append(active_counts[k] - base)

                current_state = tuple(state)

                if current_state in idx_map:
                    res = max(res, i - idx_map[current_state])
                else:
                    idx_map[current_state] = i

        return res
```

### Zaman Karmaşıklığı
Mask sayısı = 7 (sabit)
Her mask için:
O(n)
Toplam:
O(7n) = **O(n)**

### Alan Karmaşıklığı
Map en kötü durumda:
**O(n)**
Counts sabit.