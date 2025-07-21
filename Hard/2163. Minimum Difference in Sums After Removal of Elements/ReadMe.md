# 2163. Minimum Difference in Sums After Removal of Elements

**Difficulty:** Hard  
**Problem Link:** [LeetCode 2163](https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/)

---

## Problem Description

You are given an array `nums` of length `3 * n`. You need to remove exactly `n` elements from `nums` (while maintaining the relative order of the remaining elements) such that the **difference** between the sum of the first `n` elements and the sum of the last `n` elements of the remaining array is minimized.

Return the **minimum possible difference**.

---

## Approach

The key idea is to split the array into three parts:
- The left part (first `n` elements),
- The middle part (next `n` elements),
- The right part (last `n` elements).

We want to choose which `n` elements to remove (specifically from the middle part) such that after removal:
- The **sum of the first `n` numbers** (from the left side, possibly adjusted by choices in the middle) is maximized.
- The **sum of the last `n` numbers** (from the right side, after removal) is minimized.

To achieve this:
1. **Left Part (Prefix Processing):**  
   - Consider the first `2 * n` elements.
   - Use a **max-heap** to select the best `n` elements (largest sum) that can form the left part.
   - Compute a prefix array `part1` where each entry represents the maximum sum achievable for the left half up to a given index.

2. **Right Part (Suffix Processing):**  
   - Consider the last `2 * n` elements.
   - Use a **min-heap** to choose the best `n` elements (smallest sum) for the right part.
   - Compute a suffix sum `part2` for the right half.

3. **Combine:**  
   - Evaluate every possible valid split between the two parts and compute the difference:  
     **difference = (sum of chosen left part) - (sum of chosen right part)**
   - The answer is the minimum such difference over all valid splits.

---

### Complexity

- **Time Complexity:**

- - `O(n log n)` due to heap operations performed on roughly 2*n elements.

- **Space Complexity:**

- - `O(n)` for storing the prefix sums and heaps.

### Tags

`Dynamic-Programming`, `Heap`, `Greedy`, `Simulation`, `Array`

### Notes

- This solution uses two heaps: a max-heap to maximize the sum for the left part and a **min-heap** to minimize the sum for the right part.

- The two passes (prefix and suffix) combined with binary splitting yield the optimal removal strategy.

- The approach leverages the fixed structure of the array (`3*n` elements) and carefully manages which `n` elements to remove to minimize the final difference.