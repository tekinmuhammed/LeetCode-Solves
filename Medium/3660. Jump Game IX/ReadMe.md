# 3660. Jump Game IX

**Difficulty:** Hard  
**Problem Link:** [LeetCode 3660](https://leetcode.com/problems/jump-game-ix/description/)

---

## Problem
You are given an integer array `nums` of length `n`. The goal is to determine an array `ans` of the same length, where `ans[i]` represents the maximum reachable value or optimal score starting from index `i`, subject to specific jump constraints. 

*(Note: In this variation of Jump Game, the constraints involve maintaining bounds based on the maximum values to the left and minimum values to the right of the current position.)*

Return the array `ans`.

---

# Approach

This solution utilizes a **Divide and Conquer** strategy processed from right to left, relying heavily on **Prefix Maximums** to partition the array into valid segments.

Steps:

1. **Prefix Maximums (`prev_max`):** 
   * First, we iterate through the array from left to right to build a `prev_max` array.
   * For each index `i`, we store a tuple `(value, index)` representing the maximum value seen so far from index `0` up to `i`, and the exact index where this maximum occurs.

2. **Right-to-Left Partitioning:**
   * We process the array from the end (`n - 1`) down to the beginning using a recursive `process` function.
   * At any given right boundary `r`, we look up the maximum element in the prefix `nums[0..r]`. The index of this maximum element becomes our `pivot_index`.
   * This effectively splits our current working range into a segment `[pivot_index, r]` and a remaining left part `[0, pivot_index - 1]`.

3. **Constraint Propagation (`right_min` and `right_max`):**
   * As we move from right to left, we carry two bounds: `right_min` and `right_max`.
   * For the current segment `[pivot_index, r]`, we determine its target value (`curr_max`). If the maximum value in this prefix (`p_max`) is less than or equal to `right_min`, the segment is bounded by `p_max`. Otherwise, it falls back to `right_max`.
   * We assign this `curr_max` to all elements in the current segment.

4. **Recursive Step:**
   * Before moving to the left segment, we update our `next_right_min` by taking the minimum of the current `p_max`, the passed `right_min`, and all elements within the current segment.
   * We then recursively process the left part: `process(pivot_index - 1, next_right_min, curr_max)`.

---

# Example Walkthrough

Imagine an arbitrary array processed by this algorithm:

1. **Initialization:** We build `prev_max` so that any index `r` instantly knows the largest value to its left and where it is (`pivot_index`).
2. **First Call (`process(n-1, inf, 0)`):** 
   * We look at the entire array. Let's say the absolute maximum of the whole array is at index `4`.
   * Our segment is `[4, n-1]`. We calculate its `curr_max` and assign it to `ans[4...n-1]`.
   * We find the minimum value in this segment to update `next_right_min`.
3. **Second Call (`process(3, next_right_min, curr_max)`):**
   * We now look at the prefix `[0..3]`. We find its maximum, say at index `1`.
   * Our new segment is `[1, 3]`. We assign its calculated `curr_max` to `ans[1...3]`.
4. **Termination:** This continues until `pivot_index == 0`, meaning we have processed the very first element.

---

# Complexity Analysis

Time Complexity

O(N)

Building the `prev_max` array takes linear time. During the recursive `process` function, every element in the array is iterated over exactly once in the inner `for` loop to assign values to `ans` and calculate `next_right_min`. Thus, the overall time complexity is strictly linear.

Space Complexity

O(N)

We use O(N) space for the `ans` array and O(N) space for the `prev_max` array. Additionally, the maximum depth of the recursion stack in the worst case (e.g., a strictly decreasing array where `pivot_index` only decreases by 1 each time) is O(N).

---

# Code
```python
import math
from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [0] * n
        # [value, index]
        prev_max = [(0, 0)] * n

        prev = (-math.inf, -1)
        for i, value in enumerate(nums):
            if value > prev[0]:
                prev = (value, i)
            prev_max[i] = prev

        def process(r: int, right_min: float, right_max: float) -> None:
            p_max, pivot_index = prev_max[r]
            curr_max = p_max if p_max <= right_min else right_max

            next_right_min = min(p_max, right_min)
            for i in range(pivot_index, r + 1):
                ans[i] = curr_max
                next_right_min = min(next_right_min, nums[i])

            if pivot_index == 0:
                return

            process(pivot_index - 1, next_right_min, curr_max)

        process(n - 1, math.inf, 0)

        return ans
```