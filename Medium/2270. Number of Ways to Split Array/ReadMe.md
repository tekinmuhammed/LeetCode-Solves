# 🟨 LeetCode 2270 - Number of Ways to Split Array

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2270](https://leetcode.com/problems/number-of-ways-to-split-array)

---

## 📘 Problem Description

Given an array `nums`, your task is to count the number of **valid split points** where you can split the array into two non-empty parts such that:

sum(left part) ≥ sum(right part)

More formally, for index `i` (0 ≤ i < len(nums) - 1), count how many times the sum of `nums[0] to nums[i]` is **greater than or equal to** the sum of `nums[i+1] to end`.

---

## 🧪 Example

### Input:
```python
nums = [10, 4, -8, 7]
```

### Output:
```python
2
```

### Explanation:

Valid splits are:

- `[10] | [4, -8, 7] → left = 10, right = 3 ✅`

- `[10, 4] | [-8, 7] → left = 14, right = -1 ✅`

- `[10, 4, -8] | [7] → left = 6, right = 7 ❌`

### 🚀 Approach

1. Compute the total sum of the array.

2. Iterate through the array (except the last index).

3. Maintain a running `left_sum` and compute `right_sum` as `total_sum - left_sum`.

4. If `left_sum ≥ right_sum`, increment a counter.

### ⏱️ Complexity

- **Time Complexity:** `O(n)`
(One pass to calculate total sum, one pass to count valid splits)

- **Space Complexity:** `O(1)`
(Constant extra space used)

### 🏷️ Tags

`prefix-sum`, `array`, `greedy`, `leetcode-easy`