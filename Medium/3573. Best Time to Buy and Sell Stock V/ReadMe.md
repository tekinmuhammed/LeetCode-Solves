# 3573. Best Time to Buy and Sell Stock V

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3573](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/description/)

---

## 🧩 Problem Özeti (Koduna Göre)

Elimizde:
- `prices`: Günlük hisse fiyatları
- `k`: En fazla yapılabilecek **işlem sayısı**
- Her işlem:
  - **Long (al → sat)** veya
  - **Short (sat → al)** olabilir
- Bir işlem **kapatıldıktan sonra aynı gün tekrar işlem başlatılamaz**  
  → *cooldown (gap) kuralı*

🎯 Amaç:  
**En fazla `k` işlemle maksimum kârı elde etmek**

---

## 🧠 Temel Fikir

Bu çözüm:
- Günlük **fiyat farkları** (`diff`)
- **State Machine DP**
- **Long + Short pozisyon**
- **Cooldown (bekleme) durumu**

üzerine kuruludur.

---

## 📉 Fiyat Farkları Yaklaşımı
```python
diff = [prices[i+1] - prices[i] for i in range(n-1)]
```
Her gün için:

- Long pozisyon → `+v`

- Short pozisyon → `-v`

Bu yaklaşım:

- Al/sat anlarını gün bazında değil,

- **hareket bazında** modellemeyi sağlar.

### 🔁 DP Durumları (State’ler)
Her `j` (yapılan işlem sayısı) için **4 ayrı durum** tutulur:

**1️⃣ `free[j]`**
> j işlem tamamlandı, **boşta**, yeni işleme başlayabilir

**2️⃣ `cool[j]`**
> j işlem tamamlandı, **işlem yeni kapandı, bir sonraki adımda işlem açılamaz**

**3️⃣ `hold_n[j]`**
> j. işlem içindeyiz, **Long (normal) pozisyon**

**4️⃣ `hold_s[j]`**
> j. işlem içindeyiz, **Short pozisyon**

### 🧮 Başlangıç Durumu
```python
free[0] = 0
diğer tüm durumlar = -∞
```
📌 Henüz işlem yok, kâr 0.

### 🔄 Günlük DP Geçişleri
Her fiyat farkı `v` için:

### 📈 Long Pozisyon (hold_n)
```python
new_hold_n[j] = max(
    hold_n[j] + v,      # pozisyonu sürdür
    free[j-1] + v       # yeni long başlat
)
```

### 📉 Short Pozisyon (hold_s)
```python
new_hold_s[j] = max(
    hold_s[j] - v,      # shortu sürdür
    free[j-1] - v       # yeni short başlat
)
```
📌 Fiyat düşerse short kâr getirir.

### ❌ İşlem Kapatma → Cooldown
```python
close_normal = max(hold_n[j], free[j-1]) + v
close_short  = max(hold_s[j], free[j-1]) - v

new_cool[j] = max(close_normal, close_short)
```
📌 İşlem kapatılınca:
- Aynı gün tekrar işlem açılamaz
- `cool` durumuna geçilir

### 🆓 Cooldown → Free
```python
new_free[j] = max(free[j], cool[j])
```
📌 Bir gün bekledikten sonra tekrar serbest oluruz.

### 🏁 Sonuç Hesabı
```python
return max(max(free), max(cool))
```
✔️ Son gün:
- Ya tamamen boşta
- Ya da işlemi yeni kapatmış olabiliriz

### ⏱️ Zaman & Alan Karmaşıklığı
- **Zaman:** `O(n × k)`

- **Alan:** `O(k)`