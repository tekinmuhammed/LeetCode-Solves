# 3721. Longest Balanced Subarray II

**Difficulty:** Hard
**Link:** [LeetCode 3721](https://leetcode.com/problems/longest-balanced-subarray-ii/description/)

---

## Problem Özeti

Balanced subarray tanımı:

Bir subarray’de:

- Farklı (distinct) çift sayı sayısı
- Farklı (distinct) tek sayı sayısı

eşitse → subarray balanced kabul edilir.

Ama bu kez:

- n büyük
- O(n²) brute force mümkün değil
- Daha optimize bir yaklaşım gerekiyor

---

# Ana Fikir

Bu çözüm şu fikre dayanıyor:

Balanced ⇔

distinct_even_count − distinct_odd_count = 0

Bunu prefix sum mantığına çeviriyoruz.

---

# 1️⃣ Sayıları +1 / -1'e Çevirme

Her sayı için:

- çift → +1
- tek → -1

```python
def sgn(x):
    return 1 if x % 2 == 0 else -1
```

Ama kritik nokta şu:

Biz her sayı geldiğinde doğrudan prefix’e eklemiyoruz.

Sadece o sayı **ilk kez görüldüğünde** ekliyoruz.

Çünkü:
Biz distinct sayıyoruz, tekrarları değil.

---

# 2️⃣ prefix_sum Mantığı

prefix_sum[i] şu anlama gelir:

0 → i arası
distinct_even − distinct_odd

Eğer iki indeks arasında prefix farkı 0 ise:

O aralık balanced’tır.

---

# 3️⃣ Neden Segment Tree?

Ama problem şurada:

Bir sayının tekrarını geçtiğimizde,
o sayının etkisini artık çıkarmamız gerekiyor.

Yani:

Sliding window gibi davranıyoruz,
ama prefix değerleri dinamik değişiyor.

Bu yüzden:

- Range update gerekiyor
- Range min/max kontrolü gerekiyor
- Belirli bir değeri (0) son görülen yerde bulmamız gerekiyor

Bu yüzden:

👉 Lazy propagation’lı Segment Tree kullanılıyor.

---

# Segment Tree Ne Tutuyor?

Her node:

```python
min_value
max_value
```

Neden?

Çünkü biz şunu yapıyoruz:

"Bu aralıkta prefix_sum == 0 olan en sağdaki index’i bul"

Eğer:
- min > 0
- max < 0

ise → 0 yok demektir.

---

# Algoritma Akışı

## 1️⃣ Prefix oluştur

Her sayının:

- ilk görüldüğü yerde +1 veya -1 eklenir
- tekrar görüldüğünde eklenmez

Aynı zamanda:

```python
occurrences[value] → o değerin pozisyonları
```

saklanır.

---

## 2️⃣ Segment Tree kur

prefix_sum dizisi üzerine kurulur.

---

## 3️⃣ Sliding Window Mantığı

Her i için:

```python
length = max(length, seg.find_last(i + length, 0) - i)
```

Bu ne demek?

- i’den başlayarak
- prefix_sum farkı 0 olan
- en sağdaki pozisyonu bul
- uzunluğu güncelle

---

## 4️⃣ Sayının etkisini kaldırma

i ilerlediğinde:

nums[i] artık window’dan çıkıyor.

O sayının bir sonraki occurrence pozisyonunu buluyoruz:

```python
next_pos
```

Ve şu aralığı güncelliyoruz:

```python
seg.add(i + 1, next_pos - 1, -sgn(nums[i]))
```

Bu ne yapıyor?

O sayı artık distinct olmaktan çıktığı için,
prefix değerlerinden etkisini siliyor.

Bu yüzden range update gerekiyor.

---

# Zaman Karmaşıklığı

- Segment tree build → O(n)
- Her index için:
  - 1 find
  - 1 range update

Toplam:

O(n log n)

---

# Alan Karmaşıklığı

- Segment tree → O(n)
- occurrences → O(n)

**Toplam:**
`O(n)`
