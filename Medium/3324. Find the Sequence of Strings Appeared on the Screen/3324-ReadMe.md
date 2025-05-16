# LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen

## 🔗 Problem Link
[LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen](https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/)

## 🧠 Problem Description

You're given a `target` string. Starting from an empty string, you can:

1. Add a character `'a'` at the end.
2. Increment the **last character** of the string (e.g., `'a'` → `'b'`).

Your task is to return the **list of strings** that appear on the screen while transforming an empty string into the `target`.

## 🧪 Example

```python
Input: target = "abc"
Output: ['a', 'b', 'ba', 'bb', 'bc']
```
## 💡 Approach
Begin with an empty string.

Always append `'a'` to go deeper into the target.

Increment the last character repeatedly until it matches the corresponding character in `target`.

Append every intermediate step into a result list.

## 🧮 Complexity

**Time Complexity:** O(n * 26)

**Space Complexity:** O(n²)

## 📌 Tags
`string`, `simulation`, `greedy`, `string-manipulation`, `constructive`