# 🔄 LeetCode 2460 - Apply Operations to an Array

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2460](https://leetcode.com/problems/apply-operations-to-an-array)

---

## 📘 Problem Description

You are given a 0-indexed array `nums` of size `n` consisting of **non-negative integers**.

You must apply the following operation **exactly once** to each pair of consecutive elements:

- If `nums[i] == nums[i + 1]`, then:
  - `nums[i] = 2 * nums[i]`
  - `nums[i + 1] = 0`

After applying the operations, move all `0`s to the end of the array while maintaining the relative order of the non-zero elements.

Return the resulting array.

---

## 🧪 Example

### Input:

```python
nums = [1, 2, 2, 1, 1, 0]
```

### Output:

```python
[1, 4, 2, 0, 0, 0]
```

### Explanation:

- Apply operation: `[1, 4, 0, 2, 1, 0]`

- Move zeros to the end: `[1, 4, 2, 1, 0, 0]` → mistake

- Correct steps:

- - After applying operations:

- - - `2 == 2 → [1, 4, 0, 1, 1, 0]`

- - - `1 == 1 → [1, 4, 0, 2, 0, 0]`

- - Then move zeros: `[1, 4, 2, 0, 0, 0]`

### 🚀 Approach

1. Iterate through the array:

- If two consecutive elements are equal, apply the operation.

2. After the pass, move all zeros to the end:

- Filter out non-zero elements and append required zeros.

### ⏱️ Complexity

- **Time Complexity:** `O(n)`

- **Space Complexity:** `O(n)` (for the result array)

### 🏷️ Tags

`array`, `simulation`, `two-pointers`, `leetcode-easy`