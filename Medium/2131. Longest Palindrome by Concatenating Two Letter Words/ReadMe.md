# 🔠 LeetCode 2131 - Longest Palindrome by Concatenating Two Letter Words

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2131](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words)

---

## 📘 Problem Description

You are given an array of strings `words`, where each word has exactly **two lowercase English letters**.

Your task is to form the **longest palindrome string** (length-wise) by concatenating some of these words in any order. Each word can be used **at most once**.

Return the **maximum length** of the palindrome that can be formed.

---

## 🧠 Approach

We use a `Counter` to count occurrences of each 2-letter word.

1. **Mirror pairs:** For words like `'ab'` and `'ba'`, we can pair them together to form a palindrome fragment: `'abba'`. Each such pair adds 4 to the total length.
2. **Self pairs:** Words like `'aa'`, `'cc'`, etc., can form pairs like `'aaccaa'`, and if one is left unpaired, it can be placed **in the center**.
3. We ensure only one **odd self-word** (like `'aa'`) is placed in the center of the palindrome.

---

### ⏱️ Time and Space Complexity

- **Time Complexity:** `O(n)` — where `n` is the number of words.

- **Space Complexity:** `O(1)` — max 26×26 = 676 unique 2-letter lowercase combinations.

### ✅ Example
```python
Input:
words = ["lc","cl","gg"]

Output: 
6

Explanation:
"lc" + "gg" + "cl" = "lcggcl" is a palindrome.
```

### 🏷️ Tags

`hash-table`, `greedy`, `palindrome`, `string`, `counter`, `two-pointers`