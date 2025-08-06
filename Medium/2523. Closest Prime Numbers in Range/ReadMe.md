# 🧮 LeetCode 2523 - Closest Prime Numbers in Range

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2523](https://leetcode.com/problems/closest-prime-numbers-in-range)

---

## 📘 Problem Description

Given two integers `left` and `right`, return the pair of **two prime numbers** within that range such that:

- Both primes are within `[left, right]`.
- The absolute difference between them is **the smallest possible**.

If there is no such pair, return `[-1, -1]`.

---

## 🧪 Examples

### Example 1:
```python
Input: left = 10, right = 19
Output: [11, 13]
```

### Example 2:
```python
Input: left = 4, right = 4
Output: [-1, -1]
```

### 🧠 Approach

1. Use the **Sieve of Eratosthenes** to precompute all primes up to `10^6`.

2. Filter the list of primes to include only those in `[left, right]`.

3. Iterate over this list to find the **closest pair** (minimum difference).

4. If fewer than two primes exist in the range, return `[-1, -1]`.

### ⏱️ Complexity

- **Time Complexity:** O(N log log N) for sieve + O(N) for filtering and diff check

- **Space Complexity:** `O(N)` for storing sieve and primes list

### 🏷️ Tags

`primes`, `sieve`, `number-theory`, `math`, `medium`