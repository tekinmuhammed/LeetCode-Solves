# 📊 LeetCode 2161 - Partition Array According to Given Pivot

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2161](https://leetcode.com/problems/partition-array-according-to-given-pivot)

---

## 📘 Problem Description

You are given a **0-indexed** integer array `nums` and an integer `pivot`. You need to **rearrange** the elements of `nums` such that:

1. Every element **less than** `pivot` appears **before** every element **equal to** `pivot`,
2. Every element **equal to** `pivot` appears **before** every element **greater than** `pivot`,
3. The **relative order** of elements less than `pivot` and elements greater than `pivot` is **preserved**.

Return the modified array after rearranging it.

---

## 🧪 Example

### Input:
```python
nums = [9,12,5,10,14,3,10]
pivot = 10
```

### Output:

```python
[9, 5, 3, 10, 10, 12, 14]
```

### Explanation:

- Elements less than 10: `[9, 5, 3]`

- Elements equal to 10: `[10, 10]`

- Elements greater than 10: `[12, 14]`

- Final array: `[9, 5, 3, 10, 10, 12, 14]`

### 🚀 Approach

- Traverse the array three times:

- 1. First pass: Collect elements less than the pivot.

- 2. Second pass: Collect elements equal to the pivot.

- 3. Third pass: Collect elements greater than the pivot.

- Concatenate the three lists to produce the result.

### ⏱️ Complexity

- **Time Complexity:** `O(n)`

- **Space Complexity:** `O(n)`

### 🏷️ Tags
`array`, `sorting`, `stable-partition`, `leetcode-medium`