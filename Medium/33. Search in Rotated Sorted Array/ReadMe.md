# 33. Search in Rotated Sorted Array

**Difficulty:** Medium  
**Problem Link:** [LeetCode 33](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)

---

## Problem
There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). 

For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

---

# Approach

To achieve an $O(\log n)$ time complexity, we must use **Binary Search**. However, because the array is rotated, a standard binary search won't work directly. 

The key insight is that if you divide a rotated sorted array into two halves, **at least one of the halves will always be perfectly sorted**.

Steps:

1. **Initialize Pointers:** Set `l = 0` (left) and `r = len(nums) - 1` (right).
2. **Binary Search Loop:** Run the loop while `l <= r`.
3. **Calculate Midpoint:** Find `m = l + (r - l) // 2`. If `nums[m] == target`, we found our target, return `m`.
4. **Identify the Sorted Half:**
   * **Condition 1 (`nums[m] < nums[r]`):** This implies that the **right half** (from `m` to `r`) is perfectly sorted without any rotation drops.
     * Check if the `target` falls within the range of this sorted right half (`nums[m] < target <= nums[r]`).
     * If it does, we narrow our search space to the right (`l = m + 1`).
     * If it doesn't, the target must be in the left half (`r = m - 1`).
   * **Condition 2 (`nums[m] >= nums[r]`):** This implies that the **left half** (from `l` to `m`) is perfectly sorted.
     * Check if the `target` falls within the range of this sorted left half (`nums[l] <= target < nums[m]`).
     * If it does, we narrow our search space to the left (`r = m - 1`).
     * If it doesn't, the target must be in the right half (`l = m + 1`).
5. **Not Found:** If the loop terminates and we haven't returned an index, it means the `target` is not in the array. Return `-1`.

---

# Example Walkthrough

Consider `nums = [4, 5, 6, 7, 0, 1, 2]` and `target = 0`

* **Iteration 1:**
  * `l = 0`, `r = 6`, `m = 3` -> `nums[m] = 7`.
  * Target (`0`) is not `7`.
  * Check sorted half: `nums[m]` (7) is NOT `< nums[r]` (2). So the **left half is sorted** (`[4, 5, 6, 7]`).
  * Check target bounds: Is `target` (0) between `nums[l]` (4) and `nums[m]` (7)? **No.**
  * Thus, target must be in the right half. Update `l = m + 1 = 4`.
  
* **Iteration 2:**
  * `l = 4`, `r = 6`, `m = 5` -> `nums[m] = 1`.
  * Target (`0`) is not `1`.
  * Check sorted half: `nums[m]` (1) IS `< nums[r]` (2). So the **right half is sorted** (`[1, 2]`).
  * Check target bounds: Is `target` (0) between `nums[m]` (1) and `nums[r]` (2)? **No.**
  * Thus, target must be in the left half. Update `r = m - 1 = 4`.

* **Iteration 3:**
  * `l = 4`, `r = 4`, `m = 4` -> `nums[m] = 0`.
  * `nums[m] == target` (`0 == 0`). Match found!
  * Return `4`.

---

# Complexity Analysis

Time Complexity

O(\log N)

At each step, we divide the search space in half. Determining which half to discard only requires checking a few boundary values, taking constant time $O(1)$. Thus, the overall time complexity is strictly logarithmic.

Space Complexity

O(1)

The algorithm uses an iterative approach with only three pointer variables (`l`, `r`, `m`), resulting in constant extra space usage.

---

# Code

```python
class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            
            if nums[m] == target:
                return m
            
            # Check if the right half is sorted
            if nums[m] < nums[r]:
                # Check if target is in the sorted right half
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            # Otherwise, the left half must be sorted
            else:
                # Check if target is in the sorted left half
                if nums[m] > target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
                    
        return -1
```

```