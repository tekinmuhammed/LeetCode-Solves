# 🏦 LeetCode 1716. Calculate Money in Leetcode Bank  

**Difficulty:** Easy  
**Tags:** Math, Simulation  

---

## 💡 Problem Description  
Herkesin hayalindeki banka: **Leetcode Bank** 💰  

Her hafta pazartesi günü yatırılan para 1 artar, ve hafta boyunca her gün önceki günden 1 fazla para yatırılır.  

- 1. haftanın pazartesi günü 1$, salı günü 2$, … pazar günü 7$ yatırılır.  
- 2. haftanın pazartesi günü 2$, salı günü 3$, … pazar günü 8$ yatırılır.  
- Bu şekilde devam eder.  

Verilen `n` gün boyunca yatırılan toplam parayı hesaplayın.

---

## 🧠 Approach  
1. Haftaları sırayla simüle ederiz.  
2. Her haftanın **pazartesi günü yatırılacak miktar** `current_monday` değişkeni ile tutulur.  
3. Her hafta 7 gün sürer, fakat son hafta 7 günden az olabilir.  
4. Her gün yatırılan miktar bir önceki günden 1 fazla olacak şekilde toplanır.  
5. Her hafta sonunda `current_monday` değeri 1 artırılır ve kalan gün sayısı (`n`) 7 azaltılır.  

---

## 🧩 Example  
**Input:**  
```python
n = 10

**Process:**  
- 1. hafta: 1 + 2 + 3 + 4 + 5 + 6 + 7 = **28**  
- 2. hafta: 2 + 3 + 4 = **9**  
**Total = 28 + 9 = 37**

**Output:**  
37
```

---

## 🧮 Time & Space Complexity  
| Complexity | Description |
|-------------|-------------|
| ⏱ **Time:** O(n) | Her gün için sabit işlem yapılır |
| 💾 **Space:** O(1) | Ekstra alan kullanılmaz |

---

## 🧰 Code Implementation  

```python
class Solution(object):
    def totalMoney(self, n):
        total = 0
        current_monday = 1
        
        while n > 0:
            daily = current_monday
            for _ in range(min(7, n)):
                total += daily
                daily += 1
            current_monday += 1
            n -= 7
        
        return total
```

### ✅ Example Runs
| Input    | Output | Explanation                  |
| -------- | ------ | ---------------------------- |
| `n = 4`  | `10`   | (1 + 2 + 3 + 4)              |
| `n = 10` | `37`   | 28 (1. hafta) + 9 (2. hafta) |
| `n = 20` | `96`   | 28 + 35 + 33                 |


### 🏁 Summary
✔ Basit döngü tabanlı simülasyon
✔ Her hafta yatırılan tutar artarak ilerler
✔ Formülize edilmeden kolayca anlaşılır