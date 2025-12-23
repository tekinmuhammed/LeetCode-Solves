# 2054. Two Best Non-Overlapping Events

**Difficulty:** Medium
**Problem Link:** [LeetCode 2054](https://leetcode.com/problems/two-best-non-overlapping-events/description/)

---

## 🧩 Problem Özeti

- Her etkinlik şu formatta veriliyor:  
  `[startTime, endTime, value]`
- **En fazla iki etkinlik** seçebilirsin.
- Seçilen etkinlikler **zaman olarak çakışmamalı**.
- Amaç: **Toplam değeri maksimum yapmak**.

> 📌 Çakışmama kuralı:  
> İkinci etkinliğin başlangıcı **ilk etkinliğin bitişinden en az 1 gün sonra** olmalı.

---

## 🧠 Çözüm Fikri (Sorting + Binary Search + Suffix Max)

Senin çözümün çok klasik ve güçlü bir yaklaşım kullanıyor:

### Temel strateji:
1. Etkinlikleri **başlangıç zamanına göre sırala**
2. Her etkinlik için:
   - Ya **tek başına** al
   - Ya da **sonraki çakışmayan en iyi etkinlikle birlikte** al
3. Bunu hızlı yapmak için:
   - **Binary Search**
   - **Suffix Maximum Array**

---

## 🔢 Adım Adım Açıklama

---

### 1️⃣ Etkinlikleri Başlangıç Zamanına Göre Sırala

```python
events.sort()
```
Bundan sonra:
- `events[i][0]` → başlangıç
- `events[i][1]` → bitiş
- `events[i][2]` → değer

### 2️⃣ Suffix Maximum Dizisi
```python
suffixMax[i] = max(events[i][2], events[i+1][2], ...)
```
Kod:
```python
suffixMax = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    suffixMax[i] = max(suffixMax[i + 1], events[i][2])
```
📌 Anlamı:
- `i`’den sonraki **en yüksek değerli etkinliği** `O(1)` zamanda bulabiliriz.

### 3️⃣ Binary Search için Başlangıç Zamanları
```python
starts = [e[0] for e in events]
```
Bu sayede:
- “Bitiş zamanı `e` olan etkinlikten sonra başlayabilecek ilk etkinlik hangisi?”
sorusunu **O(log n)** zamanda buluruz.

### 4️⃣ Ana Döngü: Her Etkinliği Deniyoruz
```python
for i in range(n):
    s, e, v = events[i]
```
**🅰️ Seçenek 1: Sadece Bu Etkinlik**
```python
ans = max(ans, v)
```
**🅱️ Seçenek 2: Bu + Çakışmayan En İyi Etkinlik**
```python
j = bisect.bisect_left(starts, e + 1)
```
- `e + 1` → çakışmama şartı
- `j` → ilk uygun etkinlik indeksi
    Eğer varsa:
```python
ans = max(ans, v + suffixMax[j])
```

### 🏁 Sonuç
```python
return ans
```
Bu, **en fazla iki çakışmayan etkinlikten elde edilebilecek maksimum değerdir**.

### ⏱️ Zaman & Alan Karmaşıklığı
- **Zaman:**
- - Sıralama: `O(n log n)`
- - Her etkinlik için binary search: `O(log n)`
- - **Toplam:** `O(n log n)`

- **Alan:**
- - `suffixMax`, `starts`: `O(n)`

### 🧪 Küçük Örnek
```python
events = [[1,3,4],[2,4,1],[3,10,2],[5,6,5]]
```
- En iyi seçim:
- - `[1,3,4]`
- - `[5,6,5]`
- Toplam = `9`