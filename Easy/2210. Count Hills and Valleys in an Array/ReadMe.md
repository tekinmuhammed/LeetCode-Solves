# 2210. Count Hills and Valleys in an Array

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2210](https://leetcode.com/problems/count-hills-and-valleys-in-an-array/)

---

## Problem Description

You are given an array `nums` of integers. A **hill** is a point that is **strictly greater than its closest non-equal neighbors**, and a **valley** is a point that is **strictly smaller than its closest non-equal neighbors**.

Ignore adjacent equal values while determining if an element is a hill or valley.

Return the number of hills and valleys in the array.

---

### Example

**Input:**
```python
nums = [2, 4, 1, 1, 6, 5]
```

**Output:**
```python
3
```

### Explanation:

- At index 1: `4` is a hill (greater than 2 and 1).

- At index 4: `6` is a hill (greater than 1 and 5).

- At index 5: `5` is neither (last element).

- The value `1` at index 2 and 3 are considered together (equal values), so only index 2 is evaluated.

### Approach

This solution **skips over repeated adjacent values** and compares only the meaningful non-equal neighbors.

**Algorithm Steps:**

1. Initialize a pointer `j` to track the **last meaningful element**.

2. Iterate from index `1` to `n-2`:

-  If `nums[i]` is greater than both neighbors → it’s a hill.

- If `nums[i]` is smaller than both neighbors → it’s a valley.

3. Each time a hill or valley is found, update `j = i` to track the last seen meaningful comparison point.

### Complexity

-  **Time Complexity:** `O(n)`

- **Space Complexity:** `O(1)`

### Tags

`Array`, `Simulation`, `Greedy`

### Notes

- The original problem requires careful **handling of duplicates**, as multiple same values can break naïve comparisons.

- This solution cleverly tracks the last valid comparison index (`j`) to deal with plateaus.