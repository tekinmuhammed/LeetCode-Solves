# 🧩 2943. Maximize Area of Square Hole in Grid

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2943](https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/description/)

---

## 🔍 Problem Özeti
- `n x m` boyutunda bir grid var.
- Bazı **yatay (`hBars`)** ve **dikey (`vBars`)** çubuklar kaldırılıyor.
- Kaldırılan **ardışık çubuklar**, daha büyük boşluklar oluşturuyor.
- Amaç: Oluşabilecek **en büyük kare boşluğun alanını** bulmak.

---

## 🧠 Temel Fikir

Bir kare boşluğun alanı şu şekilde belirlenir:
```python
alan = kenar²
```

Kare olacağı için:
- Kenar uzunluğu = `min(max_yatay_boşluk, max_dikey_boşluk)`

---

## 📐 Boşluk (Gap) Hesabı

Kaldırılan çubuklar **ardışık** ise boşluk büyür.

Örnekler:
- `[2]` → boşluk = `2`
- `[2, 3]` → boşluk = `3`
- `[5, 6, 7]` → boşluk = `4`

📌 Genel kural:
```python
gap = (en uzun ardışık çubuk sayısı) + 1
```

---

## 🔧 Yardımcı Fonksiyon Mantığı

- Çubuklar sıralanır
- Ardışıklık `bars[i] == bars[i-1] + 1` ile kontrol edilir
- En uzun ardışık zincir bulunur
- Sonuç olarak `+1` eklenir

Boş liste durumu:
- Hiç çubuk kaldırılmadıysa → sadece `1x1` kare mümkündür

---

## 🧮 Nihai Hesaplama

```python
max_h = get_max_gap(hBars)
max_v = get_max_gap(vBars)

side = min(max_h, max_v)
return side * side
```
- Yatay ve dikey maksimum boşluklar hesaplanır
- Kare olacağı için küçük olan kenar alınır
- Alan = `kenar²`

### ⏱️ Zaman ve Alan Karmaşıklığı
- Zaman:
- - `O(h log h + v log v)` (sıralama)
- Alan:
- - `O(1)` ekstra bellek

