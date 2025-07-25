# 🔤 LeetCode 2185 - Counting Words With a Given Prefix

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2185](https://leetcode.com/problems/counting-words-with-a-given-prefix)

---

## 📘 Problem Description

You are given a list of strings `words` and a string `pref`.

Return the number of strings in `words` that **start with** the string `pref`.

---

## 🧪 Example

### Input:

```python
words = ["pay", "attention", "practice", "attend"]
pref = "at"
```

### Output:
```python
2
```

### Explanation:

- The words `"attention"` and `"attend"` start with the prefix `"at"`, so the answer is `2`.

### 🚀 Approach

We simply iterate through each word in the `words` list and check whether it starts with the given `pref` string using the built-in `startswith()` method.

### ⏱️ Complexity

- **Time Complexity:** `O(n * m)`,
where `n` is the number of words and `m` is the length of the prefix (in the worst case).

- **Space Complexity:** `O(1)`

### 🏷️ Tags
`string`, `prefix`, `leetcode-easy`, `iteration`