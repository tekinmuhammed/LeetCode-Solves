# 🟨 LeetCode 1671 - Minimum Number of Removals to Make Mountain Array

**Difficulty:** Hard  
**Problem Link:** [LeetCode 1671](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array)

---

## 📘 Problem Description

You may recall that an array `arr` is a **mountain array** if:

- `arr.length >= 3`
- There exists some index `i` (`0 < i < arr.length - 1`) such that:
  - `arr[0] < arr[1] < ... < arr[i]`
  - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given an integer array `nums`, return **the minimum number of elements to remove** to make `nums` a mountain array.

---

## 🧪 Example

### Input:
```python
nums = [2,1,1,5,6,2,3,1]
```

## Output:
`3`

## 🚀 Approach
We use dynamic programming to calculate:

- `left[i]`: Length of the Longest Increasing Subsequence (LIS) ending at i

- `right[i]`: Length of the Longest Decreasing Subsequence (LDS) starting at i

A valid mountain must have:

- At least one element on both sides of the peak

- `left[i] > 1 and right[i] > 1`

We find the maximum possible mountain length and subtract it from the total to get the minimum removals.

## ⏱️ Complexity
- **Time Complexity:** O(n²)

- **Space Complexity:** O(n)

## 🏷️ Tags
`dynamic-programming`, `lis`, `mountain-array`, `leetcode-hard`