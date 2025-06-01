# 🟨 LeetCode 2762 - Continuous Subarrays

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2762](https://leetcode.com/problems/continuous-subarrays/)

---

## 📘 Problem Description

You are given an integer array `nums`. A subarray is considered **valid** if the **absolute difference between the maximum and minimum elements is less than or equal to 2**.

Return the **total number of valid subarrays** in `nums`.

---

## 🧪 Example

### Input
```python
nums = [1, 3, 2, 3, 2]
```

### Output
`11`

### Explanation
There are 11 valid subarrays, such as:

- [1], [3], [2], [3], [2]

- [1,3], [3,2], [2,3], [3,2]

- [2,3,2], [3,2,3]

### 🚀 Approach
We use a sliding window with two **monotonic deques** to keep track of:

- The **minimum element** in the current window.

- The **maximum element** in the current window.

**Steps:**
1. Initialize `left` pointer at 0.

1. For each `right` index:

- Maintain the min and max deques in monotonic order.

- While the difference between max and min exceeds 2, move the `left` pointer forward and update deques.

- Add `right - left + 1` to the total count (number of valid subarrays ending at `right`).

### ⏱️ Complexity
- **Time Complexity:** `O(n)`

- - Each index is pushed and popped from the deque at most once.

- **Space Complexity:** `O(n)`

- - For the two deques.

### 🏷️ Tags
`sliding-window`, `deque`, `monotonic-queue`, `array`, `leetcode-medium`