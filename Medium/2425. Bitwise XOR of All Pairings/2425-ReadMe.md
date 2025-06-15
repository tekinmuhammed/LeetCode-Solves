# 🔀 LeetCode 2425 - Bitwise XOR of All Pairings

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2425](https://leetcode.com/problems/bitwise-xor-of-all-pairings)

---

## 📘 Problem Description

Given two integer arrays `nums1` and `nums2`, return the **bitwise XOR of all pairings** `(a, b)` such that:

- `a` is an element from `nums1`
- `b` is an element from `nums2`

Each pairing computes `a ^ b`, and you take the XOR of all such results.

---

## 🧪 Example

### Input:
```python
nums1 = [2, 1, 3]
nums2 = [10, 2]
```

### Output:
`2`

### Explanation:

All pairings and their XORs:

- 2 ^ 10 = 8

- 2 ^ 2 = 0

- 1 ^ 10 = 11

- 1 ^ 2 = 3

- 3 ^ 10 = 9

- 3 ^ 2 = 1

Now XOR all results: 8 ^ 0 ^ 11 ^ 3 ^ 9 ^ 1 = 2 ✅

### 🧠 Optimized Insight

Instead of calculating all pairings explicitly (which is `O(n * m)`), we can use a mathematical property of XOR:

> The total XOR of all pairings `(a ^ b)` is equal to:
>
> - `"(XOR of nums1) * (len(nums2) % 2)"`
>
> - `"XOR"`
>
> - `"(XOR of nums2) * (len(nums1) % 2)"`

Because:

- Each `a` in `nums1` appears `len(nums2)` times

- Each `b` in `nums2` appears `len(nums1)` times

If the number of appearances is **even**, the XOR cancels out.

### ⏱️ Complexity
- **Time Complexity:** `O(n + m)`

- **Space Complexity:** `O(1)`

### 🏷️ Tags
`bit-manipulation`, `XOR`, `math`, `array`

### ✅ Key Takeaway

Using mathematical properties of XOR and parity (even/odd counts), we can reduce a brute-force O(n*m) problem into O(n + m) time.