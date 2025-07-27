# 3442. Maximum Difference Between Even and Odd Frequency I

**Problem Link:** [LeetCode 3442](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/)  
**Difficulty:** Easy

---

## Problem Description

Given a string `s`, count the frequency of each character.  
Your task is to find the **maximum difference** between an **odd frequency** and an **even frequency** of characters in the string.

- The difference is defined as `odd_count - even_count`.
- You must consider **all possible pairs** of odd and even frequencies.

Return the maximum such difference. If no such pair exists, return negative infinity (`-∞`).

---

## Example

```python
Input: s = "aabbccc"
Output: 1
Explanation:
Frequencies: a → 2, b → 2, c → 3
Valid difference: 3 (odd) - 2 (even) = 1
Maximum difference is 1.
```
---

## Approach

- Count the frequency of each character using `collections.Counter`.
- Separate the frequencies into two lists:
  - `odd_freq`: list of odd counts
  - `even_freq`: list of even counts
- For every possible pair `(odd, even)`, compute `odd - even` and track the maximum.

---

### Complexity

- **Time Complexity:** `O(N + K²)`, where

- - N = length of string `s`,

- - K = number of unique characters (at most 26 for lowercase letters)

- **Space Complexity:** `O(1)`, constant space for frequency arrays

### Tags

`HashMap`, `String`, `Greedy`, `Brute-Force`, `Frequency-Count`