# 1752. Check if Array Is Sorted and Rotated

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1752](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/)

---

## Problem
Given an array `nums`, return `true` if the array was originally sorted in non-decreasing order, then rotated **some** number of positions (including zero). Otherwise, return `false`.

There may be **duplicates** in the original array.

Note: An array `A` rotated by `x` positions results in an array `B` of the same length such that `A[i] == B[(i+x) % A.length]`, where `%` is the modulo operation.

Example:

Input  
nums = [3,4,5,1,2]

Output  
true

Explanation  
[1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the element of value 1: [3,4,5,1,2].

---

# Approach

This solution uses a **Simulation (Brute-Force)** approach. The most straightforward way to find out if an array is a rotated version of a sorted array is to systematically "un-rotate" it from every possible index and check if the resulting array is sorted.

Steps:

1. **Iterate All Offsets:** We loop through every possible starting index `rotation_offset` from `0` to `n - 1`.
2. **Reconstruct the Array:** For each `rotation_offset`, we build a new array `check_sorted`. 
   * First, we append the elements from `rotation_offset` to the end of the array.
   * Then, we append the elements from the beginning of the array up to `rotation_offset - 1`.
   * This effectively simulates what the array looked like *before* it was rotated at this specific offset.
3. **Validate Sort Order:** We iterate through the newly constructed `check_sorted` array to verify if it is in strictly non-decreasing order. If we find any element strictly greater than the next one, it's not sorted.
4. **Return Early:** If we find even one `rotation_offset` that results in a perfectly sorted array, we immediately return `True`.
5. **Fallback:** If we check all possible offsets and none of them result in a sorted array, we return `False`.

*(Note: While there is an O(N) optimized approach that counts the number of "drops" in the array, this O(N²) simulation approach perfectly mirrors the mathematical definition of the problem and is highly readable.)*

---

# Example Walkthrough

Consider `nums = [3, 4, 5, 1, 2]`  
Length `n = 5`.

* **`rotation_offset = 0`**:
  * `check_sorted` = `[3, 4, 5, 1, 2]`
  * Is it sorted? No (`5 > 1`).
* **`rotation_offset = 1`**:
  * `check_sorted` = `[4, 5, 1, 2, 3]`
  * Is it sorted? No (`5 > 1`).
* **`rotation_offset = 2`**:
  * `check_sorted` = `[5, 1, 2, 3, 4]`
  * Is it sorted? No (`5 > 1`).
* **`rotation_offset = 3`**:
  * `check_sorted` = `[1, 2, 3, 4, 5]`
  * Is it sorted? **Yes!**
  * Return `True`.

---

# Complexity Analysis

Time Complexity

O(N^2)

Where `N` is the length of the array. We have an outer loop that runs `N` times to test each rotation offset. Inside this loop, we spend $O(N)$ time constructing the new array and another $O(N)$ time checking if it is sorted. Thus, the total time complexity is $O(N^2)$.

Space Complexity

O(N)

For each iteration, we create a new array `check_sorted` of size `N` to simulate the un-rotated array.

---

# Code

```python
from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        # Iterate through all possible rotation offsets
        for rotation_offset in range(n):
            check_sorted = []

            # Create the rotated array
            for index in range(rotation_offset, n):
                check_sorted.append(nums[index])
            for index in range(rotation_offset):
                check_sorted.append(nums[index])

            # Check if the constructed array is sorted
            is_sorted = True
            for index in range(n - 1):
                if check_sorted[index] > check_sorted[index + 1]:
                    is_sorted = False
                    break

            # If sorted, return true
            if is_sorted:
                return True

        # If no rotation makes the array sorted, return false
        return False
```