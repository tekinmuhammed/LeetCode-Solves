# 🔠 LeetCode 3042 - Count Prefix and Suffix Pairs I

**Difficulty:** Easy  
**Problem Link:** [LeetCode 3042](https://leetcode.com/problems/count-prefix-and-suffix-pairs-i)

---

## 📘 Problem Description

You are given a list of strings `words`.

Count the number of **distinct pairs** `(i, j)` such that:

- `0 <= i < j < len(words)`, and  
- `words[j]` **starts with** `words[i]`, and  
- `words[j]` **ends with** `words[i]`.

Return the total number of such prefix-suffix pairs.

---

## 🧪 Example

### Input:
```python
words = ["a", "ab", "aba", "abab"]
```

### Output:
`3`

### Explanation:

- Pair (0, 2): "a" is both prefix and suffix of "aba"

- Pair (0, 3): "a" is both prefix and suffix of "abab"

- Pair (2, 3): "aba" is prefix and suffix of "abab" ❌ (invalid)

- Only valid ones are (0,2), (0,3), (1,3)

### 🚀 Approach

We use a simple **brute-force double loop** to iterate over all valid `(i, j)` pairs.

For each pair, we check:

- Does `words[j].startswith(words[i])`?

- Does `words[j].endswith(words[i])`?

If both are true, we increment the count.

### ⏱️ Complexity

- **Time Complexity:** `O(n²)` — for all `(i, j)` pairs

- **Space Complexity:** `O(1)`

This brute-force approach is acceptable because the input size is small (as suggested by the "I" in the problem name).

### 🏷️ Tags

`string`, `prefix`, `suffix`, `brute-force`, `leetcode-easy`