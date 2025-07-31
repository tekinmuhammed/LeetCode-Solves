# 1432. Max Difference You Can Get From Changing an Integer

**Link:** [LeetCode 1432](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/)  
**Difficulty:** Medium

---

## Problem Description

You are given an integer `num`. You will perform **two different digit replacement operations**:

1. In the **first operation**, you replace **all occurrences of one digit** with **9** to get the **maximum possible number**.
2. In the **second operation**, you replace **all occurrences of one digit** with either **1** (for the first digit) or **0** (for other digits) to get the **minimum possible number**, ensuring no leading zeros.

You must return the **maximum difference** between the two numbers you can get from these operations.

---

## Example

```python
Input: num = 555
Output: 888
```

### Explanation:

- Maximize: Replace all '5's with '9' → 999

- Minimize: Replace all '5's with '1' → 111

- Difference: 999 - 111 = 888

---

## Constraints

- `1 <= num <= 10^8`
- No leading zeros in original or final numbers

---

## Approach

- Convert the number to a string for easy digit manipulation.
- To maximize the number:
  - Replace the first digit not equal to `'9'` with `'9'`.
- To minimize the number:
  - If the first digit is not `'1'`, replace it with `'1'`.
  - Otherwise, find the first digit (not `'0'` or `'1'`) from index 1 onwards and replace it with `'0'`.

This ensures only one digit is replaced in each transformation while producing the largest and smallest valid results.

---

### Time and Space Complexity

- **Time Complexity:** `O(N)`, where N is the number of digits in num.

- **Space Complexity:** `O(N)`, due to string operations.

### Tags

`Greedy`, `String`, `Manipulation`, `Math`

### Notes

- The logic ensures leading zeros are avoided during the minimization process.

- Only one digit type is allowed to be replaced in each transformation, which is respected in the implementation.