# 🟨 LeetCode 2696 - Minimum String Length After Removing Substrings

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2696](https://leetcode.com/problems/minimum-string-length-after-removing-substrings)

---

## 📘 Problem Description

You are given a string `s` consisting only of characters `'A'`, `'B'`, `'C'`, and `'D'`.

You can perform the following operation any number of times:

- Delete the substring `"AB"` or `"CD"` from `s`.

Return the **minimum length** of `s` after performing all possible deletions.

---

## 🧪 Example

### Input:
```python
s = "ABFCACDB"
```

## Output:
`2`

## Explanation:

- Remove `"AB"` → "FCACDB"

- Remove `"CD"` → "FCAB"

- Remove `"AB"` → "FC"

- Final length = 2

## 🚀 Approach
We use a stack to simulate the removal process:

- For each character:

- - Push it onto the stack.

- - Check if the top 2 characters form `"AB"` or `"CD"`.

- - If so, pop both — simulate the deletion.

At the end, the stack contains the remaining characters, and its length is the answer.

## ⏱️ Complexity
- **Time Complexity:** O(n)

- **Space Complexity:** O(n) (in the worst case, no deletions)

## 🏷️ Tags

`stack`, `string`, `simulation`, `leetcode-easy`