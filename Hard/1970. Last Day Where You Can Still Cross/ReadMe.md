# 1970. Last Day Where You Can Still Cross

**Difficulty:** Hard
**Problem Link:** [LeetCode 1970](https://leetcode.com/problems/last-day-where-you-can-still-cross/description/)

---

## 🧩 Problem Özeti

`row × col` boyutunda bir grid var.  
Her gün bir hücre **suya dönüşüyor** (`cells` sırasına göre).

🎯 Amaç:
> **Üst satırdan alt satıra**, sadece **kara hücrelerden (0)** geçerek **en son hangi gün geçiş yapılabildiğini** bulmak.

---

## 🧠 Ana Fikir

Bu problem iki güçlü tekniğin birleşimiyle çözülür:

1. **Binary Search (İkili Arama)**  
   → “Geçilebilen son günü” arıyoruz → **monoton özellik var**
2. **BFS (Breadth-First Search)**  
   → Belirli bir günde geçiş mümkün mü?

---

## 🔍 Neden Binary Search?

- Gün sayısı arttıkça:
  - Su hücreleri **artar**
  - Geçiş yapmak **zorlaşır**
- Yani:
  - `canCross(day)`  
    → `True, True, True, ..., False, False`

✔️ Bu yapı **binary search** için birebir uygundur.

---

## 🛠️ `canCross(day)` Fonksiyonu

Belirli bir `day` için:

### 1️⃣ Grid’i Oluştur

```python
grid = [[0] * col for _ in range(row)]

for i in range(day):
    r, c = cells[i]
    grid[r-1][c-1] = 1
```
- `0` → kara
- `1` → su

### 2️⃣ BFS Başlangıcı (Üst Satır)
```python
q = deque()
visited = [[False]*col for _ in range(row)]

for j in range(col):
    if grid[0][j] == 0:
        q.append((0, j))
        visited[0][j] = True
```
- Üst satırdaki **tüm kara hücrelerden** başlarız

### 3️⃣ BFS Yayılımı
```python
while q:
    x, y = q.popleft()
    
    if x == row - 1:
        return True
```
- Alt satıra ulaşırsak **→ geçiş mümkün**
```python
for dx, dy in directions:
    nx, ny = x + dx, y + dy
    if 0 <= nx < row and 0 <= ny < col:
        if not visited[nx][ny] and grid[nx][ny] == 0:
            visited[nx][ny] = True
            q.append((nx, ny))
```
- Sadece:
- - grid içinde
- - kara hücre
- - daha önce ziyaret edilmemiş

### 4️⃣ BFS Biterse
```python
return False
```
- Alt satıra ulaşılamadı → geçiş yok

### 🔁 Binary Search Kısmı
```python
left, right = 0, len(cells)
answer = 0

while left <= right:
    mid = (left + right) // 2
    if canCross(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
```
- `canCross(mid) == True`
    → daha ileri günleri dene

- `False`
    → daha erken günlere dön

### ✅ Sonuç
```python
return answer
```
- **Geçilebilen en son gün**

## ⏱️ Karmaşıklık Analizi
- **🧮 Zaman**
- - `canCross` → **O(row × col)** (BFS)
- - Binary Search → **O(log(row × col))**
- **📌 Toplam:**
- - `O(row × col × log(row × col))`
- **🧠 Alan**
- - Grid + visited → **O(row × col)**