# 955. Delete Columns to Make Sorted II

**Difficulty:** Medium
**Problem Link:** [LeetCode 955](https://leetcode.com/problems/delete-columns-to-make-sorted-ii/description/)

---

## 🧩 Problem Özeti

- Elimizde **aynı uzunlukta stringlerden oluşan bir liste (`strs`)** var.
- Amacımız:  
  **Bazı sütunları (column) silerek**, string listesini **lexicographically (sözlük sırası)** olacak şekilde sıralı hale getirmek.
- Silinen sütun sayısı **minimum** olmalı.
- Sütun silme işlemi **tüm stringlerde aynı anda** yapılır.

---

## 🧠 Temel Fikir (Greedy + Durum Takibi)

Bu problemde kritik fark şudur:

> Önceki sütunlarda zaten sıralandığı **kesinleşmiş** olan string çiftlerini
> tekrar kontrol etmemize gerek yok.

Bu yüzden:
- Komşu string çiftleri için  
  **“artık kesin sıralı mı?”** bilgisini tutarız.

---

## 🔧 Kullanılan Yapılar

### `sorted_pairs`
```python
sorted_pairs = [False] * (n - 1)
```
- `sorted_pairs[i] = True`
- - → `strs[i] < strs[i+1]` olduğu kesinleşti

- `False` ise hâlâ eşit olabilir, ileride bozulabilir

# 🚶‍♂️ Algoritmanın Akışı
**1️⃣ Sütun Sütun İlerleme**
```python
for col in range(m):
```
- Her sütunu soldan sağa inceliyoruz.

**2️⃣ Bu Sütun Sıralamayı Bozuyor mu?**
```python
bad = False
for i in range(n - 1):
    if not sorted_pairs[i] and strs[i][col] > strs[i + 1][col]:
        bad = True
        break
```
📌 Mantık:
- Eğer **henüz sıralı olmadığı kesinleşmemiş** bir çiftte
- `üstteki > alttaki` olursa
- - ➡️ **Bu sütun kesinlikle silinmeli**

**3️⃣ Bozuksa: Sütunu Sil**
```python
if bad:
    deletions += 1
    continue
```
- Bu sütun **hiçbir bilgi kazandırmaz**
- `sorted_pairs` güncellenmez
- Bir sonraki sütuna geçilir

**4️⃣ Bozuk Değilse: Yeni Sıralanan Çiftleri İşaretle**
```python
for i in range(n - 1):
    if not sorted_pairs[i] and strs[i][col] < strs[i + 1][col]:
        sorted_pairs[i] = True
```
📌 Eğer:
- Daha önce eşit olabilir dediğimiz bir çift
- Bu sütunda `<` ilişkisi kurduysa
- - ➡️ Artık **kesin sıralı**

**5️⃣ Erken Çıkış (Optimization)**
```python
if all(sorted_pairs):
    break
```
- Tüm komşu çiftler kesin sıralandıysa
- Artık hiçbir sütun silemez → **erken bitir**

### ⏱️ Zaman & Alan Karmaşıklığı
- **Zaman:** `O(n * m)`
- - `n`: string sayısı
- - `m`: string uzunluğu
- **Alan:** `O(n)`
- - `sorted_pairs` dizisi

### 🧠 Küçük Örnek
```python
strs = ["ca","bb","ac"]
```
- 1. sütun: `c > b` ❌ → sil

- 2. sütun: `a < b < c` ✅ → sıralı

**➡️ Cevap: 1**