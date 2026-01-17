# 🧩 3047. Find the Largest Area of Square Inside Two Rectangles

**Difficulty:** Medium  
**Link:** [LeetCode 3047](https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/description/)

## 🔍 Problem Özeti
- Düzlemde eksenlere paralel **dikdörtgenler** verilmiştir.
- Her dikdörtgen:
  - `bottomLeft[i] = [x1, y1]`
  - `topRight[i] = [x2, y2]`
- Amaç:
  - **İki farklı dikdörtgenin kesişim alanı içinde**
  - Oluşturulabilecek **en büyük karenin alanını** bulmak.

📌 Eğer iki dikdörtgenin kesişimi yoksa, kare alanı `0` kabul edilir.

---

## 🧠 Temel Fikir

Bir kare ancak:
- İki dikdörtgenin **kesişim alanı** içinde bulunabilir.

Bu nedenle:
1. Tüm dikdörtgen **çiftlerini** dolaş
2. Her çift için:
   - Kesişim dikdörtgeninin **genişliğini (w)**
   - Kesişim dikdörtgeninin **yüksekliğini (h)**
   hesapla
3. Bu kesişim içinde oluşabilecek en büyük kare:
```python
kare_kenarı = min(w, h)
```

---

## 📐 Kesişim Hesabı

İki dikdörtgen için:

### Genişlik (x ekseni)
```python
w = min(x2_i, x2_j) - max(x1_i, x1_j)
```
### Yükseklik (y ekseni)
```python
h = min(y2_i, y2_j) - max(y1_i, y1_j)
```
- Eğer `w <= 0` veya `h <= 0` ise:
- - Kesişim yok → kare alanı `0`

### 🟥 Kare Alanı
Kesişim varsa:
```python
kare kenarı = min(w, h)
kare alanı  = (min(w, h))²
```
Tüm çiftler arasında **maksimum alan** alınır.

### 🧩 Kodun Mantıksal Akışı
1. `combinations` ile tüm dikdörtgen çiftlerini gez
2. Her çift için:
- Kesişim genişliği ve yüksekliği hesapla
- `min(w, h)` ile kare kenarını bul
3. En büyük kare kenarını sakla
4. Sonuç olarak:
```python
max_size * max_size
```

### ⏱️ Zaman ve Alan Karmaşıklığı
- **Zaman Karmaşıklığı:**
```python
O(N²)
```

- **Alan Karmaşıklığı:**
```python
O(1)
```