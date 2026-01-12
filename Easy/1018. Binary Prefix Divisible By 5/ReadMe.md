# 1018. Binary Prefix Divisible By 5

**Difficulty:** Easy
**Link:** [LeetCode 1018](https://leetcode.com/problems/binary-prefix-divisible-by-5/description/)

---

## 📝 Problem Summary
Binary (ikilik) bir dizinin prefix’lerini, yani soldan başlayarak oluşan her sayıyı kontrol ediyoruz.  
Her prefix’in **5’e bölünüp bölünmediğini** bir liste olarak döndürmemiz gerekiyor.

Örneğin `nums = [1,0,1]`  
- Prefix 1   → 1 (bölünmez)  
- Prefix 10  → 2 (bölünmez)  
- Prefix 101 → 5 (bölünür)  

---

## 💡 Çözüm Mantığı
Binary bir sayıyı her yeni bit geldiğinde genişletebilirsin:
```python
current = current * 2 + bit
```

Ama sayı çok büyüyebilir.  
**Sadece mod 5 değerine ihtiyacımız olduğundan:**
```python
current = (current * 2 + bit) % 5
```

→ Böylece sayı hiç büyümez, her zaman 0–4 aralığında kalır.  
→ `current == 0` ise prefix 5’e tam bölünüyor demektir.

---

## ✔️ Senin Kodun
```python
class Solution(object):
    def prefixesDivBy5(self, nums):
        result = []
        current = 0
        
        for bit in nums:
            # keep prefix mod 5 only
            current = (current * 2 + bit) % 5
            result.append(current == 0)
        
        return result
```

### 🔍 Kod Analizi

- `current` → prefix mod 5 değeri

- Her bit geldikçe binary sayı genişletilir

- Mod korunur

- Sonuç listesi boolean değerler içerir

    Minimal, optimal, temiz. 👌

### ⏱️ Complexity

- **Time:** `O(n)`

- **Space:** `O(1)` (sonuç hariç)