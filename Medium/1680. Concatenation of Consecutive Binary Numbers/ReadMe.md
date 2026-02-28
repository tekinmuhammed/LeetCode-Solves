# 1680. Concatenation of Consecutive Binary Numbers

## Problem Özeti

Pozitif bir tam sayı `n` veriliyor.

Amaç:

1’den `n`’e kadar olan sayıların **binary gösterimlerini sırayla yan yana eklemek**
(concatenate etmek) ve oluşan büyük binary sayının **decimal karşılığını**
`10^9 + 7` modunda döndürmek.

---

## Örnek

```
n = 3
```

Binary gösterimler:

```
1  -> 1
2  -> 10
3  -> 11
```

Birleştirme:

```
"1" + "10" + "11" = "11011"
```

Decimal:

```
11011₂ = 27
```

---

## Ana Fikir

Her sayıyı string olarak eklemek **çok yavaş** olur.

Bunun yerine:

- Sayıyı bit seviyesinde ekliyoruz
- Sol kaydırma (`<<`) kullanıyoruz
- Mod işlemini her adımda uyguluyoruz

---

## Kritik Gözlem

Bir sayı `i`’nin binary uzunluğu:

```
bit_length = floor(log2(i)) + 1
```

Ama bunu hesaplamak yerine şu çok pratik kontrolü kullanabiliriz:

```
i & (i - 1) == 0
```

Bu ifade **yalnızca `i` bir power of two ise** true olur.

Örnek:

```
1  -> 1     (2^0)
2  -> 10    (2^1)
4  -> 100   (2^2)
8  -> 1000  (2^3)
```

Bu noktalarda binary uzunluk **1 artar**.

---

## Algoritma

1. `result = 0` ile başla
2. `bit_length = 0` tut
3. `i`’yi 1’den `n`’e kadar dolaş:
   - Eğer `i` bir power of two ise → `bit_length += 1`
   - `result`’ı `bit_length` kadar sola kaydır
   - `i`’yi OR (`|`) ile ekle
   - Mod al
4. Sonucu döndür

---

## Kod

```python
class Solution(object):
    def concatenatedBinary(self, n):
        MOD = 10**9 + 7
        result = 0
        bit_length = 0

        for i in range(1, n + 1):
            # i power of two ise bit sayısı artar
            if i & (i - 1) == 0:
                bit_length += 1

            result = ((result << bit_length) | i) % MOD

        return result
```

---

## Adım Adım Örnek

```
n = 3
```

Başlangıç:

```
result = 0
bit_length = 0
```

### i = 1
```
1 power of two → bit_length = 1
result = (0 << 1) | 1 = 1
```

### i = 2
```
2 power of two → bit_length = 2
result = (1 << 2) | 2 = 110₂ = 6
```

### i = 3
```
3 power of two değil
result = (6 << 2) | 3 = 11011₂ = 27
```

---

## Zaman Karmaşıklığı

```
O(n)
```

Her sayı için sabit sayıda işlem yapılır.

---

## Alan Karmaşıklığı

```
O(1)
```

Sadece birkaç değişken kullanılır.

---

## Neden Bu Çözüm Çok İyi?

✔ String işlemi yok  
✔ Bit manipulation kullanıyor  
✔ Power-of-two trick çok temiz  
✔ Mod kontrolü güvenli  
✔ Interview ve yarışma için ideal  

---

## Özet

Bu çözüm:

- Binary birleştirmeyi matematiksel hale getiriyor
- Power of two kontrolüyle bit uzunluğunu doğru yönetiyor
- Büyük sayıları mod ile güvenli biçimde hesaplıyor

Gerçekten çok şık bir çözüm 👏  

Hazırsan 👉 **bir sonraki soruya geçelim** 🚀