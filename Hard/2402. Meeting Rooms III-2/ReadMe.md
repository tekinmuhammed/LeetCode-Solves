# 2402. Meeting Rooms III

**Difficulty:** Hard  
**Link:** [LeetCode 2402](https://leetcode.com/problems/meeting-rooms-iii)

---

## 🧩 Problem Özeti

- `n` adet toplantı odası var (`0` → `n-1`)
- Her toplantı `[start, end]` şeklinde veriliyor
- Toplantılar **başlangıç zamanına göre sırayla** ele alınıyor

### Kurallar
1. Toplantı başladığında **boş olan en küçük indeksli oda** kullanılır
2. Eğer hiçbir oda boş değilse:
   - **En erken boşalacak oda** seçilir
   - Toplantı, o odanın boşalma zamanında başlar (gecikmeli)
3. Amaç:
> **En çok toplantı yapılan odanın indeksini** döndürmek  
(Eşitlikte daha küçük indeks)

---

## 🧠 Senin Çözümünün Temel Fikri

Tamamen **simülasyon** yaklaşımı:

- `times[i]` → i. odanın ne zaman boşalacağı
- `ans[i]` → i. odada kaç toplantı yapıldığı

Toplantıları sırayla alıp:
- Önce boş oda var mı bakıyorsun
- Yoksa en erken boşalan odayı seçiyorsun

---

## 🔍 Kodunun Adım Adım Açıklaması

---

### 1️⃣ Başlangıç Değişkenleri
```python
ans = [0] * n
times = [0] * n
meetings.sort()
```
- `ans[i]` → oda kullanım sayısı
- `times[i]` → odanın müsait olacağı zaman
- Toplantılar başlangıç zamanına göre sıralanıyor ✔️

### 2️⃣ Her Toplantıyı İşle
```python
for meeting in meetings:
    start, end = meeting
```
Her toplantı için:

### 3️⃣ Oda Arama
```python
flag = False
minind = -1
val = float('inf')
```
- `flag` → boş oda bulundu mu?
- `minind` → en erken boşalacak oda
- `val` → onun zamanı

### 🔹 Tüm Odaları Gez
```python
for j in range(n):
    if times[j] < val:
        val = times[j]
        minind = j
```
👉 En erken boşalan oda sürekli güncelleniyor

### 🔹 Eğer Oda Boşsa (times[j] ≤ start)
```python
if times[j] <= start:
    flag = True
    ans[j] += 1
    times[j] = end
    break
```
- Kurala uygun şekilde **ilk boş oda** seçiliyor
- Toplantı direkt yerleştiriliyor
- Döngüden çıkılıyor

### 4️⃣ Hiç Oda Boş Değilse
```python
if not flag:
    ans[minind] += 1
    times[minind] += (end - start)
```
- En erken boşalan oda seçiliyor
- Toplantı gecikmeli başlıyor
- Süre korunuyor: `(end - start)`

### 5️⃣ En Çok Kullanılan Odayı Bul
```python
maxi = -1
id = -1
for i in range(n):
    if ans[i] > maxi:
        maxi = ans[i]
        id = i
```
- En yüksek toplantı sayısı aranıyor
- Eşitlikte küçük indeks otomatik kazanıyor ✔️


### 🧪 Küçük Örnek
```python
n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]
```
Simülasyon sonucu:
- Oda 0 → 3 toplantı
- Oda 1 → 1 toplantı
**➡️ Cevap: 0**

### ⏱️ Zaman & Alan Karmaşıklığı
- **⏳ Zaman**
- - Her toplantı için n oda taranıyor
    **➡️ O(m × n)**

> Bu yüzden büyük inputlarda TLE riski var.

- **🧠 Alan**
    **O(n)**