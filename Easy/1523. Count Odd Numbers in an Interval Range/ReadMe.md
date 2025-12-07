# 1523. Count Odd Numbers in an Interval Range  

## Difficulty: Easy  
## Problem Link  
[LeetCode - 1518. Water Bottles](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/)  

Amaç:  
`[low, high]` aralığındaki **kaç tane tek sayı** olduğunu bulmak.

---

# 🧠 Core Observation

Bir aralıkta tek sayıları saymanın genel formülü:

### ✔ Eğer hem `low` hem `high` **çift** ise:
```python
count = (high - low) // 2
```

### ✔ Aksi halde:
Aralıkta mutlaka en az bir tek sayı vardır:
```python
count = (high - low) // 2 + 1
```

---

# 🟩 Your Code (Correct & Optimal)

```python
class Solution(object):
    def countOdds(self, low, high):
        return ((high - low) // 2) + (1 if low % 2 == 1 or high % 2 == 1 else 0)
```

### 📌 Why This Works

- Aralıktaki sayıların yarısı tek, yarısı çift gibi dağılır.

- Sınır değerlerden biri bile tekse → teklerin sayısı 1 artar.

### Complexity

- **Time complexity:** `O(1)`

- **Space complexity:** `O(1)`

