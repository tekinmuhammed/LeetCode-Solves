# 1262. Greatest Sum Divisible by Three

**Difficulty:** Medium
**Problem Link:** [LeetCode 1262](https://leetcode.com/problems/greatest-sum-divisible-by-three/description/)

## 📝 Problem Summary
Bir sayı listesinden seçtiğimiz elemanların toplamının **3’e tam bölünebilir** olmasını istiyoruz.  
Amaç:  
➡️ **Toplamı maksimum** yap.

Doğal yaklaşım:  
1. Tüm sayıların toplamını al (`total`)  
2. Eğer `total % 3 == 0` → zaten en büyük toplam budur  
3. Eğer değilse toplamı 3’e bölünebilir yapmak için **minimum değeri feda etmeliyiz**

---

## 🔍 Önemli Gözlem
Bir sayının mod 3 durumu:

| Remainder | Açıklama |
|----------|----------|
| 0 | etkisiz |
| 1 | toplamdan çıkarılırsa mod 1 azaltır |
| 2 | toplamdan çıkarılırsa mod 2 azaltır |

Toplamın mod 3 durumuna göre hareket edilir:

### **total % 3 == 1**
Toplamdan çıkarmak için iki seçenek:

1. **Tek bir remainder-1 sayı çıkar** (en küçüğü)
2. **İki tane remainder-2 sayı çıkar** (en küçüğü iki tanesi)

### **total % 3 == 2**
Aynı mantığın tersi:

1. **Tek bir remainder-2 sayı çıkar** (en küçüğü)
2. **İki tane remainder-1 sayı çıkar** (en küçüğü iki tanesi)

Amaç → toplamdan en küçük kaybı yapıp mod 0 yapmak.

---

## 💡 Kodun Mantığı (Senin Çözümünde)
```python
class Solution(object):
    def maxSumDivThree(self, nums):
        total = sum(nums)

        # smallest numbers with remainder 1 and 2
        r1 = []
        r2 = []

        for x in nums:
            if x % 3 == 1:
                r1.append(x)
            elif x % 3 == 2:
                r2.append(x)

        r1.sort()
        r2.sort()

        if total % 3 == 0:
            return total

        # Case remainder 1
        if total % 3 == 1:
            option1 = r1[0] if len(r1) >= 1 else float('inf')
            option2 = sum(r2[:2]) if len(r2) >= 2 else float('inf')
            return total - min(option1, option2)

        # Case remainder 2
        if total % 3 == 2:
            option1 = r2[0] if len(r2) >= 1 else float('inf')
            option2 = sum(r1[:2]) if len(r1) >= 2 else float('inf')
            return total - min(option1, option2)
```

### ✔️ Doğruluk

Çözüm **optimal ve tamamen doğru**.
LeetCode'un resmi editorial yaklaşımıyla **aynı yöntemi** kullanıyorsun:

- Mod gruplarını ayırma

- En küçük kaybı bulma

- Toplamdan çıkarma

### ⏱️ Complexity

- **Time:** `O(n log n)` (sort yüzünden)

- **Space:** `O(n)`

Daha da optimize edilmek istenirse sort yerine sadece **en küçük 2 elemanı takip ederek**
`O(n)` space + time yapılabilir.