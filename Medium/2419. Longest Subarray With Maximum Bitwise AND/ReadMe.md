# 2419. Longest Subarray With Maximum Bitwise AND

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2419](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and)

---

## Problem Description

Given an array of integers `nums`, find the **length of the longest contiguous subarray** such that the bitwise **AND** of that subarray is equal to the **maximum value** of the entire array.

---

### Example

**Input:**
```python
nums = [1,2,3,3,2,2]
```

**Output:**
```python
2
```

### Explanation:

- The maximum value in the array is `3`.

- The longest contiguous subarray with only 3s is `[3,3]`, so the answer is `2`.

### Approach

- First, find the **maximum value** in the array.

- Then, iterate through the array:

- - Count how many **consecutive elements** are equal to `max_val`.

- - Track the **longest such sequence**.

### Key Insight:

Bitwise AND of multiple numbers is always **less than or equal to** any individual number. So the only way to have AND == max value is to have **a subarray where all values are equal to max_val**.

### Complexity

- **Time Complexity:** `O(n)` — single pass through the array

- **Space Complexity:** `O(1)` — constant extra space

### Tags

`Array`, `Bit-Manipulation`, `Sliding-Window`

### Notes

- No need to calculate actual AND values — just track sequences of max values.

- This approach is both efficient and simple.