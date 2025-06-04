# 🟩 LeetCode 2559 - Count Vowel Strings in Ranges

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2559](https://leetcode.com/problems/count-vowel-strings-in-ranges)

---

## 📘 Problem Description

You are given a list of strings `words` and a list of integer queries `queries`, where each query is a range `[start, end]`.

A **vowel string** is a string that **starts and ends with a vowel** (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`).

For each query, return the number of **vowel strings** in the range `words[start]` to `words[end]` (inclusive).

---

## 🧪 Example

### Input:
```python
words = ["aba", "bcb", "ece", "aa", "e"]
queries = [[0,2], [1,4], [1,1]]
```

### Output:
```python
[2, 3, 0]
```

### Explanation:

- Query [0,2]: "aba" and "ece" are vowel strings → count = 2

- Query [1,4]: "ece", "aa", "e" → count = 3

- Query [1,1]: "bcb" → not a vowel string → count = 0

### 🚀 Approach

1. Create a helper function `is_vowel(c)` to check if a character is a vowel.

2. Build a **prefix sum array** where `prefix_sum[i]` represents the count of vowel strings in `words[0:i]`.

3. For each query `[start, end]`, compute the result as:
```python
prefix_sum[end + 1] - prefix_sum[start]
```
This allows **constant time query resolution** after a single pass precomputation.

### ⏱️ Complexity

- **Time Complexity:** `O(n + q)`

- - n = number of words (for building prefix sum)

- - q = number of queries (constant-time lookup)

- **Space Complexity:** `O(n)`

- For prefix sum array

## 🏷️ Tags
`prefix-sum`, `string`, `range-query`, `leetcode-medium`