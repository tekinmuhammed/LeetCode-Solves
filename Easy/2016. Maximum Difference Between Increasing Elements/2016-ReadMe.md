# 2016. Maximum Difference Between Increasing Elements

**Link:** [LeetCode 2016](https://leetcode.com/problems/maximum-difference-between-increasing-elements/)  
**Difficulty:** Easy

---

## Problem Description

You are given a **0-indexed** integer array `nums` of size `n`. You need to find the **maximum difference** between two elements `nums[j] - nums[i]` such that:

- `0 <= i < j < n`
- `nums[i] < nums[j]`

Return the maximum difference. If no such pair exists, return `-1`.

---

## Example

### Example 1:
```python
Input: nums = [7,1,5,4]
Output: 4
```
**Explanation:**
- The pair (1, 5) satisfies nums[1] < nums[2] and difference is 5 - 1 = 4

### Example 2:
```python
Input: nums = [9,4,3,2]
Output: -1
```
**Explanation:**
- No increasing pair exists

---

## Constraints

- `2 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^9`

---

## Approach

- Iterate through the array while keeping track of the minimum value seen so far (`min_val`).
- At each step, calculate the difference between the current number and `min_val` if the current number is greater.
- Keep updating the `max_diff` accordingly.
- If no increasing pair is found, return `-1`.

This is similar to a "best time to buy and sell stock" pattern, where you buy at `min_val` and sell at the current index.

---

### Time and Space Complexity

- **Time Complexity:** `O(n)`, where `n` is the length of the input list.

- **Space Complexity:** `O(1)`, only constant space is used.

### Tags
`Greedy`, `Array`, `One-Pass`

### Notes
- This is a common sliding minimum pattern.

- The initial `min_val` is the first element, and we try to find the largest difference with future elements.