# 2294. Partition Array Such That Maximum Difference Is K

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2294](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k)

---

## Problem Description

You are given an integer array `nums` and an integer `k`.  
You need to partition the array into one or more **non-empty** subarrays such that the **maximum difference between any two elements in a subarray is less than or equal to `k`**.

Return the **minimum number of subarrays** needed.

---

## Example

### Input:
```python
nums = [3,6,1,2,5], k = 2
```
### Output:
```python
2
```

### Explanation:
- One possible partition: [1,2,3] and [5,6]
- Both subarrays satisfy the condition (max - min ≤ k)

---

## Constraints

- `1 <= nums.length <= 10⁵`
- `0 <= nums[i] <= 10⁵`
- `0 <= k <= 10⁵`

---

## Approach

- **Sort the array** to bring similar elements closer together.
- Initialize the first subarray with the first element.
- Traverse through the array:
  - If the current element exceeds the allowed difference from the start of the current group, start a new subarray.
- Increment count whenever a new subarray is created.

---

### Time and Space Complexity

- **Time Complexity:** `O(n log n)` – due to sorting.

- **Space Complexity:** `O(1)` – constant extra space.

### Tags

`Greedy`, `Sorting`, `Array`

### Notes

- Sorting makes it easy to ensure all values in a group are within a range.

- A new group is started as soon as a value violates the max difference `k`.