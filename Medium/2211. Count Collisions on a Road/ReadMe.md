# 2211. Count Collisions on a Road — Explanation & Analysis

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2211](https://leetcode.com/problems/count-collisions-on-a-road/description/)

## 🧩 Problem Summary
Arabalar bir doğrultuda hareket ediyor:

- **'L'** → sola gider  
- **'R'** → sağa gider  
- **'S'** → duruyor  

Her çarpışmadan sonra iki araba **durmuş ('S')** kabul edilir.

Görev: Toplam çarpışma sayısını bulmak.

---

## 💡 Key Insight

### 1️⃣ Soldaki *L* arabaları  
En solda bulunan ve sola giden arabalar **hiçbir şeyle çarpışamaz**, çünkü yollarının solunda araba yok.

→ Bu yüzden **baştaki 'L' karakterlerini yok sayıyoruz**.

---

### 2️⃣ Sağdaki *R* arabaları  
En sağda bulunan ve sağa giden arabalar da **hiçbir şeye çarpmaz**, çünkü yollarının sağında araba yok.

→ Bu yüzden **sondaki 'R' karakterlerini yok sayıyoruz**.

---

### 3️⃣ Orta bölge  
Arada kalan bölge, çarpışmaların olduğu yer.

Bu bölgede:

- Hareket eden **her araba ('L' veya 'R')** mutlaka çarpışacaktır.  
- Çünkü baştaki L'ler ve sondaki R'ler çıkarıldığı için, orta bölgede hareket eden her araç karşısında duracak bir şeye denk gelir.

Bundan dolayı çarpışma sayısı:

Orta bölgede 'S' hariç tüm karakterlerin sayısı

---

## 🔍 Time & Space Complexity
- **Zaman:** O(n)  
- **Bellek:** O(1) — Ekstra dizi yok

Optimal ve temiz çözüm.

---

## ✅ Code (Your Solution)

```python
class Solution(object):
    def countCollisions(self, directions):
        # Step 1: Skip leading 'L'
        i, n = 0, len(directions)
        while i < n and directions[i] == 'L':
            i += 1
        
        # Step 2: Skip trailing 'R'
        j = n - 1
        while j >= 0 and directions[j] == 'R':
            j -= 1
        
        # Step 3: Count all moving cars inside the effective region
        collisions = 0
        for k in range(i, j + 1):
            if directions[k] != 'S':
                collisions += 1
                
        return collisions
```

### 🧠 Why This Works

**Orta bölgede:**

- Her 'R' bir şekilde sola bakan veya duran bir arabaya çarpar.

- Her 'L' bir şekilde sağa bakan veya duran bir arabaya çarpar.

- 'S' ise çarpışma yaratmaz ama diğerleri ona çarpar.

**Bu yüzden:**

- Çarpışmalar = orta bölgede hareket eden arabaların sayısı