# 2616. Minimize the Maximum Difference of Pairs

**Problem Link:** [LeetCode 2616](https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/)  
**Difficulty:** Medium

---

## Problem Description

You are given a **0-indexed** integer array `nums` and an integer `p`.

Form `p` **pairs** of indices such that each element in `nums` is in at most one pair.  
A pair of indices `(i, j)` is **valid** if `abs(nums[i] - nums[j]) <= threshold`.

Your task is to **minimize the maximum difference** among all such `p` pairs.

Return the **minimum possible value of the maximum difference**.

---

## Example

```python
Input: nums = [10, 1, 2, 7, 1, 3], p = 2
Output: 1
```

### Explanation:

- We can form pairs: `(1,2)` and `(4,5)` → differences: abs(1-2)=1 and abs(1-3)=2 → max=`2`

- But if we form (1,2) and (0,4): abs(1-2)=1 and abs(10-1)=9 → max=`9`

- The optimal solution is `(1,2)` and `(4,5)` → max diff = `1`.

---

## Approach

- **Step 1:** Sort the array. This ensures the closest values are next to each other.
- **Step 2:** Use **binary search** on the range of possible maximum differences (from `0` to `max(nums) - min(nums)`).
- **Step 3:** For each candidate max difference (`threshold`), try to form `p` valid pairs greedily:
    - Iterate over sorted array
    - If a pair `(nums[i-1], nums[i])` has difference ≤ threshold, use it and skip both.
- **Step 4:** If at least `p` pairs can be formed, try a smaller threshold (move left).
- Otherwise, increase the threshold (move right).

---

### Complexity
- **Time Complexity:**

- - Sorting: O(N log N)

- - Binary Search: O(log M × N), where M = max difference, N = len(nums)

- **Space Complexity:** `O(1)`

- - Only variables are used, no extra space beyond input.

### Tags
`Greedy`, `Binary-Search`, `Sorting`

### Notes
- This problem is a great example of using binary search on the **answer space**.

- Greedy pairing after sorting ensures that small differences are prioritized first.