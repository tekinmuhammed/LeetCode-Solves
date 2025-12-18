# 3652. Best Time to Buy and Sell Stock using Strategy

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3652](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/description/)

---

## 🧩 Problem Özeti (Koduna Göre)

Elimizde:
- `prices[i]`: i. günkü hisse fiyatı
- `strategy[i]`:
  - `0` → **hold** (tut)
  - `1` → **sell** (sat)
- `k`: Uzunluğu `k` olan **tek bir pencere** seçip stratejiyi değiştirme hakkımız var

### 🔁 Değişiklik Kuralı
Seçilen pencere `[l, r)` (uzunluk `k`) için:
- İlk `k/2` gün → **hold (0)**
- Son `k/2` gün → **sell (1)**

🎯 Amaç:  
Bu değişikliği **en iyi yerde** yaparak toplam kârı **maksimize etmek**.

---

## 🧠 Genel Yaklaşım

Çözüm 3 ana adımdan oluşur:

1. **Mevcut stratejiyle oluşan temel kârı hesapla**
2. Strateji değişirse **kârda oluşacak farkları (delta)** hesapla
3. Uzunluğu `k` olan **sliding window** ile en yüksek ek kazancı bul

---

## 1️⃣ Mevcut (Base) Kâr

```python
base_profit = sum(strategy[i] * prices[i] for i in range(n))
```
📌 Sadece `sell (1)` olan günler kâr üretir.

### 2️⃣ Strateji Değişikliğinin Etkisi (Delta Mantığı)
Pencere içine giren her gün için:

**🔹 Hold’a Çevirmek (0)**
```python
to_hold[i] = -(strategy[i] * prices[i])
```
- Eğer o gün zaten `sell` ise → kâr kaybı

- Eğer `hold` ise → değişim yok

**🔹 Sell’e Çevirmek (1)**
```python
to_sell[i] = (1 - strategy[i]) * prices[i]
```
- Eğer o gün `hold` ise → ek kâr

- Eğer zaten `sell` ise → değişim yok

**3️⃣ Prefix Sum ile Hızlandırma**
```python
prefix_hold[i] = to_hold[0] + ... + to_hold[i-1]
prefix_sell[i] = to_sell[0] + ... + to_sell[i-1]
```
📌 Böylece herhangi bir aralıktaki kazancı **O(1)** sürede hesaplarız.

**4️⃣ Sliding Window (Boyut = k)**
Her pencere için:
```text
[l ........ mid ........ r)
|-- hold --|--- sell ---|
```
- `mid = l + k//2`

- İlk yarı → **hold**

- İkinci yarı → **sell**

**🧮 Pencere Kazancı**
```python
gain_hold = prefix_hold[mid] - prefix_hold[l]
gain_sell = prefix_sell[r] - prefix_sell[mid]
total_gain = gain_hold + gain_sell
```
Tüm pencereler denenir ve **maksimum ek kazanç** bulunur.

**🏁 Nihai Sonuç**
```python
return base_profit + max_gain
```
✔️ En iyi pencere seçilerek toplam kâr maksimize edilir.

### ⏱️ Zaman & Alan Karmaşıklığı
- **Zaman:** `O(n)`

- **Alan:** `O(n)`