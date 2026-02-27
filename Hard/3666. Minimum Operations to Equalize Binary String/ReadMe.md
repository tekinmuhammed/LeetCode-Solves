# 3666. Minimum Operations to Equalize Binary String

**Difficulty:** Hard
**Link:** [LeetCode 3666](https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/description/)

---

## Problem Özeti

Binary bir string `s` ve bir tam sayı `k` veriliyor.

Bir işlemde:
- **Uzunluğu `k` olan bir alt string** seçiliyor
- Bu alt string içindeki **tüm bitler tersine çevriliyor** (`0 ↔ 1`)

Amaç:
- String’i **tamamen aynı bitlerden** (hepsi `0` veya hepsi `1`) oluşur hale getirmek
- Bunu **minimum işlem sayısıyla** yapmak
- Eğer mümkün değilse `-1` döndürmek

---

## Temel Gözlemler

### 1️⃣ Hiç `0` yoksa
Zaten tüm bitler `1`:
```
→ 0 işlem
```

---

### 2️⃣ `k == n` (tüm string tek hamlede çevrilebiliyorsa)
- Eğer tüm string `0` ise → **1 işlem**
- Aksi halde → **imkansız**
```
Çünkü karışık bir string tek hamlede eşitlenemez
```

---

### 3️⃣ Parite (Tek–Çift) Kritik Noktası

Bir işlem:
- `k` tane bitin değerini değiştirir

Toplam `m` işlem sonrası:
- Değiştirilen bit sayısı = `m × k`

Bu sayı:
- **çift** ise → toplam `0` sayısının paritesi değişmez
- **tek** ise → parite değişir

Buradan şu sonuç çıkar:

- `k` **çift** ise → `m × k` **her zaman çift**
  - O zaman `0` sayısı **tek olamaz**
- `k` **tek** ise → `m`’nin tek/çift olması sonucu belirler

Bu yüzden bazı durumlar **doğrudan imkansızdır**.

---

## Matematiksel Yaklaşım (O(1))

Bu problem aslında bir **formülasyon problemi**.

Amaç:
- Gerekli minimum `m` (işlem sayısı) değerini bulmak

Bunun için iki zorunluluk var:

### Zorunluluk 1: Yeterli bit çevrilebilmeli
- `m × k ≥ cnt_0`  (0’ları 1’e çevirmek için)
- `m × (n - k) ≥ (n - cnt_0)` (1’leri 0’a çevirmek için)

Bu yüzden:
```
m ≥ ceil(cnt_0 / k)
m ≥ ceil((n - cnt_0) / (n - k))
```

---

### Zorunluluk 2: Parite uyumu
- `k` tek/çift olmasına göre `m` tek mi çift mi olmalı kontrol edilir

---

## Kod

```python
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        cnt_0 = s.count('0')
        
        # 1) Hiç 0 yoksa
        if cnt_0 == 0:
            return 0
            
        # 2) k == n durumu
        if k == n:
            return 1 if cnt_0 == n else -1
                
        # 3) k çift & cnt_0 tek → imkansız
        if k % 2 == 0 and cnt_0 % 2 != 0:
            return -1
            
        if k % 2 == 1:
            # k tek
            if cnt_0 % 2 == 0:
                # m çift olmalı
                m = max((cnt_0 + k - 1) // k,
                        (cnt_0 + (n - k) - 1) // (n - k))
                if m % 2 != 0:
                    m += 1
                return m
            else:
                # m tek olmalı
                m = max((cnt_0 + k - 1) // k,
                        ((n - cnt_0) + (n - k) - 1) // (n - k))
                if m % 2 == 0:
                    m += 1
                return m
        else:
            # k çift
            m_even = max((cnt_0 + k - 1) // k,
                         (cnt_0 + (n - k) - 1) // (n - k))
            if m_even % 2 != 0:
                m_even += 1
                
            m_odd = max((cnt_0 + k - 1) // k,
                        ((n - cnt_0) + (n - k) - 1) // (n - k))
            if m_odd % 2 == 0:
                m_odd += 1
                
            return min(m_even, m_odd)
```

---

## Zaman ve Alan Karmaşıklığı

- **Zaman:** `O(n)` (sadece `count`)
- **Alan:** `O(1)`

---

## Neden Bu Çözüm Zor?

Bu soru:
- Greedy
- Sliding window
- DP **değil**

Tamamen:
- **Parity (tek–çift)**
- **Matematiksel alt sınırlar**
- **Formül türetme**

üzerine kurulu.

Bu yüzden “thinking problem” kategorisinde ve zorlayıcı.

---

## Özet

Bu çözüm:

✔ Simülasyon yapmaz  
✔ Doğrudan matematikle çözer  
✔ O(1) formül yaklaşımı içerir  
✔ Parite analizini doğru kullanır  

Gerçekten ileri seviye bir problem ve çözüm 👏  

Hazırsan 👉 sıradaki soruya geçelim 🚀