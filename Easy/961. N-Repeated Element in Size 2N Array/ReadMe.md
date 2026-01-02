# 961. N-Repeated Element in Size 2N Array

**Difficulty:** Easy  
**Link:** [LeetCode 961](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/)

---

## 🧩 Problem Özeti

Uzunluğu **2N** olan bir dizi veriliyor.

📌 Özellik:
- Dizide **tek bir sayı N kez tekrar eder**
- Diğer **N sayı yalnızca 1 kez** görünür

🎯 Amaç:
> **N kez tekrar eden sayıyı** bulup döndürmek.

---

## 💡 Temel Fikir

- İlk tekrar eden elemanı bulmak yeterlidir
- Çünkü **sadece bir sayı tekrar eder**
- Set kullanarak daha önce görülüp görülmediğini kontrol edebiliriz

---

## ✅ Senin Çözümün

```python
class Solution(object):
    def repeatedNTimes(self, nums):
        seen = set()
        
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
```

## 🔍 Adım Adım Açıklama
### 1️⃣ Set ile Takip
```python
seen = set()
```
- Daha önce görülen elemanları saklar
- Arama işlemi **O(1)**

### 2️⃣ Dizi Üzerinde Dolaşma
```python
for num in nums:
```
- Elemanlar sırayla incelenir

### 3️⃣ Tekrar Kontrolü
```python
if num in seen:
    return num
```
- Aynı sayı ikinci kez görüldüğünde
- Bu sayı **N kez tekrar eden** elemandır

### 4️⃣ İlk Görülüyorsa Ekle
```python
seen.add(num)
```

### 🧪 Örnek
**Girdi**
```python
nums = [5,1,5,2,5,3,5,4]
```
İşleyiş
- 5 → ekle
- 1 → ekle
- 5 → **daha önce görüldü → return 5**

### ⏱️ Karmaşıklık Analizi
- **🧮 Zaman**
- - Tek geçiş
    👉 **O(n)**
- **🧠 Alan**
- - Set en fazla N+1 eleman tutar
    👉 **O(n)**

