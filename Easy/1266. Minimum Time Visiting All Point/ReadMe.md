# 1266. Minimum Time Visiting All Points

**Difficulty:** Easy
**Link:** [LeetCode 1266](https://leetcode.com/problems/minimum-time-visiting-all-points/description/)

---

## 🧩 Problem Özeti

2D düzlemde bir dizi nokta veriliyor.  
Başlangıç noktası `points[0]`.

Her 1 saniyede şu hareketlerden **birini** yapabilirsin:
- Yukarı / aşağı
- Sağa / sola
- Çapraz (hem x hem y aynı anda ±1)

🎯 Amaç:
> Noktaları **verilen sırayla** ziyaret etmek için gereken **minimum süreyi** bulmak.

---

## 💡 Temel Gözlem (Kritik İçgörü)

İki nokta arasındaki minimum süre:

```python
max(|x₂ - x₁|, |y₂ - y₁|)
```

**Neden?**
- Çapraz hareket, hem x hem y ekseninde **aynı anda** ilerler
- Önce ortak mesafeyi çapraz gidersin
- Kalan fark varsa tek eksende devam edersin
📌 Bu mesafe metriğine **Chebyshev Distance** denir.

### ✏️ Matematiksel Açıklama
İki nokta:
```python
(x₁, y₁) → (x₂, y₂)
```
- Çapraz adım sayısı: `min(|Δx|, |Δy|)`
- Kalan adım sayısı: `| |Δx| - |Δy| |`
Toplam:
```python
min(dx, dy) + (max(dx, dy) - min(dx, dy)) = max(dx, dy)
```

### ✅ Kod
```python
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        total_time = 0
        
        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]
            
            total_time += max(abs(x2 - x1), abs(y2 - y1))
        
        return total_time
```

### 🧪 Örnek
```python
points = [[1,1],[3,4],[-1,0]]
```
Hesap:
```python
(1,1) → (3,4) = max(2,3) = 3
(3,4) → (-1,0) = max(4,4) = 4
Toplam = 7
```

### ⏱️ Zaman & Alan Karmaşıklığı
- **Zaman:** `O(n)`
- **Alan:** `O(1)`