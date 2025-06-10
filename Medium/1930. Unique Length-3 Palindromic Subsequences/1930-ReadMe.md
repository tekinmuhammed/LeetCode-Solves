# 🟨 LeetCode 1930 - Unique Length-3 Palindromic Subsequences

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1930](https://leetcode.com/problems/unique-length-3-palindromic-subsequences)

---

## 📘 Problem Description

Given a string `s`, return the **number of unique palindromic subsequences of length 3**.

A palindromic subsequence is a string that reads the same forward and backward and is derived from `s` by deleting some characters **without changing the order** of the remaining characters.

You must count only **unique** palindromic subsequences of length 3.

---

## 🧪 Example

### Input:
```python
s = "aabca"
```

### Output:
`3`

### Explanation:
The unique palindromic subsequences of length 3 are:

- `"aba"`

- `"aaa"`

- `"aca"`

So the result is 3.

### 🚀 Approach
We are looking for palindromes in the form of `aXa`, where the first and last characters are the same, and the middle character can be any.

- Iterate through **all unique characters** in the string.

- For each character `char`:

- - Find its first and last occurrence.

- - All characters between those two can serve as the **middle character**.

- - Combine `char + mid_char + char` for all possible `mid_char` to form palindromes and store them in a set.

The final result is the **size of the set**, which stores all unique valid palindromes.

### ⏱️ Complexity
- **Time Complexity:** `O(26 × n)` → Simplifies to `O(n)`
(Since we loop through at most 26 characters and scan substring for each.)

- **Space Complexity:** `O(1)`
(At most 26×26 = 676 unique palindromes.)

### 🏷️ Tags
`string`, `hashset`, `palindrome`, `leetcode-medium`