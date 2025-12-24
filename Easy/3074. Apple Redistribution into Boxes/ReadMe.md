# 3074. Apple Redistribution into Boxes

**Difficulty:** Easy  
**Problem Link:** [LeetCode 3074](https://leetcode.com/problems/apple-redistribution-into-boxes/description/)

---

## 🧩 Problem Özeti

- `apple[i]`: i. tür elmanın **adet sayısı**
- `capacity[j]`: j. kutunun **taşıma kapasitesi**
- Amaç:  
  👉 **Tüm elmaları yerleştirmek için gereken minimum kutu sayısını** bulmak

📌 Kutular **birleştirilebilir**, yani hangi elmanın hangi kutuya girdiği önemli değil.  
Önemli olan **toplam kapasitenin**, toplam elma sayısını karşılaması.

---

## 🧠 Temel Fikir (Greedy)

Bu problem saf bir **greedy (açgözlü)** problemidir.

### Mantık:
- Önce **toplam elma sayısını** bul
- Kutuları **kapasitelerine göre büyükten küçüğe sırala**
- En büyük kapasiteli kutulardan başlayarak elma yerleştir
- Toplam kapasite, toplam elmayı karşıladığı anda dur

👉 En büyük kutuları önce kullanmak, **kutu sayısını minimize eder**.

---

## 🔍 Kodunun Adım Adım Açıklaması

---

### 1️⃣ Toplam Elma Sayısını Hesapla
```python
total_apples = sum(apple)
```
Artık hedefimiz şu:
> Kapasitelerin toplamı ≥ `total_apples`

### 2️⃣ Kutuları Büyükten Küçüğe Sırala
```python
capacity.sort(reverse=True)
```
📌 Neden?
- Büyük kutular daha fazla elma taşır
- Daha az kutu kullanmamızı sağlar

### 3️⃣ Greedy Toplama
```python
curr = 0
count = 0
```
- `curr`: şu ana kadar toplanan toplam kapasite
- `count`: kullanılan kutu sayısı

### 4️⃣ Kutuları Tek Tek Kullan
```python
for cap in capacity:
    curr += cap
    count += 1
    if curr >= total_apples:
        return count
```
- Her adımda:
- - Kutuyu ekle
- - Kutu sayısını artır
- **Toplam kapasite yeterliyse hemen dur ⛔**

### 🏁 Sonuç
Fonksiyon:
- **Tüm elmaları yerleştirmek için gereken minimum kutu sayısını döndürür.**

### ⏱️ Zaman ve Alan Karmaşıklığı

- **Zaman:**
- - Sıralama → `O(n log n)`
- - Tek geçiş → `O(n)`
- - Toplam: `O(n log n)`

- **Alan:**
- - Ekstra sabit değişkenler → `O(1)`

### 🧪 Örnek
```python
apple = [1, 3, 2]
capacity = [4, 3, 1, 5]
```
- Toplam elma = `6`
- Kapasiteler (sıralı) = `[5, 4, 3, 1]`

**Adımlar:**
- 5 → yetmedi
- 5 + 4 = 9 ✅
**➡️ Cevap: 2**