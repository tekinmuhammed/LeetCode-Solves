# 3304. Find the K-th Character in String Game I — Explanation & Analysis

**Difficulty:** Easy  
**Problem Link:** [LeetCode 3304](https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description/)

## ✔️ Problem Summary
Başlangıç kelimesi:

`word = "a"`

Her turda kelime şu şekilde güncelleniyor:
- `word + next(word)`
- Burada `next(word)`: her karakterin 1 ileri harfi  
  - `a → b`, `b → c`, ... `z → {` (ama sınırlar problem gereği aşılmaz)

**Örnek:**
```python
a
a b
ab bc → abb c
```

Senin görevin: **oluşan teorik olarak çok uzun kelimenin k. karakterini bulmak**.

---

## 💡 Naive Approach (Senin Kodun)
Aşağıdaki mantık çalışır **ama** `word` her adımda ikiye katlandığı için,  
k büyük olduğunda **zaman ve bellek açısından çok pahalı** olur:

```python
class Solution(object):
    def kthCharacter(self, k):
        word = "a"
        
        while len(word) < k:
            new_part = ''.join(chr(ord(c) + 1) for c in word)
            word += new_part
        
        return word[k - 1]
```

### ✨ Mantığın Detaylı Analizi (Markdown Formatında)
#### 🔍 Gözlem

**Her iterasyonda:**
```python
S(n+1) = S(n) + next(S(n))
```

**Bu nedenle:**

- 1. iterasyon: 1 karakter

- 2. iterasyon: 2 karakter

- 3. iterasyon: 4 karakter

- 4. iterasyon: 8 karakter

- ...

- n. iterasyon: `2^(n-1)` karakter

- Prefix uzunlukları: 1, 2, 4, 8, 16, ...

Yani **k. karakterin hangi iterasyonda oluştuğu logaritmik bir şekilde bulunabilir**.

### 📌 Kural

Eğer `k` bir önceki uzunluğun içinde kalıyorsa, karakter değişmez.
Eğer yeni eklenen bölümdeyse, karakter bir harf büyümüştür.

### ⏱️ Complexity
| Amaç      | Değer    |
| --------- | -------- |
| **Time**  | O(log k) |
| **Space** | O(1)     |


### 🧠 Özet

- Naive yaklaşım doğru ama gereksizce uzun string üretir.

- Optimal çözüm `k` değerine göre geri sararak hangi karakter olduğunu bulur.

- String oluşturmaya gerek kalmaz.