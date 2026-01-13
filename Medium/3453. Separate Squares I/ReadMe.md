# 3453. Separate Squares I

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3443](https://leetcode.com/problems/separate-squares-i/description/)

---

## 🧩 Problem Özeti

Düzlemde verilen kareler var.  
Her kare şu şekilde tanımlanıyor:

```python
[x, y, l]  → sol-alt köşe (x, y), kenar uzunluğu l
```

### 🎯 Amaç:
> **Yatay bir çizgi (y = k)** çizerek, bu çizginin **altında kalan toplam alan = üstünde kalan toplam alan** olacak şekilde k değerini bulmak.
Sonuç **float** olarak döndürülmeli.

### 💡 Ana Fikir
Bu problemde kritik nokta şu:
- Kareler **üst üste binebilir**
- Alan hesabı **her kare için ayrı ayrı** yapılır
- Çizgi y = k, bir kareyi:
- - Tamamen yukarıda
- - Tamamen aşağıda
- - Ya da **kısmen kesebilir**
👉 Bu nedenle **doğrudan formül** yok
👉 **Binary Search (ikili arama)** ile çözüm ideal

### 🧠 Strateji
**1️⃣ Toplam Alanı Hesapla**
Her karenin alanı: `l²`
```python
total_area += l**2
```

**2️⃣ Binary Search Aralığı**
- Alt sınır: `0`
- Üst sınır: en yüksek karenin üst kenarı
```python
max_y = max(y + l)
```

**3️⃣ Kontrol Fonksiyonu check(limit_y)**
Bu fonksiyon şunu yapar:
> y = limit_y çizgisinin altında kalan alan,
> toplam alanın yarısından büyük mü?
Her kare için:
- Eğer kare çizginin **tamamen üstündeyse** → katkı yok
- Eğer kare çizgiyi **kesiyorsa** → `l * (limit_y - y)`
- En fazla `l * l` olabilir → `min(...)`
```python
area += l * min(limit_y - y, l)
```

### ✅ Kod
```python
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        max_y, total_area = 0, 0
        for x, y, l in squares:
            total_area += l**2
            max_y = max(max_y, y + l)

        def check(limit_y):
            area = 0
            for x, y, l in squares:
                if y < limit_y:
                    area += l * min(limit_y - y, l)
            return area >= total_area / 2

        lo, hi = 0, max_y
        eps = 1e-5
        while abs(hi - lo) > eps:
            mid = (hi + lo) / 2
            if check(mid):
                hi = mid
            else:
                lo = mid

        return hi
```

### 🔍 Kod İncelemesi

**✔️ Zaman Karmaşıklığı**
- `check()` → `O(n)`
- Binary Search → ~`log(1e5)`
- **Toplam:** `O(n log M)` ✔️

### 📌 Neden Binary Search Çalışıyor?
Çünkü:
- `f(y) = çizginin altındaki alan`
- `f(y)` monoton artan
- Yani:
- - Küçük y → az alan
- - Büyük y → fazla alan