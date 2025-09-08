# 1317. Convert Integer to the Sum of Two No-Zero Integers

**Difficulty:** Easy  
**Link:** [LeetCode 1317](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/)

---

## Problem Description
Given an integer `n`, return two integers `[a, b]` such that:
- `a + b = n`
- Neither `a` nor `b` contains the digit `0`

It is guaranteed that at least one valid solution exists.

---

## Example 1
**Input:**
```python
n = 11
```

**Output:**
```python
[2, 9]
```

---

## Example 2
**Input:**
```python
n = 1010
```

**Output:**
```python
[11, 999]
```

---

## Constraints
- `2 <= n <= 10^4`

---

## Approach

### Key Idea
- Iterate over possible values of `a` starting from `1`.
- Compute `b = n - a`.
- Check if both `a` and `b` do **not** contain the digit `'0'`.
- If valid, return `[a, b]`.

### Algorithm
1. Define a helper function `has_zero(x)` → returns `True` if `'0'` appears in the decimal representation of `x`.
2. Loop `a` from `1` to `n-1`.
3. For each `a`, compute `b = n - a`.
4. If both `a` and `b` pass the check, return `[a, b]`.

---

## Time and Space Complexity
- **Time Complexity:** O(n) in the worst case (linear scan up to `n`).  
- **Space Complexity:** O(1) (constant extra memory).  

---

## Tags
Math, Brute Force, Constructive Algorithms

---

## Notes
- The problem guarantees that a solution exists, so the loop will always find an answer.  
- In practice, solutions are found very quickly (often near the beginning of the search).  