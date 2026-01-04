# 1390. Four Divisors

**Difficulty:** Medium  
**Link:** [LeetCode 1390](https://leetcode.com/problems/four-divisors/description/)

---

## 🧩 Problem Özeti

Bir `nums` dizisi veriliyor.

Bir sayı **tam olarak 4 pozitif böleni** varsa:
- Bu 4 bölenin **toplamını** al
- Tüm sayılar için bu toplamları **genel sonuca ekle**

🎯 Amaç:
> Dizideki tüm sayılar için, **4 böleni olanların bölen toplamlarının toplamını** döndürmek

---

## 🔍 Temel Gözlem

Bir sayının **tam olarak 4 böleni** olması için yapı genellikle şudur:

- **p³** (p asal) → bölenler: `1, p, p², p³`
- **p × q** (p ve q farklı asal) → bölenler: `1, p, q, p×q`

Ama sen çözümünde bu matematiksel ayrımı yapmadan,
👉 **kareköküne kadar bölen sayarak** genel ve güvenli bir yöntem kullanmışsın.

---

## 💡 Yaklaşımın (Brute Force + Optimizasyon)

Her `num` için:

1. `1`’den `√num`’a kadar döngü
2. Eğer `i`, `num`’u bölüyorsa:
   - `i` ve `num // i` bölen olarak sayılır
3. Eğer `i * i == num` ise (kare kök durumu):
   - Tek bölen eklenir
4. Bölen sayısı **4’ü geçerse**, erken çıkılır (optimizasyon)
5. Döngü sonunda:
   - Eğer bölen sayısı **tam olarak 4** ise → bölenlerin toplamı eklenir

---

## ✅ Senin Kodun

```python
import math

class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        total_sum = 0
        
        for num in nums:
            # Bölen sayısını ve toplamını tutacak değişkenler
            count = 0
            div_sum = 0
            
            # 1'den sayının kareköküne kadar (karekök dahil) kontrol et
            limit = int(math.sqrt(num))
            
            for i in range(1, limit + 1):
                if num % i == 0:
                    # i bir bölendir.
                    # Eğer i tam karekök ise (örn: num=4, i=2), sadece 1 bölen sayılır.
                    if i * i == num:
                        count += 1
                        div_sum += i
                    else:
                        # Değilse, hem i hem de num/i bölendir.
                        count += 2
                        div_sum += (i + (num // i))
                    
                    # Optimizasyon: Eğer bölen sayısı 4'ü geçerse, dur
                    if count > 4:
                        break
            
            # Eğer tam olarak 4 böleni varsa, toplamı ekle
            if count == 4:
                total_sum += div_sum
                
        return total_sum
```

### 🧪 Örnek
**nums = [21, 4, 7]**
- **21** → bölenler: `1, 3, 7, 21` → toplam = **32** ✅
- **4** → bölenler: `1, 2, 4` → ❌
- **7** → bölenler: `1, 7` → ❌
**➡️ Sonuç = 32**

### ⏱️ Karmaşıklık Analizi
- **🧮 Zaman**
- - Her sayı için: `O(√num)`
- - Maksimum `num ≤ 10⁵` olduğu için yeterince hızlı

- **🧠 Alan**
- - Sadece birkaç değişken
- - **O(1)** ek alan