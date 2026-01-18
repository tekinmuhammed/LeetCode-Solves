# 🧩 1895. Largest Magic Square

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1895](https://leetcode.com/problems/largest-magic-square/description/)

---

## 🔍 Problem Özeti
- `grid` adlı bir 2D matris veriliyor.
- Amaç:
  - Matris içinde bulunan **en büyük sihirli (magic) kare alt-matrisin kenar uzunluğunu** bulmak.

### 🔮 Magic Square Nedir?
Bir `k × k` kare:
- Tüm **satırların toplamı eşit**
- Tüm **sütunların toplamı eşit**
- **Ana köşegen** ve **ters köşegen** toplamları da aynı

---

## 🧠 Temel Yaklaşım

Brute force ile her kareyi kontrol etmek pahalı olur.  
Bu yüzden:

### ✔️ Optimizasyon
- **Satır ve sütun prefix sum** kullanarak
  - Bir satırın veya sütunun toplamını **O(1)** sürede hesaplarız.
- Kare boyutlarını:
  - **En büyükten küçüğe** deneriz  
  → İlk bulunan geçerli kare, **maksimumdur**.

---

## 📊 Prefix Sum Yapıları

### Satır Prefix Sum
```python
row_ps[i][j] = grid[i][0] + grid[i][1] + ... + grid[i][j-1]
```

### Sütun Prefix Sum
```python
col_ps[i][j] = grid[0][j] + grid[1][j] + ... + grid[i-1][j]
```
Bu sayede:
- Bir satır aralığının toplamı
- Bir sütun aralığının toplamı tek işlemle bulunur.

### 🔎 Kontrol Edilen Şartlar
Bir `k × k` kare için:

**1️⃣ Referans Toplam**
```python
target = ilk satırın toplamı
```

**2️⃣ Satır Kontrolü**
```python
Her satırın toplamı == target
```

**3️⃣ Sütun Kontrolü**
```python
Her sütunun toplamı == target
```

**4️⃣ Köşegenler**
```python
Ana köşegen toplamı == target
Ters köşegen toplamı == target
```
Hepsi sağlanıyorsa → **Magic Square**

### 🔁 Algoritma Akışı
1. Prefix sum dizilerini oluştur
2. Kare boyutlarını:
```python
k = min(m, n) → 2
```
şeklinde **büyükten küçüğe** dene
3. Her `(i, j)` başlangıç noktası için:
- Satırları kontrol et
- Sütunları kontrol et
- Köşegenleri kontrol et

4. İlk bulunan geçerli `k` → cevap
5. Hiçbiri bulunamazsa → `1`

### ⏱️ Zaman ve Alan Karmaşıklığı
- **Zaman Karmaşıklığı:**
```python
O(min(m,n)³)
```

- **Alan Karmaşıklığı:**
```python
O(m × n)
```