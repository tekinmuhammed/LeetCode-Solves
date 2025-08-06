# 🏚️ LeetCode 2560 - House Robber IV

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2560](https://leetcode.com/problems/house-robber-iv)

---

## 📘 Problem Description

You are given an array `nums` representing the amount of money at each house, and an integer `k`. You must rob **at least `k` non-adjacent** houses such that the **maximum amount of money robbed from any single house is minimized**.

---

## 🧪 Examples

### Example 1:
```python
Input: nums = [2,3,5,9], k = 2  
Output: 5  
Explanation: Rob house 0 and 2 (values 2 and 5).
```

### Example 2:
```python
Input: nums = [9,1,1,9,1], k = 2  
Output: 2
```

### 💡 Key Insight

We need to minimize the **maximum amount robbed from any selected house**, while ensuring:

- At least `k` houses are robbed

- No two robbed houses are adjacent

This naturally leads to a **binary search on the answer** — we search for the smallest possible value `X` such that there exists a valid selection of `k` houses with values ≤ `X`.

### 🧠 Approach

1. Use **binary search** on the answer, where `left = min(nums)` and `right = max(nums)`

2. For each mid-value in binary search:

- Check if it's possible to select at least `k` non-adjacent houses with values ≤ `mid`

- If possible, search for a smaller maximum (`right = mid`)

3. Else, search higher (`left = mid + 1`)

### ⏱️ Complexity

- **Time Complexity:** `O(n log(max(nums) - min(nums)))`

- **Space Complexity:** `O(1)`

### 🏷️ Tags

`binary-search`, `greedy`, `dynamic-programming`, `medium`