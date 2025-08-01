# 1593. Split a String Into the Max Number of Unique Substrings

This solution uses a backtracking approach to explore all possible ways to split a string into **non-empty, unique substrings**. The goal is to maximize the number of such substrings whose concatenation equals the original string.

## 🧠 Algorithm

1. Start at the beginning of the string.
2. For each possible end position, form a substring.
3. If the substring hasn't been seen before:
   - Add it to the set.
   - Recurse from the end of the current substring.
   - Remove the substring (backtrack).
4. Track the maximum number of unique substrings seen during this process.

## 📌 Example

```python
Input: s = "ababccc"
Output: 5
```

## 🚀 Time & Space Complexity

**Time:** O(2^n), where n is the length of the string (due to exploring all split possibilities)

**Space:** O(n) for recursion stack and substring set

---

### 🏷️ Tags

`#backtracking`, `#recursion`, `#string`, `#dfs`, `#brute-force`, `#unique-substrings`, `#leetcode-medium`, `#python`
