# 🟩 LeetCode 1422 - Maximum Score After Splitting a String

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1422](https://leetcode.com/problems/maximum-score-after-splitting-a-string)

---

## 📘 Problem Description

Given a binary string `s`, split it into two **non-empty substrings** at any index `i` (1 ≤ i < len(s)).

The **score** of the split is defined as:

- Number of `'0'`s in the **left** substring +
- Number of `'1'`s in the **right** substring.

Return the **maximum score** achievable by splitting the string at any position.

---

## 🧪 Example

### Input:
```python
s = "011101"
```

### Output:

`4`

### Explanation:

- Splitting at index 3: `"011"` and `"101"`

- Left part has **2 zeros**, right part has **2 ones**

- Score = 2 + 2 = 4

### 🚀 Approach
We try all possible split positions:

- At each position `i`, calculate:

- - `left_zeros = count('0') in s[:i]`

- - `right_ones = count('1') in s[i:]`

- - `score = left_zeros + right_ones`

- Track and return the maximum score.

This brute-force approach is efficient enough since the input size is limited.

### ⏱️ Complexity
- **Time Complexity:** `O(n²)`
(Each split recomputes counts over substrings)

> You can optimize this to O(n) by precomputing prefix sums.

- **Space Complexity:** `O(1)`

### 🏷️ Tags
`string`, `greedy`, `prefix`, `leetcode-easy`