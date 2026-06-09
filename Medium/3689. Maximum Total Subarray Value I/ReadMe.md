# 3689. Maximum Total Subarray Value I

**Difficulty:** Medium
**Problem Link:** [LeetCode 3689](https://leetcode.com/problems/maximum-total-subarray-value-i/description/)

---

## Problem
You are given an integer array `nums` of length `n` and an integer `k`. You need to choose exactly `k` non-empty subarrays of `nums`. 
* Subarrays may overlap.
* The **exact same** subarray can be chosen more than once.

The value of a subarray is defined as: `max(subarray) - min(subarray)`.
The total value is the sum of the values of all chosen subarrays. 

Return the maximum possible total value you can achieve.
 
--- 
 
# Approach 
 
A brute-force approach to finding and evaluating all $O(N^2)$ subarrays would be incredibly slow and lead to a Time Limit Exceeded (TLE) error. However, a critical observation in the problem's constraints turns this into an extremely simple mathematical/greedy problem: **You can choose the exact same subarray multiple times.**
 
Steps: 
 
1. **Upper Bound of a Subarray Value:** The value of any subarray is its maximum element minus its minimum element. Therefore, the absolute maximum value *any* subarray could possibly have is bounded by the **Global Maximum** of the entire array minus the **Global Minimum** of the entire array.
2. **Finding the Optimal Subarray:** Is there always a subarray that gives this maximum value? Yes! The entire array `nums` itself (or a specific subarray containing both the global min and global max) naturally yields this exact difference.
3. **Greedy Maximization:** Since we want to maximize the sum of `k` subarray choices, and we are allowed to pick the exact same subarray repeatedly, the most optimal strategy is to simply find the subarray with the maximum possible value and pick it `k` times.
4. **Result Calculation:** The answer is straightforwardly `(Global Maximum - Global Minimum) * k`.
 
--- 
 
# Example Walkthrough 
 
Consider `nums = [4, 2, 5, 1]` and `k = 3`.

1. Find the global minimum: `m1 = min(nums) = 1`
2. Find the global maximum: `m2 = max(nums) = 5`
3. The absolute maximum value any single subarray can yield is `5 - 1 = 4`. (We can achieve this by choosing the subarray `[4, 2, 5, 1]` or `[5, 1]`).
4. To maximize our total for `k = 3` choices, we simply choose this optimal subarray 3 times: 
   * Choice 1: Value = 4 
   * Choice 2: Value = 4
   * Choice 3: Value = 4 
5. Total Maximum Value = `4 * 3 = 12`.
 
--- 
 
# Complexity Analysis 
 
Time Complexity 
 
O(N) 
 
Where `N` is the length of the `nums` array. The built-in `min()` and `max()` functions scan the array exactly once. Thus, the overall time complexity is strictly linear. *(Note: Python's built-in functions are implemented in C and are highly optimized, making two passes $O(2N)$ perfectly efficient for this problem).*
 
Space Complexity 
 
O(1)  
 
We do not generate any subarrays or use any auxiliary data structures. We only store the `m1` and `m2` integers, which requires constant extra space.
 
--- 

# Code

```python
from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        m1 = min(nums)
        m2 = max(nums)
        return (m2 - m1) * k
```