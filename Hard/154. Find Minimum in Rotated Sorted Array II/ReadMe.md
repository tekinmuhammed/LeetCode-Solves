# 154. Find Minimum in Rotated Sorted Array II

**Difficulty:** Hard
**Problem Link:** [LeetCode 154](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/)

---

## Problem
Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. This problem is similar to [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/), but `nums` **may contain duplicates**. 

Given the sorted rotated array `nums` that may contain duplicates, return the **minimum element** of this array. 

You must decrease the overall operation steps as much as possible. 

---

# Approach 

This problem builds directly upon finding the minimum in a rotated sorted array without duplicates. We use **Binary Search**, comparing the middle element (`nums[mid]`) with the rightmost element (`nums[right]`).

However, the presence of duplicates introduces a tricky edge case. What if `nums[mid] == nums[right]`? We can no longer confidently determine whether the minimum element lies in the left half or the right half (e.g., `[3, 1, 3, 3, 3]` vs `[3, 3, 3, 1, 3]`).

Steps: 

1. **Initialize Pointers:** `left = 0` and `right = len(nums) - 1`.
2. **Binary Search Loop:** While `left < right`:
3. **Calculate Midpoint:** `mid = (left + right) // 2`.
4. **Condition 1 (`nums[mid] > nums[right]`):** 
   * The minimum must be strictly to the right. 
   * Update `left = mid + 1`.
5. **Condition 2 (`nums[mid] < nums[right]`):**
   * The right half is sorted correctly, so the minimum is at `mid` or to the left.
   * Update `right = mid`.
6. **Condition 3 (`nums[mid] == nums[right]`):**
   * We hit a duplicate. Since `nums[mid]` and `nums[right]` share the same value, we can safely discard `nums[right]` without losing the minimum value (because `nums[mid]` still holds that value inside the search space). 
   * We shrink the search space by 1: `right -= 1`.
7. **Return:** When `left == right`, we have isolated the minimum element. Return `nums[left]`.

---

# Example Walkthrough 

Consider an array with duplicates: `nums = [3, 3, 1, 3]`

* **Iteration 1:** 
  * `left = 0`, `right = 3`
  * `mid = (0 + 3) // 2 = 1` -> `nums[mid] = 3`
  * `nums[right] = nums[3] = 3`
  * `nums[mid] == nums[right]` -> We can't be sure which half holds the minimum. But we can discard `right`.
  * Update `right -= 1` -> `right = 2`.
* **Iteration 2:** 
  * `left = 0`, `right = 2`
  * `mid = (0 + 2) // 2 = 1` -> `nums[mid] = 3`
  * `nums[right] = nums[2] = 1`
  * `nums[mid] > nums[right]` (`3 > 1`) -> The minimum is strictly to the right of `mid`.
  * Update `left = mid + 1` -> `left = 2`.
* **Termination:** `left` (2) is now equal to `right` (2). Loop ends.
* **Return:** `nums[2]` which is `1`.

---

# Complexity Analysis 

Time Complexity 

O(\log N) on average, O(N) worst case. 

In the best and average cases, the search space is halved at each step, yielding $O(\log N)$ time. However, in the worst-case scenario where all elements are identical (e.g., `[2, 2, 2, 2, 2]`), the algorithm triggers the `right -= 1` condition repeatedly, degrading the time complexity to $O(N)$ as it linearly scans the array. 

Space Complexity 

O(1) 

The algorithm operates in-place, requiring only a few integer variables (`left`, `right`, `mid`) regardless of the array's size. 

---

# Code 

```python
class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            
            elif nums[mid] < nums[right]:
                right = mid
            
            else:
                right -= 1
        
        return nums[left]
```