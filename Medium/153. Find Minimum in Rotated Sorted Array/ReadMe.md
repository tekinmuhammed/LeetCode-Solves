# 153. Find Minimum in Rotated Sorted Array

**Difficulty:** Medium
**Problem Link:** [LeetCode 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

---

## Problem 
Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
* `[4,5,6,7,0,1,2]` if it was rotated 4 times. 
* `[0,1,2,4,5,6,7]` if it was rotated 7 times. 

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return the **minimum element** of this array. 

You must write an algorithm that runs in `O(log n)` time. 

---

# Approach 

To achieve an $O(\log N)$ time complexity, we must use **Binary Search**.

In a standard sorted array, `nums[left] < nums[right]`. However, in a rotated sorted array, the array is split into two perfectly sorted halves, where all elements in the left half are strictly greater than all elements in the right half.

The core idea is to compare the middle element (`nums[mid]`) with the rightmost element (`nums[right]`) to determine which half of the array contains the minimum value:

1. **Initialize Pointers:** Set `left = 0` and `right = len(nums) - 1`.
2. **Binary Search Loop:** Run the loop as long as `left < right`.
3. **Calculate Midpoint:** Find `mid = (left + right) // 2`.
4. **Condition 1 (`nums[mid] > nums[right]`):** 
   * This means the middle element is greater than the rightmost element. This anomaly is only possible if the `mid` element is part of the "larger" left half, meaning the drop-off point (the minimum element) is strictly to the right. 
   * We update `left = mid + 1`.
5. **Condition 2 (`nums[mid] <= nums[right]`):**
   * This means the middle element is less than or equal to the rightmost element. This indicates that the right half is properly sorted without any drop-offs. Thus, the minimum element must be exactly at `mid` or somewhere to the left of `mid`.
   * We update `right = mid`. *(Note: We do not do `mid - 1` because `nums[mid]` itself could be the minimum).*
6. **Return:** When the loop terminates (`left == right`), the pointers converge perfectly on the minimum element. We return `nums[left]`.

---

# Example Walkthrough 

Consider `nums = [3, 4, 5, 1, 2]`

* **Initial State:** `left = 0`, `right = 4`
* **Iteration 1:**
  * `mid = (0 + 4) // 2 = 2` -> `nums[mid] = 5`
  * `nums[right] = nums[4] = 2`
  * `5 > 2` is True. The minimum is to the right.
  * Update `left = mid + 1 = 3`.
* **Iteration 2:**
  * `left = 3`, `right = 4`
  * `mid = (3 + 4) // 2 = 3` -> `nums[mid] = 1`
  * `nums[right] = nums[4] = 2`
  * `1 > 2` is False. The minimum is at `mid` or to the left.
  * Update `right = mid = 3`.
* **Termination:** `left` (3) is now equal to `right` (3). Loop ends.
* **Return:** `nums[3]` which is `1`.

---

# Complexity Analysis 

Time Complexity 

O(\log N) 

At each step of the `while` loop, we cut the search space in half. This is the classic signature of binary search, resulting in a logarithmic time complexity.

Space Complexity 

O(1) 

We only use a few integer variables (`left`, `right`, `mid`) to keep track of the indices, which takes constant extra memory. 

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
            else:
                right = mid
        
        return nums[left]
```