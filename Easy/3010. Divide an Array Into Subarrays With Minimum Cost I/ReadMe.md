## 3010. Divide an Array Into Subarrays With Minimum Cost I

**Difficulty:** Easy  
**Link:** [LeetCode 3010](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description/)  

---

### Problem Özeti

- `nums` dizisi veriliyor
- Diziyi **3 elemanlık bir alt diziye** ayırıyoruz
- **Maliyet tanımı**:
  - Seçilen 3 elemanın **toplamı**
- Ama bir kural var:
  - İlk eleman **mutlaka `nums[0]` olmalı**
- Amaç:
  - **Toplam maliyeti minimum yapmak**

---

## Senin Çözümünün Temel Mantığı 🎯

Bu problem aslında şu soruya indirgeniyor:

> `nums[0]` sabitken, geri kalan elemanlardan **en küçük 2 tanesini** seç.

---

## Adım Adım İnceleyelim 🔍

### 1️⃣ İlk Elemanı Sabitle

```python
nums[0]
```
Problem gereği bu eleman **her zaman seçilmek zorunda.**

### 2️⃣ Geri Kalan Elemanları Ayır
```python
rest = nums[1:]
```
Artık amacımız:
> `rest` içinden **en küçük 2 sayıyı** bulmak

### 3️⃣ Sırala
```python
rest.sort()
```
Sıralama sonrası:
- `rest[0]` → en küçük
- `rest[1]` → ikinci en küçük

### 4️⃣ Minimum Toplamı Hesapla
```python
return nums[0] + rest[0] + rest[1]
```
Bu seçim:
- Kurallara uygun
- Matematiksel olarak **en küçük mümkün toplam**

### Örnek Üzerinden 🎯
nums = [1, 2, 3, 4]
nums[0] = 1

rest = [2, 3, 4]

En küçük iki sayı: 2 ve 3

➡️ Sonuç:

1 + 2 + 3 = 6
Zaman & Alan Karmaşıklığı ⏱️
Time: O(n log n) (sıralama)

Space: O(n) (rest dizisi)