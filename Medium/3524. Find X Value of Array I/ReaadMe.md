# 3524. Find X Value of Array I

**Difficulty:** Medium 
**Problem Link:** [LeetCode 3524](https://leetcode.com/problems/find-x-value-of-array-i/description/)

---

## Problem
Given an integer array `nums` and an integer `k`, you need to calculate the number of contiguous subarrays that yield a specific product modulo `k`. 

Return an array `result` of size `k`, where `result[x]` represents the total number of contiguous subarrays of `nums` such that the product of their elements modulo `k` is exactly `x`.

---

# Approach

To efficiently find the product of all possible contiguous subarrays modulo `k`, we can use **Dynamic Programming (DP)**. Instead of recalculating the product for every subarray from scratch, we build upon the products of the subarrays that ended at the previous index.

Steps:
1. **Initialize Arrays**: 
   * `result`: An array of size `k` to store the total global count for each remainder.
   * `dp`: An array of size `k` representing the current state. `dp[r]` stores the number of contiguous subarrays *ending exactly at the previous index* whose product modulo `k` is `r`.
2. **Iterate through `nums`**: For each number at index `i`, we create a new state array `ndp` (next DP) initialized to all zeros.
3. **Single Element Subarray**: The element at `nums[i]` can form a valid contiguous subarray all by itself. We calculate its remainder `nums[i] % k` and increment `ndp[nums[i] % k]` by 1.
4. **Extend Previous Subarrays**: For every possible remainder `r` from `0` to `k-1` that was formed by subarrays ending at index `i-1` (which are stored in `dp[r]`), we extend them by multiplying with `nums[i]`. The new remainder becomes `(r * nums[i]) % k`. We add the count `dp[r]` to `ndp[(r * nums[i]) % k]`.
5. **Update State and Accumulate**: 
   * Set `dp = ndp` to prepare for the next iteration.
   * Add the counts in the current `dp` state to our global `result` array.

---

# Code

```python
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [0] * k
        # Initial state: no elements have been processed, so no non-empty subarray exists.
        dp = [0] * k

        for i in range(n):
            ndp = [0] * k  # Current state (rolling array).

            # 1. A subarray can start and end at the current element
            ndp[nums[i] % k] += 1

            # 2. Extend subarrays that ended at the previous index
            for r in range(k):
                ndp[(r * nums[i]) % k] += dp[r]

            dp = ndp  # Update the state.

            # Accumulate the answer.
            for r in range(k):
                result[r] += dp[r]
                
        return result
```

---

# Example Walkthrough

Let's trace `nums = [1, 2, 3]`, `k = 3`.

**Initial state:** `result = [0, 0, 0]`, `dp = [0, 0, 0]`

1. **i = 0, nums[0] = 1**
   * `ndp[1 % 3] += 1` $\rightarrow$ `ndp = [0, 1, 0]`
   * (Extension loop adds nothing since `dp` is all zeros)
   * `dp = [0, 1, 0]`
   * `result = [0, 1, 0]` (Subarrays: `[1]` -> prod 1)

2. **i = 1, nums[1] = 2**
   * `ndp[2 % 3] += 1` $\rightarrow$ `ndp[2] = 1`
   * Extend previous: `r = 1`, `dp[1] = 1`. New remainder: `(1 * 2) % 3 = 2`.
   * `ndp[2] += dp[1]` $\rightarrow$ `ndp[2] = 2`
   * `dp = [0, 0, 2]`
   * `result = [0, 1, 2]` (New subarrays: `[2]` -> prod 2, `[1, 2]` -> prod 2)

3. **i = 2, nums[2] = 3**
   * `ndp[3 % 3] += 1` $\rightarrow$ `ndp[0] = 1`
   * Extend previous: `r = 2`, `dp[2] = 2`. New remainder: `(2 * 3) % 3 = 0`.
   * `ndp[0] += dp[2]` $\rightarrow$ `ndp[0] = 1 + 2 = 3`
   * `dp = [3, 0, 0]`
   * `result = [3, 1, 2]` (New subarrays: `[3]` -> prod 3, `[2, 3]` -> prod 6, `[1, 2, 3]` -> prod 6. All yield remainder 0).

**Final Result**: `[3, 1, 2]`
* Remainder 0: 3 subarrays
* Remainder 1: 1 subarray
* Remainder 2: 2 subarrays

---

# Complexity Analysis

Time Complexity

O(N * K)

Where `N` is the length of `nums` and `K` is the modulo integer. For each of the `N` elements, we iterate `K` times to extend the previous states.

Space Complexity

O(K)

We maintain three arrays of size `K` (`result`, `dp`, and `ndp`). The space does not scale with the length of the input array `nums`, making the space complexity strictly proportional to `K`.