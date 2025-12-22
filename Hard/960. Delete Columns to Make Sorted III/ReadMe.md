# 960. Delete Columns to Make Sorted III

**Difficulty:** Hard  
**Problem Link:** [LeetCode 960](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/description/)

---

## 🧩 Problem Özeti

- Elimizde **aynı uzunlukta stringlerden oluşan bir liste (`strs`)** var.
- Sütunları (column) silebiliriz.
- Amaç:  
  Kalan sütunlarla oluşturulan stringlerin **lexicographically sıralı** olması.
- **En az kaç sütun silmeliyiz?**

> 🔴 Önceki II sorusundan farkı:  
> Burada **sütunları sırayla inceleyip anında silme** yetmez.  
> Daha genel bir optimizasyon gerekir.

---

## 🧠 Temel Fikir (Longest Increasing Subsequence – LIS)

Bu problem aslında şuna indirgenir:

> **Tüm satırlarda bozulmadan artan sütunların en uzun alt dizisini bul.**

- Ne kadar çok sütunu **koruyabilirsek**
- O kadar az sütun **silmiş oluruz**

---

## 🔁 Dinamik Programlama Tanımı

### `dp[j]` Nedir?

```python
dp[j] = j. sütun SON seçilen sütun olacak şekilde
        tutulabilecek maksimum sütun sayısı
```
Başlangıç:
```python
dp = [1] * m
```
Her sütun **tek başına** tutulabilir.

**🔄 Geçiş Mantığı (i → j)**
```python
for j in range(m):
    for i in range(j):
```
Önceki bir sütundan (`i`), sonraki bir sütuna (`j`) geçebilir miyiz?

**Geçiş Şartı (En Önemli Kısım)**
```python
valid = True
for r in range(n):
    if strs[r][i] > strs[r][j]:
        valid = False
        break
```
**📌 i → j geçişi geçerli mi?**
- **TÜM satırlar için**
- `strs[r][i] <= strs[r][j]` olmalı
> Tek bir satır bile bozuyorsa, bu iki sütun birlikte tutulamaz ❌

**✅ Geçiş Geçerliyse DP Güncelle**
```python
if valid:
    dp[j] = max(dp[j], dp[i] + 1)
```
Yani:
- `i` ile biten en iyi dizinin sonuna `j` eklenebilir

### 🏁 Sonuç Hesabı
**Tutulabilecek Maksimum Sütun**
```python
keep = max(dp)
```

**Silinmesi Gereken Minimum Sütun**
```python
return m - keep
```

### ⏱️ Zaman & Alan Karmaşıklığı

- **Zaman:** `O(m² * n)`
- - `m`: sütun sayısı
- - `n`: satır sayısı

- **Alan:** `O(m)` → DP dizisi

### 🧪 Küçük Örnek
```python
strs = ["babca","bbazb"]
```
Sütunlar:
```python
b b a c a
b b a z b
```
- En uzun geçerli sütun dizisi: `b b a z`
- Uzunluk = 4
- Toplam sütun = 5

**➡️ Cevap: 1 sütun silinir**