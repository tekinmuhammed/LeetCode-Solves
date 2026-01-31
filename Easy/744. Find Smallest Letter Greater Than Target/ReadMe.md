## 744. Find Smallest Letter Greater Than Target

**Difficulty:** Easy  
**Link:** [LeetCode 744](https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/)

---

### Problem Özeti

- Sana **sıralı** (`sorted`) bir karakter listesi `letters` veriliyor
- Bir de `target` karakteri var
- Amaç:
  - `target`’tan **strictly greater (>)** olan **en küçük harfi** bulmak
- Eğer böyle bir harf yoksa:
  - **wrap-around** yap → dizinin ilk elemanını döndür

---

## Senin Çözümünün Ana Fikri 🎯

Bu problem **klasik binary search + wrap-around** sorusu.

Temel soru:
> `letters` dizisinde `target`’tan büyük olan **ilk elemanın indeksi nedir?`

---

## Binary Search Mantığı 🧠
```python
left, right = 0, len(letters) - 1
```

## Döngü Koşulu
```python
while left <= right:
```

## Orta Nokta
```python
mid = (left + right) // 2
```

## Karar Mekanizması
```python
if letters[mid] <= target:
    left = mid + 1
else:
    right = mid - 1
```

Neden böyle?
letters[mid] <= target ise:

Bu harf işimize yaramaz

Daha büyük bir harf arıyoruz → sağa git

letters[mid] > target ise:

Bu aday olabilir

Daha küçüğü var mı diye sola kay

Döngü Sonrası Durum 🔍
Binary search bittiğinde:

left = target’tan büyük olan ilk elemanın indeksi
Wrap-around Kontrolü 🔁
return letters[left] if left < len(letters) else letters[0]
İki Olasılık:
1️⃣ left < len(letters)

Dizide target’tan büyük bir harf bulundu

Direkt döndür

2️⃣ left == len(letters)

Dizide target’tan büyük hiçbir harf yok

Wrap-around → ilk eleman

Örnek Üzerinden 🎯
letters = ["c","f","j"]
target = "j"
Binary search sonunda:

left = 3 (len(letters))
➡️ Wrap-around:

return letters[0]  # "c"
Zaman & Alan Karmaşıklığı ⏱️
Time: O(log n)

Space: O(1)