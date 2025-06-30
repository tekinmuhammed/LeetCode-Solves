# 🔄 LeetCode 3355 - Zero Array Transformation I

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3355](https://leetcode.com/problems/zero-array-transformation-i)

---

## 📘 Problem Description

Given an integer array `nums` and a list of `queries`, each query is a range `[l, r]` meaning that you can **decrease** each element in `nums[l..r]` by 1 **once**.

You can apply all queries in any order.

Your task is to determine if it's possible to make the **entire array equal to zero** after applying all queries.

---

## ✅ Constraints

- `1 <= nums.length <= 10⁵`
- `0 <= nums[i] <= 10⁹`
- `1 <= queries.length <= 10⁵`
- `0 <= l <= r < nums.length`

---

## 🧠 Approach

We track how many times each index will be decremented using a **prefix sum array** (a common range update trick):

1. Initialize an `ops` array of size `n + 1` to store the number of times each index is decremented.
2. For each query `[l, r]`, increment `ops[l]` and decrement `ops[r + 1]` to represent a range update.
3. Build the prefix sum of `ops` so that `ops[i]` represents the total number of times index `i` will be decremented.
4. For each index `i`, check if `nums[i]` is less than or equal to `ops[i]`. If not, return `False`.

---

### ⏱️ Time and Space Complexity

- **Time Complexity:** `O(n + q)`
Where n is the length of nums and q is the number of queries.

- **Space Complexity:** `O(n)`

### 📌 Example
```python
Input:
nums = [2, 1, 1]
queries = [[0, 1], [1, 2]]

Output: True

Explanation:
Apply [0,1]: nums becomes [1,0,1]
Apply [1,2]: nums becomes [1,-1,0] → but we only count total decrements at each index.
Total decrements = [1,2,1], original nums = [2,1,1]
All nums[i] <= decrements[i], so return True.
```

### 🏷️ Tags
`prefix-sum`, `greedy`, `range-update`, `array`, `simulation`