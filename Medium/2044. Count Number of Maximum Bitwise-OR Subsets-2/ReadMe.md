# 2044. Count Number of Maximum Bitwise-OR Subsets

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2044](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/)

---

## Problem Description

You are given an array of integers `nums`. You need to return the **number of non-empty subsets** of `nums` such that the **bitwise OR** of all the elements in the subset is **equal to the maximum possible OR** of any subset of `nums`.

---

### Example

**Input:**
```python
nums = [3,1]
```

**Output:**
```python
2
```

### Explanation:

- Possible subsets: [3], [1], [3,1]

-  OR values: 3, 1, 3

- Maximum OR is 3, and occurs in 2 subsets: [3], [3,1]

### Approach

We perform a **Depth-First Search (DFS)** to explore all possible subsets of the array.

- At each step, we choose to either:

1. **Include** the current number in the subset.

2. **Exclude** the current number.

- We track the OR value as we go, and when we reach the end of a subset, we:

- - Compare the current OR with the max OR seen so far.

- - Update the count accordingly.

### Why DFS?

DFS is well-suited for generating and evaluating all subsets (2^n possibilities), especially when n ≤ 16.

### Complexity

- **Time Complexity:** `O(2^n)`, where `n = len(nums)`

- **Space Complexity:** `O(n)` (for recursion stack)

### Tags

`Backtracking`, `Bit-Manipulation`, `DFS`, `Recursion`, `Combinatorics`

### Notes

- The key idea is recognizing that the maximum OR can be computed first, and all subsets can be tested for matching that value.

- Efficient due to small input constraints (typically n ≤ 16).