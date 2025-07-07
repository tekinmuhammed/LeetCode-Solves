# 2566. Maximum Difference by Remapping a Digit

**Problem Link:** [LeetCode 2566](https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/)  
**Difficulty:** Easy

---

## Problem Description

You are given a positive integer `num`.

You are allowed to **remap at most one digit to another digit** in `num`. The digit must be **replaced with the same digit** wherever it appears in the number.

- For example, if `num = 1231`, you can remap digit `1` to `9`, and get `9239`.

Your task is to compute the **maximum possible difference** between two numbers:
- One obtained by remapping **a digit to `9`** (maximize)
- The other obtained by remapping **a digit to `0`** (minimize, but cannot make number start with `0`)

Return the **maximum difference** between these two results.

---

## Example
```python
Input: num = 11891
Output: 99009
```

### Explanation:

- Replace '1' with '9' → 99899

- Replace '8' with '0' → 10891 → not optimal

- Replace first non-zero digit that's not 0 (i.e., '1') with '0' → 00800 → invalid

- Optimal: replace '1' with '0' → 00891 → 891 (valid, leading zero removed)

- Final result: 99899 - 891 = 99008

---

## Approach

- Convert `num` to a string for digit-level manipulation.
- For **maximizing**:
  - Find the first digit that is not `'9'` and replace all its occurrences with `'9'`.
- For **minimizing**:
  - Find the first digit that is not `'0'` and replace all its occurrences with `'0'`.
- Take the integer difference between these two modified values.

---

### Complexity

- **Time Complexity:** `O(N)`, where N is the number of digits in num

- **Space Complexity:** `O(N)`, due to string manipulation

### Tags
`Greedy`, `String`, `Math`

### Notes

- Leading zeros in the minimized number do not affect the result, as converting to `int` removes them.

- The approach ensures only one digit is remapped, which is optimal by design.