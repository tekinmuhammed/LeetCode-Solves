# 🔢 LeetCode 2894 - Divisible and Non-divisible Sums Difference

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2894](https://leetcode.com/problems/divisible-and-non-divisible-sums-difference)

---

## 📘 Problem Description

You are given two integers `n` and `m`.  
- Consider all integers from `1` to `n` (inclusive).
- Separate them into two groups:
  - **Group 1:** Not divisible by `m`
  - **Group 2:** Divisible by `m`

Return the difference between the sum of Group 1 and Group 2:

(sum of numbers not divisible by m) - (sum of numbers divisible by m)

---

## ✅ Example

```python
Input: n = 10, m = 3  
Output: 19

Explanation:
Numbers not divisible by 3: 1, 2, 4, 5, 7, 8, 10 → Sum = 37  
Numbers divisible by 3: 3, 6, 9 → Sum = 18  
Result = 37 - 18 = 19
```

### 💡 Approach

- Initialize two counters: `num1` for non-divisible, `num2` for divisible.

- Iterate `i` from `1` to `n`:

- - If `i % m == 0`, add to `num2`.

- - Else, add to `num1`.

- Return `num1 - num2`.

---

### ⏱️ Complexity

- **Time Complexity:** `O(n)` – One pass through numbers 1 to n.

- **Space Complexity:** `O(1)` – Only two integer accumulators are used.

### 🏷️ Tags

`math`, `simulation`, `basic-loops`, `easy`