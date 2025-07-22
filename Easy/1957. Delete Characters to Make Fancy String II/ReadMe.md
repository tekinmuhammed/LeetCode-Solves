# 1957. Delete Characters to Make Fancy String

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1957](https://leetcode.com/problems/delete-characters-to-make-fancy-string/)

---

## Problem Description

A **fancy string** is a string where **no three consecutive characters are the same**.

Given a string `s`, your task is to **delete the minimum number of characters** from `s` so that it becomes a fancy string.

Return the final fancy string.

### Example

**Input:**
```python
s = "leeetcode"
```

**Output:**
```python
"leetcode"
```

**Explanation:**  
Remove one of the `'e'` characters so that no three consecutive characters are the same.

---

## Approach

We iterate through the characters of the string and build a new result list. While iterating:

- If the last two characters in the result list are equal to the current character (i.e., three in a row), we skip the current character.
- Otherwise, we append the character to the result list.

This greedy approach ensures that at most two consecutive characters are kept.

---

### Complexity

- **Time Complexity:** `O(n)`, where `n` is the length of the input string.

- **Space Complexity:** `O(n)`, for storing the result list.

### Tags
`Greedy`, `String`, `Two-Pointers`

### Key Insights

- The solution uses a simple greedy strategy to skip unnecessary characters.

- Keeping track of only the last two characters is sufficient to enforce the “no three consecutive characters” rule.