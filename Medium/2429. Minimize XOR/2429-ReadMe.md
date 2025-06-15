# ⚡ LeetCode 2429 - Minimize XOR

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2429](https://leetcode.com/problems/minimize-xor/)

---

## 📘 Problem Description

You are given two positive integers `num1` and `num2`. 

Your goal is to construct an integer `x` such that:
- `x` has **the same number of set bits** (`1`s in binary) as `num2`
- The **XOR value `num1 ^ x` is minimized**

Return the integer `x`.

---

## 🧪 Example

### Input:
```python
num1 = 3  # (binary 011)
num2 = 5  # (binary 101 → 2 set bits)
```

### Output:
`3  # binary 011`

### Explanation:

We want a number with 2 set bits (like `num2`) that is as close as possible to `num1` in terms of XOR.

Possible 2-bit numbers:

- 1 (001), XOR = 2

- 2 (010), XOR = 1

- 3 (011), XOR = 0 ← ✅ minimum

### 🧠 Approach

- Count the number of `1` bits in `num2`.

- Try to match as many bits as possible from `num1`, starting from the highest bit (to minimize XOR).

- If there are still set bits left to assign, assign them starting from the **lowest unset bits**.

### ⏱️ Complexity

- **Time Complexity:** `O(32)` — Constant time for 32-bit integers

- **Space Complexity:** `O(1)`

### 🔍 Notes

- This solution first **preserves bits** from `num1` that are already set (for minimum XOR), and only adds bits where necessary.

- The two passes (high-to-low and low-to-high) ensure optimal selection of bit positions.

### 🏷️ Tags
`bit-manipulation`, `greedy`, `XOR`, `binary`