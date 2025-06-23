# 🔢 LeetCode 2375 - Construct Smallest Number From DI String

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2375](https://leetcode.com/problems/construct-smallest-number-from-di-string)

---

## 📘 Problem Description

You are given a string `pattern` of length `n` consisting only of the characters `'I'` (for increasing) and `'D'` (for decreasing).

Return the **lexicographically smallest** permutation of the numbers `[1, 2, ..., n + 1]` that satisfies the pattern:

- `'I'` at index `i` means `perm[i] < perm[i + 1]`
- `'D'` at index `i` means `perm[i] > perm[i + 1]`

---

## 🧪 Example

### Input:
```python
pattern = "IDID"
```

### Output:
```python
"13254"
```

### Explanation:

- 1 < 3 (I), 3 > 2 (D), 2 < 5 (I), 5 > 4 (D)

### 🚀 Approach

We use a **stack-based approach** to simulate the pattern:

- Iterate through the `pattern` + `"I"` (added sentinel to flush the stack at the end).

- For each position:

- - Push the current number onto a stack.

- - If the current character is `"I"`, pop all elements from the stack into the result.

- This approach ensures that for a series of `"D"`s, numbers are placed in descending order when flushed.

This greedy + stack trick yields the **lexicographically smallest** valid number.

### ⏱️ Complexity

- **Time Complexity:** `O(n)`, where `n` is the length of the pattern.

- **Space Complexity:** `O(n)`, for the stack and result list.

### 🏷️ Tags
`greedy`, `stack`, `string`, `permutation`, `simulation`