# 🌟 LeetCode 2401 - Longest Nice Subarray

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2401](https://leetcode.com/problems/longest-nice-subarray)

---

## 📝 Problem Description

You are given an array of integers `nums`.

A **subarray** is called **"nice"** if the bitwise AND of any two elements is `0`.

👉 **Goal:** Return the length of the **longest nice subarray**.

---

## 🔍 Example

```python
Input: nums = [1, 3, 8, 48, 10]
Output: 3
Explanation:
The subarray [3, 8, 48] is nice because:
- 3 & 8 == 0
- 3 & 48 == 0
- 8 & 48 == 0
```

### 💡 Intuition

Two numbers `a` and `b` are bitwise independent if `(a & b) == 0`.

To maximize the length of a subarray that satisfies this condition:

- We use the **sliding window** technique.

- We maintain a **bitmask** to represent the OR of the current window elements.

- If `bitmask & nums[right] != 0`, we shrink the window from the left.

### 🔨 Approach

1. Initialize a `bitmask = 0`, and window pointers `left = 0`, `max_len = 0`.

2. For each `right` index in `nums`:

- While the current number overlaps in bits with the current window (`bitmask & nums[right] != 0`), shrink the window from the left.

- Update `bitmask` to include the current number.

- Track the maximum window size.

### ⏱️ Complexity

- **Time Complexity:** `O(n * 32)` → Worst case is shrinking 32-bit integers.

- **Space Complexity:** `O(1)` → Only a few integers are used.

### 🏷️ Tags

`bit-manipulation`, `sliding-window`, `greedy`, `medium`