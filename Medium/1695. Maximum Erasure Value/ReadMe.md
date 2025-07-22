# 1695. Maximum Erasure Value

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1695](https://leetcode.com/problems/maximum-erasure-value/)

---

## Problem Description

You are given an array of positive integers `nums`.

You must choose a **subarray** (i.e., a contiguous sequence of elements) such that all the elements are **unique**, and the **sum** of the subarray is **maximized**.

Return the **maximum possible sum** of such a subarray.

---

### Example

**Input:**
```python
nums = [4,2,4,5,6]
```

### Output:
```python
17
```

### Explanation:

The subarray `[2, 4, 5, 6]` has all unique elements and a sum of `17`, which is the maximum possible.

### Approach

This problem is efficiently solved using the **sliding window** technique combined with a `set` to track unique elements:

- We use two pointers: `left` and `right`.

- As we iterate with the `right` pointer, if we encounter a duplicate element, we shrink the window from the left until the duplicate is removed.

- At each valid window, we maintain the current sum and update the maximum sum accordingly.

### Complexity

- **Time Complexity:** `O(n)`, where `n` is the length of `nums`. Each element is visited at most twice (once by right, once by left).

- **Space Complexity:** `O(n)`, for the seen set.

### Tags

`Sliding-Window`, `HashSet`, `Greedy, `Two-Pointers`

### Key Insights

- Using a **hash set** ensures we track unique elements efficiently.

- The **sliding window** approach is ideal for contiguous subarray problems with constraints on elements.