# 3423. Maximum Difference Between Adjacent Elements in a Circular Array

**Problem Link:** [LeetCode 3423](https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/)  
**Difficulty:** Easy

---

## Problem Description

You are given an integer array `nums`.  
Your task is to return the **maximum absolute difference** between any two **adjacent elements**, treating the array as **circular**.

- This means that `nums[n-1]` is adjacent to `nums[0]`.

---

## Example

```python
Input: nums = [10, 1, 5, 9]
Output: 9
Explanation:
Adjacent pairs:
abs(10 - 1) = 9
abs(1 - 5) = 4
abs(5 - 9) = 4
abs(9 - 10) = 1 (circular pair)

Maximum = 9
```

---

## Approach

- Iterate over all adjacent index pairs `(i, (i+1)%n)` where `%n` ensures circular behavior.
- For each pair, compute the absolute difference `abs(nums[i] - nums[j])`.
- Track the maximum of these differences.

---

### Complexity
- **Time Complexity:** `O(N)`
We traverse the array once.

- **Space Complexity:** `O(1)`
Only a few integer variables are used.

### Tags
`Array`, `Simulation`, `Greedy`, `Math`

### Notes
- The use of modulo `%` is key to handling the circular nature of the array.

- Be careful when the array has only 1 element (edge case).