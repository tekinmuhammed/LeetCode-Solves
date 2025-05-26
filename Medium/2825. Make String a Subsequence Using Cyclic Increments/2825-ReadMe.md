# 🔁 LeetCode 2825 - Make String a Subsequence Using Cyclic Increments

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2825](https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments)

---

## 📘 Problem Description

Given two strings `str1` and `str2`, determine whether you can make `str2` a subsequence of `str1` by **cyclically incrementing** some characters in `str1`.

- A cyclic increment means changing a character `c` to the **next character** in the alphabet. `'z'` becomes `'a'`.

---

## 🧪 Example

### Input:
```python
str1 = "abc"
str2 = "bcd"
```

## Output:
`True`

## Explanation:

- We can increment:

- - `'a'` → `'b'`

- - `'b'` → `'c'`

- - `'c'` → `'d'`

- So `"bcd"` can be formed as a subsequence of `"abc"` after cyclic increments.

# 🚀 Approach
- Use a two-pointer approach:

- - Traverse `str1` with `i`, and try to match `str2[j]`.

- - Allow a match if `str1[i] == str2[j]` or if cyclic increment of `str1[i]` equals `str2[j]`.

- If we can match all characters of `str2`, return `True`.

## ⏱️ Complexity
- **Time Complexity:** `O(n)`, where `n` is the length of `str1`.

- **Space Complexity:** `O(1)`

## 🏷️ Tags
`string`, `subsequence`, `cyclic-increment`, `two-pointers`, `leetcode-medium`