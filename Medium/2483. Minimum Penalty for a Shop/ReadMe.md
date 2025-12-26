# 2483. Minimum Penalty for a Shop

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2483](https://leetcode.com/problems/minimum-penalty-for-a-shop/description/)

---

## 🧩 Problem Özeti

Bir dükkanın **kapanış saatini** seçiyoruz.

- `customers[i] == 'Y'` → o saatte müşteri var
- `customers[i] == 'N'` → o saatte müşteri yok

### Ceza Kuralları
- **Açıkken gelen `N`** → ceza +1  
- **Kapalıyken gelen `Y`** → ceza +1  

Amaç:
> **Toplam cezayı minimize eden kapanış saatini** bulmak.

⏰ Kapanış saati `j` seçilirse:
- `[0, j)` → dükkan açık
- `[j, n)` → dükkan kapalı

---

## 🧠 Temel Fikir

Her olası kapanış saati `j` için cezayı **O(1)** zamanda hesaplamak.

Ceza iki parçadan oluşur:

1. **Açıkken gelen `N` sayısı**
2. **Kapalıyken gelen `Y` sayısı**

---

## 🔍 Kodunun Adım Adım Açıklaması

---

### 1️⃣ Suffix `Y` Dizisi

```python
suffix_Y[i] = i'den sona kadar kaç tane 'Y' var
```
```python
suffix_Y = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    suffix_Y[i] = suffix_Y[i + 1] + (1 if customers[i] == 'Y' else 0)
```
📌 Bu sayede:
- `suffix_Y[j]` → kapalıyken gelen müşteri cezası

### 2️⃣ Değişkenler
```python
min_penalty = float('inf')
best_hour = 0
open_N = 0
```
- `open_N` → dükkan açıkken gelen `N` sayısı
- `best_hour` → en iyi kapanış saati

### 3️⃣ Tüm Kapanış Saatlerini Dene
```python
for j in range(n + 1):
```
Her `j` için:

### 🔹 Ceza Hesabı
```python
penalty = open_N + suffix_Y[j]
```
- `open_N` → açıkken gelen boş saatler
- `suffix_Y[j]` → kapalıyken gelen müşteriler

### 🔹 Minimumu Güncelle
```python
if penalty < min_penalty:
    min_penalty = penalty
    best_hour = j
```
📌 Eşitlikte **ilk gelen saat** seçilir → problem kuralına uygun ✔️

### 🔹 Bir Sonraki Saat İçin Güncelle
```python
if j < n and customers[j] == 'N':
    open_N += 1
```

### 🧪 Örnek
```python
customers = "YYNY"
```
| Kapanış Saati | Açık N | Kapalı Y | Toplam Ceza |
| ------------- | ------ | -------- | ----------- |
| 0             | 0      | 3        | 3           |
| 1             | 0      | 2        | 2           |
| 2             | 0      | 1        | 1           |
| 3             | 1      | 1        | 2           |
| 4             | 1      | 0        | 1           |

➡️ **En küçük ceza = 1**, ilk görüldüğü saat **2**

### ⏱️ Zaman & Alan Karmaşıklığı
- **Zaman:** `O(n)`
- **Alan:** `O(n)` (suffix dizisi)

