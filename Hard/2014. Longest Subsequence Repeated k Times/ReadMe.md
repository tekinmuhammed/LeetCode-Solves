# 2014. Longest Subsequence Repeated k Times

**Difficulty:** Hard  
**Link:** [LeetCode 2014](https://leetcode.com/problems/longest-subsequence-repeated-k-times/)

---

## Problem Description

Given a string `s` and an integer `k`, find the **longest string** `x` such that:

- `x` is a subsequence of `s`.
- Repeating `x` exactly `k` times (`x + x + ... + x`) is still a subsequence of `s`.

If there are multiple answers, return the **lexicographically largest** one.

---

## Example

### Input:
```python
s = "letsleetcode"
k = 2
```

### Output:
```python
"let"
```

### Constraints

- `2 <= s.length <= 2000`

- `1 <= k <= 2000`

- `s` consists only of lowercase English letters.

### Approach

**Core Idea:**
Use **Breadth-First Search (BFS)** with a queue to generate all candidate subsequences in lexicographical order. For each candidate, check whether repeating it `k` times is still a subsequence of `s`.

**Subsequence Check:**
A helper function `isK(sub, s, k)` simulates scanning through `s` to see if `sub * k` is a subsequence.

### Time and Space Complexity

- **Time Complexity:** Exponential in the length of the result (worst-case), but pruned by subsequence validation.

- **Space Complexity:** `O(B)`, where `B` is the number of valid candidate subsequences held in the queue.

### Tags

`Greedy`, `BFS`, `String-Matching`, `Subsequence`

### Notes

- Lexicographical order is implicitly handled by BFS exploring shorter strings first and checking `a` to `z` in order.

- Smart pruning is achieved using the `isK` function to skip invalid paths early.