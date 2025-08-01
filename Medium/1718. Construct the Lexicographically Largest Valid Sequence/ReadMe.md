# 🔠 LeetCode 1718 - Construct the Lexicographically Largest Valid Sequence

**Difficulty:** Hard  
**Problem Link:** [LeetCode 1718](https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence)

---

## 📘 Problem Description

You are given an integer `n`.

You need to construct an array `nums` of size `2 * n - 1` such that:

1. Each integer from `1` to `n` appears **exactly twice**, **except** for `1` which appears **only once**.
2. For every integer `i > 1`, the two occurrences of `i` must be exactly `i` indices apart (i.e., `j` and `j + i` for some `j`).

Return the **lexicographically largest** valid sequence possible.  
If multiple answers exist, return the one that is **largest in lexicographical order**.

---

## 🧪 Example

### Input:
```python
n = 3
```

### Output:
```python
[3, 1, 2, 3, 2]
```

### Explanation:

- `3` is placed at indices `0` and `3` (distance = 3)

- `2` is placed at indices `2` and `4` (distance = 2)

- `1` is placed at index `1` (only once)

### 🚀 Approach

We use **backtracking** to try placing numbers from `n` down to `1`, greedily aiming for the **largest lexicographical result**:

- Start from the leftmost index.

- For each number `num` from `n` to `1`:

- - If it's not used:

- - - If `num == 1`, place it once.

- - - If `num > 1`, try placing it at `i` and `i + num`.

- If we reach the end of the array, a valid sequence is found.

- Track usage with a `used` array and backtrack when needed.

### ⏱️ Complexity

- **Time Complexity:** Exponential in `n` (backtracking over placements).

- **Space Complexity:** `O(n)` for tracking usage and result array.

### 🏷️ Tags

`backtracking`, `greedy`, `recursion`, `lexicographical`, `hard`