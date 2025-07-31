# 🔐 LeetCode 1400 - Construct K Palindrome Strings

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1400](https://leetcode.com/problems/construct-k-palindrome-strings)

---

## 📘 Problem Description

Given a string `s` and an integer `k`, return `true` if you can construct **k** non-empty palindrome strings with all the characters in `s`. Otherwise, return `false`.

Each character must be used **exactly once**.

---

## 🧪 Example

### Input:
```python
s = "annabelle"
k = 2
```

### Output:

`True`

### Explanation:

- You can construct "anna" and "elle", both palindromes.

### 🧠 Approach

**Key Ideas:**

- A **palindrome** can have **at most one character with odd frequency** (if the palindrome has odd length).

- If we want to build **k** palindromes, we must be able to distribute the characters such that **at most k** of them need an odd middle character.

- So we count how many characters appear an odd number of times. If that number is **greater than** k, it's impossible.

- Also, we must have **at least k characters** in total to make k non-empty strings.

**Steps:**

1. If `k > len(s)`, return `False`. Not enough characters.

2. Count frequencies using `collections.Counter`.

3. Count how many characters have **odd frequencies**.

4. Return `True` if `odd_count <= k`, else `False`.

### ⏱️ Complexity

- **Time Complexity:** `O(n)`, where `n` is the length of string `s`

- **Space Complexity:** `O(1)` (at most 26 lowercase letters in the Counter)

### 🏷️ Tags

`greedy`, `hashmap`, `palindrome`, `string`, `frequency`