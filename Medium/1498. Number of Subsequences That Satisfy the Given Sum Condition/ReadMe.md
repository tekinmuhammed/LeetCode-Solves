# 1498. Number of Subsequences That Satisfy the Given Sum Condition

**Difficulty:** Medium  
**Link:** [LeetCode 1498](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)

---

## Problem Description

Given an array of integers `nums` and an integer `target`, return the **number of non-empty subsequences** such that the **sum of the minimum and maximum elements** in the subsequence is less than or equal to `target`.

Since the answer may be too large, return it **modulo 10⁹ + 7**.

---

## Example

### Input:
```python
nums = [3,5,6,7]
target = 9
```

### Output:
`4`

### Explanation:

The subsequences are: `[3]`, `[3,5]`, `[3,5,6]`, `[3,6]`.

### Constraints

- `1 <= nums.length <= 10⁵`

- `1 <= nums[i] <= 10⁶`

- `1 <= target <= 10⁶`

### Approach

Key Observations:
- Sort nums to efficiently evaluate minimum and maximum values using two pointers.

- For a fixed left and right, if nums[left] + nums[right] <= target, all subsets formed by elements between them are valid.

### Algorithm:

1. Sort the array to make min/max evaluation easy.

2. Precompute powers of 2 to represent all possible subsequences between two indices.

3. Use two pointers (left, right) to iterate:

- If nums[left] + nums[right] <= target: count all valid subsequences between left and right.

- Else: decrement right.

### Time and Space Complexity

- **Time Complexity:** `O(n log n)`
Sorting the array dominates the complexity.

- **Space Complexity:** `O(n)`
For precomputed powers of 2.

### Tags

`Two-Pointers`, `Sorting`, `Binary-Search`, `Combinatorics`, `Greedy`

### Notes

- This problem emphasizes counting valid subsequences based on extreme values.

- Precomputing powers of 2 is a common trick in combinatorial subset counting problems.