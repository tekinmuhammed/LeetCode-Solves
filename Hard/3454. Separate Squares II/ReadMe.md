# 3454. Separate Squares II

---

## 🧩 Problem Özeti (I ile farkı)

Bu problem, **3453. Separate Squares I**’in **daha zor versiyonu**.

Önemli fark:
- **Kareler üst üste binebilir**
- Alan **örtüşmeler dikkate alınarak (union area)** hesaplanmalı
- Yani artık:
  - “Her kareyi ayrı ayrı say” ❌
  - “Gerçek birleşim alanını hesapla” ✅

🎯 Amaç yine aynı:
> Yatay bir `y = k` çizgisiyle, **altındaki birleşim alanı = üstündeki birleşim alanı** olacak `k` değerini bulmak.

---

## 🧠 Ana Yaklaşım

Bu problem **klasik bir Sweep Line + Interval Union + Alan birikimi** problemidir.

Temel fikir:
1. **Y ekseni boyunca sweep (tarama)**
2. Her yatay şeritte:
   - Aktif karelerin **x-projeksiyonlarının birleşim uzunluğunu** bul
3. Şerit alanlarını sırayla biriktir
4. Toplam alanın yarısına ulaşılan noktada **kesin y değerini hesapla**

---

## 🔑 Adım Adım Çözüm Mantığı

---

### 1️⃣ Event Listesi Oluşturma (Sweep Line)

Her kare için iki olay eklenir:

```text
(y,     +1, x1, x2)  → kare başlıyor
(y + l, -1, x1, x2)  → kare bitiyor
python
Kodu kopyala
events.append((y, 1, x, x + l))
events.append((y + l, -1, x, x + l))
📌 typ = 1 → ekle
📌 typ = -1 → çıkar

Sonra:

python
Kodu kopyala
events.sort()
2️⃣ Union Length (X ekseni birleşim uzunluğu)
Aktif aralıkların örtüşmeden toplam uzunluğunu hesaplayan fonksiyon:

python
Kodu kopyala
def union_length(intervals):
    intervals.sort()
    total = 0
    cur_start, cur_end = -1, -1
    for s, e in intervals:
        if s > cur_end:
            total += cur_end - cur_start
            cur_start, cur_end = s, e
        else:
            cur_end = max(cur_end, e)
    total += cur_end - cur_start
    return total
✔️ Overlap’leri doğru şekilde birleştiriyor
✔️ En kritik yardımcı fonksiyon

3️⃣ Sweep Line ile Alan Biriktirme
python
Kodu kopyala
active = []     # aktif x aralıkları
strips = []     # (y1, y2, width, area_before)
total_area = 0
Her iki y event’i arasında:

text
Kodu kopyala
alan = (y - prev_y) * union_width
Kaydedilen bilgi:

python
Kodu kopyala
strips.append((prev_y, y, width, total_area))
📌 Bu sayede:

Alanın hangi y aralığında

Ne kadar genişlikte

Toplam alanın neresinde olduğunu biliyoruz

4️⃣ Alanın Yarısını Bulma
python
Kodu kopyala
half = total_area / 2
Strip’ler üzerinde ilerle:

python
Kodu kopyala
if area_before + area_here >= half:
    return y1 + (half - area_before) / width
🎯 İşte aradığımız kesin y değeri

✅ Senin Kodun
python
Kodu kopyala
class Solution(object):
    def separateSquares(self, squares):
        events = []
        
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
        
        events.sort()
        
        def union_length(intervals):
            intervals.sort()
            total = 0
            cur_start, cur_end = -1, -1
            for s, e in intervals:
                if s > cur_end:
                    total += cur_end - cur_start
                    cur_start, cur_end = s, e
                else:
                    cur_end = max(cur_end, e)
            total += cur_end - cur_start
            return total
        
        strips = []
        active = []
        prev_y = events[0][0]
        total_area = 0.0
        
        i = 0
        while i < len(events):
            y = events[i][0]
            height = y - prev_y
            if height > 0 and active:
                width = union_length(active)
                area = width * height
                strips.append((prev_y, y, width, total_area))
                total_area += area
            
            while i < len(events) and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                if typ == 1:
                    active.append((x1, x2))
                else:
                    active.remove((x1, x2))
                i += 1
            
            prev_y = y
        
        half = total_area / 2.0
        
        for y1, y2, width, area_before in strips:
            area_here = width * (y2 - y1)
            if area_before + area_here >= half:
                return y1 + (half - area_before) / width
        
        return 0.0
🔍 Kod Değerlendirmesi
✔️ Doğruluk
Overlap’ler doğru şekilde union alınıyor

Alan hesapları geometrik olarak kusursuz

✔️ Algoritmik Seviye
Sweep Line

Interval Union

Kümülatif alan + interpolasyon

👉 Bu çözüm Hard++ seviyesi

⏱️ Zaman & Bellek
Event sayısı: 2n

Her event’te union_length → O(k log k)

Toplam: O(n² log n) (n küçük olduğu için kabul edilebilir)