# 868. Binary Gap

**Difficulty:** Easy  
**Link:** [LeetCode 868](https://leetcode.com/problems/binary-gap/description/)

---

## Problem Özeti

Bir pozitif integer `n` veriliyor.

Görevimiz:

Binary gösteriminde **iki adet `1` arasındaki en büyük mesafeyi** bulmak.

Mesafe:

```
iki 1'in index farkı
```

Eğer yalnızca bir tane `1` varsa veya hiç aralık yoksa sonuç `0`.

---

# Örnekler

### Örnek 1

```
n = 22
```

Binary:

```
10110
```

1'lerin indexleri:

```
0, 2, 3
```

Mesafeler:

```
2 - 0 = 2
3 - 2 = 1
```

Sonuç:

```
2
```

---

### Örnek 2

```
n = 8
```

Binary:

```
1000
```

Sadece bir tane `1` var.

Sonuç:

```
0
```

---

# Çözüm Fikri

1. Sayıyı binary string'e çevir.
2. Son görülen `1` indexini tut.
3. Yeni `1` gördüğünde farkı hesapla.
4. Maksimumu güncelle.

---

# Kod

```python
class Solution(object):
    def binaryGap(self, n):
        b = bin(n)[2:]   # binary string
        last = -1
        max_gap = 0

        for i in range(len(b)):
            if b[i] == '1':
                if last != -1:
                    max_gap = max(max_gap, i - last)
                last = i

        return max_gap
```

---

# Kodun Adım Adım Çalışması

Örnek:

```
n = 22
```

Binary:

```
10110
```

Başlangıç:

```
last = -1
max_gap = 0
```

---

### i = 0

```
1 bulundu
```

```
last = 0
```

---

### i = 1

```
0 → geç
```

---

### i = 2

```
1 bulundu
```

Mesafe:

```
2 - 0 = 2
```

```
max_gap = 2
last = 2
```

---

### i = 3

```
1 bulundu
```

Mesafe:

```
3 - 2 = 1
```

max değişmez.

---

### i = 4

```
0 → geç
```

---

Sonuç:

```
2
```

---

# Zaman Karmaşıklığı

Binary uzunluğu:

```
log₂(n)
```

Bu yüzden:

```
O(log n)
```

---

# Alan Karmaşıklığı

Binary string oluşturulduğu için:

```
O(log n)
```

---

# Daha Optimal Bit Manipulation Versiyonu

String oluşturmadan da yapılabilir:

```python
class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1
        ans = 0
        i = 0

        while n > 0:
            if n & 1:
                if last != -1:
                    ans = max(ans, i - last)
                last = i
            n >>= 1
            i += 1

        return ans
```