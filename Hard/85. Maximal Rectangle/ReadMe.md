# 85. Maximal Rectangle

**Difficulty:** Hard  
**Link:** [LeetCode 85](https://leetcode.com/problems/maximal-rectangle/description/)

---

## 🧩 Problem Özeti

Binary bir matris veriliyor (`'0'` ve `'1'`lerden oluşan).

🎯 Amaç:
> Sadece `'1'`lerden oluşan **en büyük dikdörtgen alanını** bulmak.

---

## 💡 Ana Fikir

Bu problem, çok güçlü bir indirgeme (reduction) içerir:

> **Her satırı**, bir histogramın tabanı gibi düşün.

- Yukarıdan aşağıya doğru `'1'` gördükçe **yükseklik artırılır**
- `'0'` görülürse o sütunun yüksekliği **sıfırlanır**
- Her satırda oluşan histogram için  
  👉 **Largest Rectangle in Histogram** problemi çözülür

Sonuç: Tüm satırlar boyunca bulunan maksimum alan.

---

## 🧱 Histogram Mantığı

Örnek:
```python
Matrix:
1 0 1 1
1 1 1 1
```
**2.**satırda histogram:
```python
heights = [2, 1, 2, 2]
```
Bu histogramda en büyük dikdörtgen alanı hesaplanır.

### 📐 Histogramda En Büyük Dikdörtgen
Bu kısım **monoton stack** ile çözülür:

### Stack Özelliği
- Stack, **artan yükseklik indekslerini** tutar
- Daha küçük bir yükseklik gelince:
- - Stack’ten pop edilir
- - Pop edilen yüksekliğe ait maksimum genişlik hesaplanır

### Genişlik Hesabı
```python
width = i                     (stack boşsa)
width = i - stack[-1] - 1     (değilse)
```

### ✅Kod
```python
class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            # Histogram yüksekliklerini güncelle
            for i in range(cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            
            # Histogramda en büyük dikdörtgen
            stack = []
            for i in range(cols + 1):
                cur_height = heights[i] if i < cols else 0
                while stack and cur_height < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * width)
                stack.append(i)
        
        return max_area
```

### 🧠 Neden `cols + 1`?
Sonuna **yüksekliği 0 olan sanal bir sütun** eklenir.
➡️ Bu sayede stack’te kalan tüm sütunlar da hesaplanmış olur.

### 🧪 Örnek
```python
matrix =
[
 ["1","0","1","0","0"],
 ["1","0","1","1","1"],
 ["1","1","1","1","1"],
 ["1","0","0","1","0"]
]
```
➡️ Çıktı: `6`

### ⏱️ Zaman & Alan Karmaşıklığı
- **Zaman:** `O(rows × cols)`
- **Alan:** `O(cols)` (stack + heights)