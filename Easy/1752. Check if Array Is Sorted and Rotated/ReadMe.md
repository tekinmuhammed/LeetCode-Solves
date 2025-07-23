# 🔁 LeetCode 1752 - Check if Array Is Sorted and Rotated

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1752](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/)

---

## 🧩 Problem Description

Given an array `nums`, return `True` if the array is **sorted in non-decreasing order** and **then rotated** some number of positions (possibly 0). Otherwise, return `False`.

### A sorted and rotated array:

- Is initially sorted in ascending order

- Then some leading elements are moved to the end of the array

---

## 🔍 Example

### Input:
```python
nums = [3, 4, 5, 1, 2]
```

### Output:
```python
True
```

### Explanation:

This is a sorted array `[1, 2, 3, 4, 5]` rotated 3 positions.

### 🧠 Approach & Intuition

To be **sorted and rotated**, the array must:

- Have at **most one point** where the order breaks (i.e., `nums[i] > nums[i+1]`)

We simulate this with a **modulo check**:

- Compare each `nums[i]` with `nums[(i + 1) % n]`

- If there's more than one "drop", it's not a valid sorted-rotated array

### ⏱️ Complexity

- **Time Complexity:** `O(n)`
One pass through the array.

- **Space Complexity:** `O(1)`
No extra space used.

### ✅ Key Insight

An array that is sorted and rotated can have **at most one descent** (i.e., a pair of adjacent elements where the earlier one is greater).

### 🏷️ Tags
`array`, `rotation`, `sorted`, `greedy`, `implementation`