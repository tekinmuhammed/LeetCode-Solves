# 2966. Divide Array Into Arrays With Max Difference

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2966](https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/)

---

## Problem Description

You are given an integer array `nums` and an integer `k`.  
You must divide `nums` into multiple subarrays of length `3`, such that **the difference between the maximum and minimum values in each subarray is less than or equal to `k`**.

Return the list of all valid subarrays. If it's **not possible**, return an empty list.

---

## Example

### Input:
```python
nums = [1,3,4,8,7,9], k = 2
```
### Output:
```python
[[1,3,4],[7,8,9]]
```
---

## Constraints

- `nums.length % 3 == 0`
- `1 <= nums.length <= 3 * 10⁴`
- `1 <= nums[i] <= 10⁵`
- `0 <= k <= 10⁵`

---

## Approach

To form valid subarrays:
1. **Sort the input array.**
   - This helps in grouping closest values together, minimizing the max difference in groups.
2. **Iterate in chunks of 3.**
   - For each group of 3 elements:
     - Check if the difference between the largest and smallest element is `<= k`.
     - If yes, append to the result.
     - If not, return an empty list since division isn’t possible.

---

### Time and Space Complexity

- **Time Complexity:** `O(n log n)` due to sorting.

- **Space Complexity:** `O(n)` for storing the result groups.

### Tags
`Sorting`, `Greedy`, `Array`, `Simulation`

### Notes
- Sorting the array simplifies grouping.

- Always check the max-min difference for each triplet.