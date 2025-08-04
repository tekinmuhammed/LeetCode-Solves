# 2311. Longest Binary Subsequence Less Than or Equal to K

**Difficulty:** Medium  
**Link:** [LeetCode 2311](https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/)

---

## Problem Description

Given a binary string `s` and an integer `k`, return the length of the **longest subsequence** of `s` that represents a binary number less than or equal to `k`.

A **subsequence** is a sequence derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

---

## Example

### Input:
```python
s = "1001010"
k = 5
```

### Output:
```python
5
```

### Constraints

- `1 <= s.length <= 1000`

- `s consists only of '0' and '1'`

- `0 <= k <= 10^9`

### Approach

**Key Ideas:**

- Start by counting all `'0'`s in the string; these contribute `0` to any binary number and can always be part of a valid subsequence.

- Traverse the string in reverse (from least to most significant bit) to greedily add `'1'`s if the binary number constructed so far does not exceed `k`.

- Use bitwise operations to build the number incrementally for efficiency.

### Time and Space Complexity

- **Time Complexity:** `O(n)`

- **Space Complexity:** `O(1)`

### Tags

`Greedy`, `Bit-Manipulation`, `Subsequence`, `Binary`

### Notes

- Traversing from the end ensures that added `'1'`s contribute the least possible value.

- This is a space-optimized and efficient solution suitable for large strings.