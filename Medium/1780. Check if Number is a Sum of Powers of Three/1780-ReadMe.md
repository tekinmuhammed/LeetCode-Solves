# 🔢 LeetCode 1780 - Check if Number is a Sum of Powers of Three

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1780](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three)

---

## 📘 Problem Description

Given an integer `n`, return `true` if it is possible to represent `n` as the sum of **distinct** powers of three. Otherwise, return `false`.

A number is a sum of distinct powers of three if it can be written as:

`3^0 + 3^1 + 3^2 + ... + 3^k`

with each power used **at most once**.

---

## 🧪 Example

### Input:
```python
n = 91
```

### Output:
```python
True
```

### Explanation:


- 91 = 3^0 + 3^2 + 3^4

### 🚀 Approach

This is equivalent to checking whether the number `n` can be represented in base-3 without using the digit `2`.

**Why?**

Each digit in base-3 can only be 0, 1, or 2. Since we're only allowed to use each power of 3 **once**, any digit `2` would mean we need to use the same power twice — which is not allowed.

So we simply divide `n` by 3 repeatedly and check the remainder:

- If any remainder is `2`, return `False`

- If we reduce `n` to 0 without encountering `2`, return `True`

### ⏱️ Complexity

- **Time Complexity:** `O(log₃(n))` → because we divide `n` by 3 each time.

- **Space Complexity:** `O(1)`

### 🏷️ Tags

`math`, `greedy`, `base-conversion`, `leetcode-medium`