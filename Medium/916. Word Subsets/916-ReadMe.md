# 📚 LeetCode 916 - Word Subsets

**Difficulty:** Medium  
**Problem Link:** [LeetCode 916](https://leetcode.com/problems/word-subsets)

---

## 📘 Problem Description

You are given two string arrays `words1` and `words2`.

A string `b` is a **subset** of string `a` if every letter in `b` occurs in `a` including multiplicity.

A string `a` from `words1` is a **universal word** if for every string `b` in `words2`, `b` is a subset of `a`.

Return an array of all the universal words in `words1`. You may return the answer in **any order**.

---

## 🧪 Example

### Input:
```python
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
```

### Output:

`["facebook","google","leetcode"]`

### Explanation:

- All universal words must contain at least one `'e'` and one `'o'`.

### 🚀 Approach

Step-by-step:
1. For each word in `words2`, count the frequency of each letter.

2. Build a **combined frequency map** that stores the maximum count required for each character across all `words2`.

3. For each word in `words1`, count its letters and check if it satisfies all character requirements from the combined map.

4. If yes, it’s a universal word — add it to the result.

**Why it works:**
Using the **maximum requirement** for each character from `words2` lets us check each word in `words1` only once, against a fixed reference, instead of checking against each word in `words2` individually.

###  ⏱️ Complexity

- **Time Complexity:** `O(n * k + m * l)`
Where:

- - `n = len(words1)`, `k` is average word length in `words1`

- - `m = len(words2)`, `l` is average word length in `words2`

- **Space Complexity:** `O(26)` for the combined counter

### 🏷️ Tags
`hashmap`, `counter`, `subset`, `frequency`, `strings`, `medium`