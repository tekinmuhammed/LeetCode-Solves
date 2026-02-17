# 401. Binary Watch

## Problem Özeti

Bir binary saat var:

- Saat kısmı → 4 LED (0–11)
- Dakika kısmı → 6 LED (0–59)

Toplam 10 LED bulunuyor.

Verilen `turnedOn` değeri,
yanan LED sayısını temsil eder.

Amaç:

Tam olarak `turnedOn` adet LED yanıyorken
oluşabilecek tüm geçerli saatleri listelemek.

---

## Çözüm Mantığı

Bu problem için brute-force yeterlidir çünkü:

Toplam olası zaman sayısı:

12 × 60 = 720

Bu küçük bir sayı olduğu için tüm kombinasyonları deneyebiliriz.

---

## Adımlar

1. Saatleri 0–11 arasında dolaş.
2. Dakikaları 0–59 arasında dolaş.
3. Her kombinasyon için:
   - Saatteki `1` bit sayısını bul.
   - Dakikadaki `1` bit sayısını bul.
4. Eğer toplam `turnedOn` değerine eşitse:
   - Formatlı şekilde sonucu ekle.

---

## Kod

```python
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        times = []
        
        # Saatler 0-11 arası olabilir
        for h in range(12):
            # Dakikalar 0-59 arası olabilir
            for m in range(60):
                
                # Saat ve dakikanın binary temsillerindeki 1 sayısı
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                    
                    # Dakika her zaman 2 haneli yazılmalı
                    times.append(f"{h}:{m:02d}")
                    
        return times
```

---

## Önemli Noktalar

### 1️⃣ `bin(x).count('1')`

- `bin(5)` → `'0b101'`
- `'0b101'.count('1')` → 2

Bu sayede bit sayısını kolayca hesaplıyoruz.

---

### 2️⃣ Formatlama

```
f"{h}:{m:02d}"
```

- Saat normal yazılır.
- Dakika 2 haneli olur.
  - 5 → 05
  - 9 → 09

---

## Örnek

turnedOn = 2

Olası bazı sonuçlar:

- 0:03
- 0:05
- 0:06
- 1:01
- 2:01
- 4:01
- 8:01
- ...

---

## Zaman Karmaşıklığı

O(12 × 60)

Sabit → O(1)

---

## Alan Karmaşıklığı

En kötü durumda 720 sonuç olabilir.

Sabit üst sınır → O(1)

---

## Küçük İyileştirme (Python 3.8+)

Daha hızlı bit sayımı:

```python
if (h.bit_count() + m.bit_count()) == turnedOn:
```

`bit_count()` doğrudan CPU seviyesinde çalışır.

