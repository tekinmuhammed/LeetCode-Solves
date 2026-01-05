# 1975. Maximum Matrix Sum

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1975](https://leetcode.com/problems/maximum-matrix-sum/description/)

---

## 🧩 Problem Özeti

Bir `matrix` veriliyor.  
İstediğin kadar **işlem** yapabilirsin:

- Bir işlemde, **iki komşu hücrenin işaretini** aynı anda değiştirebilirsin  
  (yani ikisini de `* -1` yaparsın).

🎯 Amaç:
> Tüm bu işlemlerden sonra, **matristeki elemanların toplamını maksimum yapmak**

---

## 🔍 Kritik Gözlem

Bu problemde asıl mesele **işaretlerdir**, konumlar değil.

Önemli noktalar:

1. Mutlak değerlerin toplamı her zaman korunabilir  
   → Çünkü işaretlerle oynuyoruz, değerlerin büyüklüğü değişmiyor
2. Eğer **negatif sayı sayısı çift** ise:
   - Hepsini pozitif yapabiliriz ✅
3. Eğer **negatif sayı sayısı tek** ise:
   - En küçük mutlak değere sahip sayı **negatif kalmak zorunda** ❌

📌 Çünkü:
- Her işlem **iki sayının işaretini** değiştirir
- Yani negatif sayının **paritesi (tek/çift)** değişmez

---

## 💡 Strateji

1. Tüm elemanların **mutlak değerlerini topla**
2. Kaç tane negatif sayı olduğunu say
3. Tüm elemanlar arasındaki **en küçük mutlak değeri** bul
4. Eğer negatif sayısı **tek** ise:
   - Toplamdan `2 × min_abs` çıkar

---

## ✅ Senin Kodun

```python
class Solution(object):
    def maxMatrixSum(self, matrix):
        total = 0
        neg_count = 0
        min_abs = float('inf')
        
        for row in matrix:
            for val in row:
                if val < 0:
                    neg_count += 1
                total += abs(val)
                min_abs = min(min_abs, abs(val))
        
        if neg_count % 2 == 1:
            total -= 2 * min_abs
        
        return total
```

### 🧪 Örnek
**matrix = [[1, -1], [-1, 1]]**
- Mutlak toplam = `1 + 1 + 1 + 1 = 4`
- Negatif sayısı = 2 (çift)
- Hepsi pozitife çevrilebilir
**➡️ Cevap = 4**

**matrix = [[1, -2], [3, -4]]**
- Mutlak toplam = `1 + 2 + 3 + 4 = 10`
- Negatif sayısı = 2 (çift)
**➡️ Cevap = 10**

**matrix = [[-1, 2], [3, 4]]**
- Mutlak toplam = `1 + 2 + 3 + 4 = 10`
- Negatif sayısı = 1 (tek)
- En küçük mutlak değer = 1
**➡️ 10 - 2×1 = 8**

### ⏱️ Karmaşıklık Analizi
- **Zaman:** `O(n × m)` (tüm hücreler bir kez geziliyor)
- **Alan:** `O(1)` (sabit ekstra alan)

