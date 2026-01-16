# 🧩 2975. Maximum Square Area by Removing Fences From a Field

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2975](https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/description/)

## 🔍 Problem Özeti
- `m x n` boyutlarında bir tarla var.
- Bazı **yatay (`hFences`)** ve **dikey (`vFences`)** çitler kaldırılabiliyor.
- Kalan çitler, alanı parçalara ayırıyor.
- Amaç: Çitleri kaldırarak oluşturulabilecek **en büyük kare alanın** değerini bulmak.
- Eğer kare oluşturulamıyorsa `-1` döndürülür.
- Sonuç `10^9 + 7` modunda istenir.

---

## 🧠 Temel Fikir

Bir **kare alan** oluşturabilmek için:
- Yatayda bir boşluk (gap)
- Dikeyde **aynı uzunlukta** bir boşluk gerekir

📌 Yani:
```python
kare kenarı = ortak yatay boşluk ∩ dikey boşluk
```
**En büyük kare için:**
- maksimum ortak boşluk

---

## 🧱 Sabit Sınır Çitleri

Tarla sınırları da çit kabul edilir:

```python
h = [1] + hFences + [m]
v = [1] + vFences + [n]
```
Bunlar eklenmezse:
- En dıştaki boşluklar hesaplanamaz ❌

### 📐 Tüm Olası Boşlukları Hesaplama
**Yatay Boşluklar**
```python
for i < j:
    gap = h[j] - h[i]
```
**Dikey Boşluklar**
```python
for i < j:
    gap = v[j] - v[i]
```
- Tüm olası mesafeler `set` içinde tutulur
- Aynı uzunluklar otomatik elenir

### 🔗 Ortak Boşlukların Bulunması
```python
common = h_gaps & v_gaps
```
- Eğer **ortak boşluk yoksa:**
```python
return -1
```
- **Varsa:**
```python
side = max(common)
```

#### 🧮 Alan Hesabı
```python
area = side * side
return area % (10^9 + 7)
```

### ⏱️ Zaman ve Alan Karmaşıklığı
- **Zaman:**
- - `O(H² + V²)`
- **Alan:**
- - `O(H² + V²)` (gap setleri)