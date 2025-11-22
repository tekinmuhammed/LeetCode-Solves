# 3190. Find Minimum Operations to Make All Elements Divisible by Three  
### ✔️ Explanation & Analysis (Markdown Format)

**Difficulty:** Easy  
**Problem Link:** [LeetCode 3190](https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/)

## 📝 Problem Summary
Elimizde bir sayı listesi var. Her sayı üzerinde **en fazla 1 işlem** yapılabiliyor:  
- ya **1 ekle**,  
- ya **1 çıkar**  

**Amaç:**  
Tüm elemanları **3’e tam bölünebilir hâle getirmek** için gereken minimum işlem sayısını bulmak.

**Önemli gözlem:**  
Bir sayı zaten `x % 3 == 0` ise → işlem gerekmez.  
Bir sayı `1 mod 3` veya `2 mod 3` ise → her zaman **tek işlem** ile mod 0 yapılabilir.

Yani çözüm:  
`3'e bölünemeyen her sayı 1 işlem gerektirir.`

---

## 💡 Kodun Mantığı
```python
class Solution(object):
    def minimumOperations(self, nums):
        operations = 0
        for x in nums:
            if x % 3 != 0:
                operations += 1
        return operations
```

### ✔️ Doğruluk

- Tamamen doğru.

**Çünkü:**

| x % 3 | İşlem   | Sebep             |
| ----- | ------- | ----------------- |
| 0     | 0 işlem | zaten bölünüyor   |
| 1     | 1 işlem | 1 çıkar → 0 mod 3 |
| 2     | 1 işlem | 1 ekle → 3 olur   |

## ⏱️ Complexity

**Time:** `O(n)`

**Space:** `O(1)`