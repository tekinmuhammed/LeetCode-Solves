# 67. Add Binary

**Difficulty:** Easy  
**Problem Link:** [LeetCode 67](https://leetcode.com/problems/add-binary/description/)

---

## Problem Özeti

İki binary string veriliyor:
```python
a  
b  
```
Amaç:

Bu iki binary sayıyı toplayıp sonucu yine binary string olarak döndürmek.

---

## Ana Fikir

Bu problem aslında:

👉 Elle binary toplama işleminin simülasyonu.

Sağdan sola doğru:

- İki biti topla
- Carry ekle
- Sonucu yaz
- Yeni carry hesapla

---

## Adım Adım Mantık

1️⃣ İki pointer kullan:

i → a'nın sonundan başlar  
j → b'nin sonundan başlar  

2️⃣ carry başlangıçta 0

3️⃣ Döngü şu şartla devam eder:

- i >= 0
- j >= 0
- carry varsa

4️⃣ Her adımda:
```python
total = carry
```
a[i] (varsa)

b[j] (varsa)


5️⃣ Yeni bit:
```python
total % 2
```

6️⃣ Yeni carry:
```python
total // 2
```

---

## Kod

```python
class Solution(object):
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return ''.join(reversed(result))
```

### Örnek
```python
a = "1010"
b = "1011"
```
Toplama:

   1010
+  1011
-------
  10101
Sonuç:
```python
"10101"
```

### Zaman Karmaşıklığı
- En fazla:
- - max(len(a), len(b))
- - **O(n)**

### Alan Karmaşıklığı
- Result listesi:
- - **O(n)**