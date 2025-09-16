# 📘 LeetCode 1671 - Minimum Number of Removals to Make Mountain Array

**Difficulty:** Hard  
**Problem Link:** [LeetCode 1671](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array)

---

## Problem Description

You may recall that an array `arr` is a **mountain array** if:

- `arr.length >= 3`  
- There exists some index `i` (`0 < i < arr.length - 1`) such that:
  - `arr[0] < arr[1] < ... < arr[i]`
  - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given an integer array `nums`, return **the minimum number of elements to remove** to make `nums` a mountain array.

---

## Example
### Input:
```python
nums = [2,1,1,5,6,2,3,1]
```

### Output:
```python
3
```

## Approach

We use dynamic programming to compute two arrays:

- `left[i]`: Length of the Longest Increasing Subsequence (LIS) **ending at** index `i`

- `right[i]`: Length of the Longest Decreasing Subsequence (LDS) **starting at** index `i`

A valid mountain peak `i` must have at least one element on both sides, so we require:

- `left[i] > 1` and `right[i] > 1`

For each index `i` that can be a peak, the total mountain length with peak at i is:

```python
left[i] + right[i] - 1
```
(we subtract 1 because `i` is counted twice).

The answer is:
```python
n - max_mountain_length
```
where n = len(nums).

## Complexity
- **Time Complexity:** `O(n²)`

- **Space Complexity:** `O(n)`

## Tags
`dynamic-programming`, `lis`, `lds`, `mountain-array`, `leetcode-hard`