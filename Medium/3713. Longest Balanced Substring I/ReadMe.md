# 3713. Longest Balanced Substring I

## Problem Özeti

Bir string `s` veriliyor (küçük harfler).

Bir substring **balanced** kabul edilir eğer:

- Substring içinde bulunan tüm karakterlerin
- Frekansları (kaç kez göründükleri)
- Birbirine eşitse.

Örneğin:

"abab"  
a → 2  
b → 2  
✅ balanced

"aaabb"  
a → 3  
b → 2  
❌ balanced değil

Amaç:
En uzun balanced substring’in uzunluğunu bulmak.

---

# Ana Fikir (Brute Force)

Bu problem “I” versiyonu olduğu için:

O(n²) çözüm yeterli.

Yaklaşım:

1. Her başlangıç index’i `i` için
2. Sağ tarafa doğru substring genişlet
3. Her adımda:
   - 26 uzunluklu frequency array tut
   - min ve max frekansı kontrol et
4. Eğer min_freq == max_freq ise balanced

---

# Kritik Nokta

Burada önemli olan:

Sadece frekansı > 0 olan harfleri kontrol ediyoruz.

Yani:

for f in freq:
if f > 0:
min_freq = min(...)
max_freq = max(...)


Bu olmazsa:

0 frekanslı harfler dengeyi bozar.

---

# Kod

```python
class Solution(object):
    def longestBalanced(self, s):
        n = len(s)
        ans = 0
        
        for i in range(n):
            freq = [0] * 26
            
            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                freq[idx] += 1
                
                min_freq = float('inf')
                max_freq = 0
                
                for f in freq:
                    if f > 0:
                        min_freq = min(min_freq, f)
                        max_freq = max(max_freq, f)
                
                if min_freq == max_freq:
                    ans = max(ans, j - i + 1)
        
        return ans
Örnek
s = "aabbcc"

Substring: "aabbcc"

a → 2
b → 2
c → 2

min_freq = 2
max_freq = 2

✅ Balanced
Length = 6

Zaman Karmaşıklığı
Dış döngü → O(n)

İç döngü → O(n)

26 harf kontrolü → O(1)

Toplam:

O(n²)

Alan Karmaşıklığı
freq array → O(1) (26 sabit)