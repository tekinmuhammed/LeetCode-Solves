# 1351. Count Negative Numbers in a Sorted Matrix

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1351](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/)

---

## 🧩 Problem Özeti

- `grid` adlı bir matris veriliyor
- Her **satır soldan sağa**, her **sütun yukarıdan aşağıya** **azalan sırada** (non-increasing) sıralı
- Amaç:
> Matris içindeki **negatif sayıların toplam sayısını** bulmak

---

## 🧠 Temel Gözlem

Matris sıralı olduğu için:

- Bir hücre **negatifse**, onun **sağındaki tüm hücreler de negatiftir**
- Bir hücre **negatif değilse**, onun **üstündeki hücreler de negatif değildir**

Bu sayede tek tek tüm hücreleri gezmek zorunda kalmayız 🚀

---

## 🔍 Senin Çözümünün Fikri (Bottom-Left Yöntemi)

- **Sol alt köşeden** başlıyorsun
- İki yönlü ilerliyorsun:
  - **Negatifse → yukarı çık**
  - **Negatif değilse → sağa git**

Bu klasik ve optimal bir yaklaşım 👍

---

## 🧪 Kodun Adım Adım Açıklaması

### 1️⃣ Başlangıç

```python
m, n = len(grid), len(grid[0])
row, col = m - 1, 0
count = 0
```
- `row = m - 1` → en alt satır
- `col = 0` → en sol sütun
- `count` → negatif sayı adedi

### 2️⃣ Matris İçinde Gez
```python
while row >= 0 and col < n:
```
Matris sınırları içinde kaldığın sürece devam

### 3️⃣ Negatif Sayı Bulunursa
```python
if grid[row][col] < 0:
    count += (n - col)
    row -= 1
```
📌 Kritik nokta:
- `(row, col)` negatifse:
- - `(row, col+1 ... n-1)` tamamı negatiftir
- Bu yüzden:
- - `(n - col)` tane negatif eklenir
- Sonra **bir üst satıra çıkılır**.

### 4️⃣ Negatif Değilse
```python
else:
    col += 1
```
- Negatif değilse:
- - Bu sütunda yukarıda da negatif yoktur
- Sağa geçilir

### 5️⃣ Sonuç
```python
return count
```

### 📌 Küçük Örnek
```python
grid = [
  [ 4,  3,  2, -1],
  [ 3,  2,  1, -1],
  [ 1,  1, -1, -2],
  [-1, -1, -2, -3]
]
```
İzlenen yol:
- (3,0) → negatif → +4
- (2,0) → pozitif → sağ
- (2,1) → pozitif → sağ
- (2,2) → negatif → +2
- (1,2) → pozitif → sağ
- (1,3) → negatif → +1
- (0,3) → negatif → +1
**➡️ Toplam = 8**

## ⏱️ Zaman & Alan Karmaşıklığı
- **⏳ Zaman**
- - Her adımda ya **bir satır yukarı** ya **bir sütun sağa**
- - Toplam en fazla `m + n` adım
```python
O(m + n)
```

- **🧠 Alan**
- Sadece sabit değişkenler kullanılıyor
```python
O(1)
```