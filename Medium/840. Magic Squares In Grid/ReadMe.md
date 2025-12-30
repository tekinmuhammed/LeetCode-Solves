# 840. Magic Squares In Grid

**Difficulty:** Medium  
**Problem Link:** [LeetCode 840](https://leetcode.com/problems/magic-squares-in-grid/description/)

---

## 🧩 Problem Özeti

Bir **3×3 alt grid**, aşağıdaki koşulları sağlıyorsa **magic square** kabul edilir:

1. İçinde **1’den 9’a kadar tüm sayılar tam olarak bir kez** bulunmalı  
2. Her **satır**, **sütun** ve **iki köşegenin** toplamı **eşit** olmalı  

🎯 Amaç:
> Verilen `grid` içinde kaç tane **3×3 magic square** olduğunu bulmak.

---

## 🧠 Temel Gözlem (Önemli!)

📌 **3×3 magic square** için:
- Ortadaki hücre **mutlaka 5** olmalıdır  

Bu sayede:
- Geçersiz adayları **çok hızlı eleyebiliriz** 🚀

---

## 🛠️ Çözüm Stratejisi

- Grid içinde dolaş
- Her `(i, j)` için 3×3 alt kareyi kontrol et
- `isMagic(r, c)` fonksiyonu ile doğrula

---

## 🔍 `isMagic(r, c)` Fonksiyonu

### 1️⃣ Merkez Kontrolü
```python
if grid[r+1][c+1] != 5:
    return False
```
- Magic square değilse direkt elenir ⚡

### 2️⃣ 1–9 Kontrolü
```python
nums = []
for i in range(r, r+3):
    for j in range(c, c+3):
        nums.append(grid[i][j])

if set(nums) != set(range(1, 10)):
    return False
```
✔️ Tüm sayılar:
- 1’den 9’a kadar
- Eksiksiz
- Tekrar yok

### 3️⃣ Hedef Toplamı Belirleme
```python
s = sum(grid[r][c:c+3])
```
- İlk satırın toplamı → referans değer

### 4️⃣ Satır Kontrolleri
```python
for i in range(r, r+3):
    if sum(grid[i][c:c+3]) != s:
        return False
```

### 5️⃣ Sütun Kontrolleri
```python
for j in range(c, c+3):
    if grid[r][j] + grid[r+1][j] + grid[r+2][j] != s:
        return False
```

### 6️⃣ Köşegen Kontrolleri
```python
if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
    return False
if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
    return False
```

### ✅ Hepsi Sağlandıysa
```python
return True
```

### 🔁 Ana Döngü
```python
for i in range(rows - 2):
    for j in range(cols - 2):
        if isMagic(i, j):
            count += 1
```
- Tüm olası 3×3 kareler denenir

### ⏱️ Zaman & Alan Karmaşıklığı
- **⏳ Zaman**
- - Her 3×3 kare `O(1)`
- - Toplam: `O(rows × cols)`

- **🧠 Alan**
- - Sabit ekstra alan → `O(1)`