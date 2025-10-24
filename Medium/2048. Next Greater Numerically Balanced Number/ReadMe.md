# 🧩 LeetCode 2048. Next Greater Numerically Balanced Number  

**Difficulty:** Medium
**Link:** [LeetCode 2048](https://leetcode.com/problems/next-greater-numerically-balanced-number/description/)  

**Difficulty:** Medium   

---

## 💡 Problem Description  
A **numerically balanced number** is a positive integer such that for every digit `d` in the number, the digit `d` appears **exactly `d` times**.  

For example:  
- `22` is balanced because the digit `2` appears **2 times**.  
- `1333` is balanced because `1` appears **1 time** and `3` appears **3 times**.  

Given an integer `n`, return the **smallest numerically balanced number** that is **strictly greater than `n`**.

---

## 🧠 Approach  
1. Start checking numbers beginning from `n + 1`.  
2. For each number, determine if it is **numerically balanced** by counting how many times each digit occurs.  
3. To verify balance:  
   - The digit `0` can never appear in a balanced number (since it should appear `0` times).  
   - For each digit `d` (1–9), if `d` appears in the number, it must appear **exactly `d` times**.  
4. Once a balanced number is found, return it immediately.  

Given the constraint (`n ≤ 10^6`), this **brute-force** approach works efficiently because numerically balanced numbers are sparse and small.

---

## 🧩 Example  
**Input:**
```python
n = 1200

**Process:**  
Check sequentially:  
- 1201 ❌ (not balanced)  
- 122 ❌  
- 1333 ✅  

**Output:**  
1333
```

---

## 🧮 Time & Space Complexity  

| Complexity | Description |
|-------------|-------------|
| ⏱ **Time:** `O(k × m)` | `k`: number of numbers checked, `m`: number of digits |
| 💾 **Space:** `O(1)` | Uses a fixed-size digit count array |

---

## 🧰 Code Implementation  

```python
class Solution:
    def isBalance(self, num: int) -> bool:
        count = [0] * 10
        temp = num

        while temp > 0:
            digit = temp % 10
            if digit == 0:
                return False
            count[digit] += 1
            temp //= 10

        for d in range(1, 10):
            if count[d] > 0 and count[d] != d:
                return False
        return True

    def nextBeautifulNumber(self, n: int) -> int:
        num = n + 1
        while True:
            if self.isBalance(num):
                return num
            num += 1
```

### ✅ Example Runs
| Input      | Output | Explanation                           |
| ---------- | ------ | ------------------------------------- |
| `n = 1`    | `22`   | Smallest balanced number > 1          |
| `n = 1000` | `1333` | 1 appears once, 3 appears three times |
| `n = 3000` | `3133` | 1 appears once, 3 appears three times |


### 🏁 Summary
✔ Simple brute-force approach
✔ Works efficiently due to small input range
✔ Uses digit frequency matching rule cleanly

### Tags
`LeetCode-Medium`, `Math`, `Brute-Force`, `Simulation` 