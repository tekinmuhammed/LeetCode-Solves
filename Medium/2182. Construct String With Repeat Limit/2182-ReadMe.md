# 🟨 LeetCode 2182 - Construct String With Repeat Limit

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2182](https://leetcode.com/problems/construct-string-with-repeat-limit/)

---

## 📘 Problem Description

Given a string `s` and an integer `repeatLimit`, construct a **lexicographically largest** string by reordering the characters of `s` such that:

- No character appears more than `repeatLimit` times **in a row**.

If it's not possible to use a character due to the limit, insert a smaller character (if available) to break the sequence.

---

## 🧪 Example

### Input
```python
s = "cczazcc"
repeatLimit = 3
```


### Output
```python
"zzcccac"
```

### Explanation
- Use 'z' once.

- Then add up to 3 'c's.

- Can't add a 4th 'c', so break with 'a'.

- Continue accordingly.

### 🚀 Approach

1. Count the frequency of each character.

2. Sort the characters in **descending lexicographical order**.

3. In each iteration:

- Add up to `repeatLimit` of the current highest character.

- If the limit is hit and more of that character remains:

- - Try to insert the next available smaller character to break the sequence.

- Repeat until no characters remain or valid insertion is no longer possible.

This greedy approach ensures we always pick the **largest lexicographical character available**, while respecting the repeat limit.

### ⏱️ Complexity
- **Time Complexity:** `O(n log n)`

- - Sorting characters once and iterating through the string.

- **Space Complexity:** `O(n)`

- - Frequency map and result string.

### 🏷️ Tags
`greedy`, `heap`, `string`, `sorting`, `leetcode-medium`