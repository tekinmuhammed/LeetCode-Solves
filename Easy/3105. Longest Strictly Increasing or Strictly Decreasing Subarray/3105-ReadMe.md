# 📈 LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray

**Difficulty:** Easy  
**Problem Link:** [LeetCode 3105](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/)

---

## 🧩 Problem Description

Given an array `nums`, return the length of the longest **strictly increasing** or **strictly decreasing** contiguous subarray.

---

## 🔍 Example

### Input:
```python
nums = [1, 4, 7, 3, 2, 6, 7]
```
### Output:
`3`

### Explanation:

- Longest strictly increasing subarray: `[1, 4, 7]`

- Longest strictly decreasing subarray: `[7, 3, 2]`

### 🧠 Approach & Intuition

We iterate through the array while keeping track of:

- `inc_length`: length of current increasing sequence

- `dec_length`: length of current decreasing sequence

- `max_length`: overall longest length seen so far

#### Key rules:
- If `nums[i] > nums[i - 1]`: it's part of an increasing streak.

- If `nums[i] < nums[i - 1]`: it's part of a decreasing streak.

- Otherwise, reset both counters to 1.

### ⏱️ Complexity

- **Time Complexity:** `O(n)`
One pass through the array.

- **Space Complexity:** `O(1)`
Constant space used for counters.

### 🏷️ Tags
`array`, `sliding-window`, `greedy`, `sequence`, `monotonic`