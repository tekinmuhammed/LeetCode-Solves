# 🟨 LeetCode 1957 - Delete Characters to Make Fancy String

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1957](https://leetcode.com/problems/delete-characters-to-make-fancy-string/)

---

## 📘 Problem Description

A string is called **fancy** if it doesn't contain **three consecutive** identical characters.

Given a string `s`, return the **minimum-length fancy string** you can get after deleting some characters (without reordering the others).

---

## 🧪 Example

### Input:

```python
s = "leeetcode"
```

## Output:

`"leetcode"`

## Explanation:

- Remove one `'e'` to avoid having three in a row.

## 🚀 Approach

We iterate through the string while building a result list:

- If the last two characters in **the result are the same as the current character**, skip the current character.

- Otherwise, append it.

This ensures no three identical characters are adjacent.

## ⏱️ Complexity

- **Time Complexity:** O(n)

- **Space Complexity:** O(n)

## 🏷️ Tags

`string`, `greedy`, `leetcode-easy`