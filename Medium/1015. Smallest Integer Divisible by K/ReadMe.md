# 1015. Smallest Integer Divisible by K  
### ✔️ Explanation & Analysis

## 📝 Problem Summary
Sadece `1` rakamından oluşan (111..., repunit) en küçük sayıyı bulmamız isteniyor; bu sayı verilen `K` değerine tam bölünmeli.

Örneğin:  
- K = 3 → 111 % 3 = 0 → cevap 3  
- K = 7 → 111111 % 7 = 0 → cevap 6  

Ancak bazı K değerleri için **hiçbir repunit bölünemez** → özellikle **2 veya 5’e bölünebilen sayılar**.

---

## 💡 Temel Matematik Fikri

Bir repunit şu şekilde increment edilir:
```python
1 → remainder = 1 % k
11 → remainder = (110 + 1) % k
111 → remainder = ((110 + 1)*10 + 1) % k
```
...

Her adımda sayıyı büyütmeden sadece **mod değerini güncelliyoruz**:
```python
remainder = (remainder * 10 + 1) % k
```

❗ Eğer `remainder == 0` ise;  
repunit tam bölündü → uzunluğu cevaptır.

---

## 🚫 Neden k % 2 == 0 veya k % 5 == 0 ise imkansız?
Çünkü sadece 1’lerden oluşan hiçbir sayı;

- Çift olamaz → **2’ye bölünemez**
- Sonu 1 olduğundan → **5’e bölünemez**

Bu durumda cevap **-1**.

---

## ✔️ Senin Kodun
```python
class Solution(object):
    def smallestRepunitDivByK(self, k):
        # If k is divisible by 2 or 5, no repunit will ever be divisible by it.
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length
        
        return -1
```

### 🔍 Kod Analizi

- `k % 2 == 0 or k % 5 == 0` → erken çıkış, doğru.

- Mod yöntemi → overflow riskini yok eder.

- Döngüyü `1..k` arasında sınırlamak doğru, çünkü mod tekrarlandığında döngü kapanır.

- İlk remainder sıfır olduğunda uzunluk bulundu → doğru.

- 💡 Yani çözüm **optimal**, zaman ve hafıza açısından en verimli çözüm sınıfında.

### ⏱️ Complexity

- **Time:** `O(k)`

- **Space:** `O(1)`