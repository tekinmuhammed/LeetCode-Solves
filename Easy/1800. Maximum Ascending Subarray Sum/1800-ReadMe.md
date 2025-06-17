# 🔼 LeetCode 1800 - Maximum Ascending Subarray Sum

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1800](https://leetcode.com/problems/maximum-ascending-subarray-sum/)

---

## 🧩 Problem Description

Given an array of positive integers `nums`, return the **maximum sum** of any **strictly ascending subarray**.

A subarray is a contiguous sequence of elements. A subarray is strictly ascending if each element is strictly greater than the one before.

---

## 🔍 Example

### Input:
```python
nums = [10, 20, 30, 5, 10, 50]
```

### Output:
`65`

###  Explanation:

- Ascending subarrays: `[10,20,30]`, `[5,10,50]`

- Their sums: `60`, `65`

- Maximum: `65`

### 🧠 Approach & Intuition
The idea is to iterate through the array and:

- Accumulate a running `current_sum` for ascending sequences.

- If the current number is not greater than the previous, reset `current_sum`.

- Track the maximum sum seen so far in `max_sum`.

### ⏱️ Complexity

- **Time Complexity:** `O(n)`
Single pass through the list.

- **Space Complexity:** `O(1)`
Only a few variables used.

### 🏷️ Tags
`array`, `greedy`, `prefix-sum`, `subarray`