# 2574. Left and Right Sum Differences

**Difficulty:** Easy
**Problem Link:** [LeetCode 2574](https://leetcode.com/problems/left-and-right-sum-differences/description/)

--- 
 
## Problem
Given a **0-indexed** integer array `nums`, find a **0-indexed** integer array `answer` where:
* `answer.length == nums.length`.
* `answer[i] = |leftSum[i] - rightSum[i]|`.
 
Where:
* `leftSum[i]` is the sum of elements to the left of the index `i` in the array `nums`. If there is no such element, `leftSum[i] = 0`.
* `rightSum[i]` is the sum of elements to the right of the index `i` in the array `nums`. If there is no such element, `rightSum[i] = 0`.
 
Return the array `answer`. 
 
--- 
 
# Approach 
 
A naive approach would be to calculate the left sum and right sum from scratch for every single index, which would take $O(N^2)$ time. A better approach is to use prefix sums.

While many solutions create two separate arrays (`left_arr` and `right_arr`) to store these prefix and suffix sums, this solution optimizes the space by reusing the output array (`ans`) in a clever **Two-Pass (Left-to-Right and Right-to-Left)** strategy:

1. **First Pass (Left to Right):**
   * We initialize a running total `left_sum` to `0`.
   * We iterate through the array from left to right.
   * For each index `i`, we store the current `left_sum` into `ans[i]`.
   * Then, we add the current element `nums[i]` to `left_sum` for the next iteration.
   * By the end of this pass, `ans` holds all the `leftSum` values.
2. **Second Pass (Right to Left):**
   * We initialize another running total `right_sum` to `0`.
   * We iterate through the array backwards (from `n - 1` down to `0`).
   * For each index `i`, we already have `leftSum[i]` stored in `ans[i]`. We calculate the absolute difference: `abs(ans[i] - right_sum)` and update `ans[i]` with this final result.
   * Then, we add the current element `nums[i]` to `right_sum` for the next iteration.

---

# Example Walkthrough

Consider `nums = [10, 4, 8, 3]`

**Step 1: Left-to-Right Pass**
* `i = 0`: `ans[0] = 0`, `left_sum` becomes `10`
* `i = 1`: `ans[1] = 10`, `left_sum` becomes `14`
* `i = 2`: `ans[2] = 14`, `left_sum` becomes `22`
* `i = 3`: `ans[3] = 22`, `left_sum` becomes `25`
* `ans` array is now: `[0, 10, 14, 22]`

**Step 2: Right-to-Left Pass**
* `i = 3`: `ans[3] = |22 - 0| = 22`, `right_sum` becomes `3`
* `i = 2`: `ans[2] = |14 - 3| = 11`, `right_sum` becomes `11`
* `i = 1`: `ans[1] = |10 - 11| = 1`, `right_sum` becomes `15`
* `i = 0`: `ans[0] = |0 - 15| = 15`, `right_sum` becomes `25`
* `ans` array is now: `[15, 1, 11, 22]`

---

# Complexity Analysis

Time Complexity

O(N)

Where `N` is the length of the `nums` array. We iterate through the array exactly twice (once forward, once backward). Each iteration performs $O(1)$ constant time operations.

Space Complexity

O(1) auxiliary

We allocate an `ans` array of size `N` to store the results. Since this is the required output array, it does not count towards auxiliary space complexity. Aside from that, we only use a few integer variables (`left_sum`, `right_sum`, `n`), keeping the extra space strictly constant.

---

# Code

```python
from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        left_sum = 0
        for i in range(n):
            ans[i] = left_sum
            left_sum += nums[i]

        right_sum = 0
        for i in range(n - 1, -1, -1):
            ans[i] = abs(ans[i] - right_sum)
            right_sum += nums[i]

        return ans
```