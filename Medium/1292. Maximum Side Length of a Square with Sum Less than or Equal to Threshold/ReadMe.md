# 🧩 1292. Maximum Side Length of a Square with Sum ≤ Threshold

**Difficulty:** Medium  
**Link:** [LeetCode 1292](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/description/)  

## 🔍 Problem Özeti
- `mat` adlı bir 2D matris ve bir `threshold` değeri veriliyor.
- Amaç:
  - **Elemanları toplamı `threshold` değerini aşmayan**
  - **en büyük kare alt-matrisin kenar uzunluğunu** bulmak.

---

## 🧠 Temel Fikir

Brute-force ile tüm kareleri tek tek hesaplamak çok maliyetlidir.  
Bu yüzden iki güçlü tekniği birleştiriyoruz:

### ✔️ 1. Prefix Sum (Önek Toplam)
- Kare içindeki toplamı **O(1)** sürede hesaplamak için

### ✔️ 2. Binary Search
- Kare kenar uzunluğunu **maksimize etmek** için

---

## 📊 Prefix Sum Matrisi

### Tanım
```python
ps[i][j] = mat[0..i-1][0..j-1] elemanlarının toplamı
```

### Hesaplama
```python
ps[i+1][j+1] = ps[i][j+1] + ps[i+1][j] - ps[i][j] + mat[i][j]
```

### Bir k × k Karenin Toplamı
Sol üst köşe `(i, j)` ise:
```python
sum = ps[i+k][j+k]
    - ps[i][j+k]
    - ps[i+k][j]
    + ps[i][j]
```
⏱️ **O(1)** zamanda!

### 🔎 Yardımcı Fonksiyon: exists_square(k)
**Amaç:**
- **En az bir tane** `k × k` kare var mı?
- Ve bu karenin toplamı `threshold`’dan küçük/eşit mi?

**İşleyiş**
- Tüm olası `(i, j)` başlangıç noktalarını dener
- Prefix sum ile toplamı hesaplar
- Şart sağlanırsa hemen `True` döner

### 🔁 Binary Search Stratejisi
Aradığımız şey:
> **En büyük geçerli kare kenar uzunluğu**

### Aralık
```python
left = 1
right = min(m, n)
```
### Mantık
- Eğer `k` boyutunda geçerli kare varsa:
- - Daha büyüğü olabilir → `left = k + 1`
- Yoksa:
- - Küçült → `right = k - 1`

### ⏱️ Zaman ve Alan Karmaşıklığı
- **Zaman Karmaşıklığı**
```python
O(m × n × log(min(m, n)))
```
- - Binary search → `log(min(m,n))`
- - Her kontrol → `O(m × n)`

- **Alan Karmaşıklığı**
```python
O(m × n)
```
(Prefix sum matrisi)