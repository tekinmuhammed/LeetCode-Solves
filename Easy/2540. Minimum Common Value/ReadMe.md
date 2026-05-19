# 2540. Minimum Common Value

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2540](https://leetcode.com/problems/minimum-common-value/description/)

---

## Problem
Given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, return the **minimum integer common** to both arrays. If there is no common integer amongst `nums1` and `nums2`, return `-1`.

Note that an integer is said to be common to `nums1` and `nums2` if both arrays have at least one occurrence of that integer.

Example:

Input  
nums1 = [1,2,3], nums2 = [2,4]

Output  
2

Explanation  
The smallest element common to both arrays is 2, so we return 2.

---

# Approach

While this problem can be solved using a Two-Pointer approach since the arrays are sorted, a **Hash Set** provides a very clean and Pythonic alternative with excellent average-case performance.

Steps:

1. **Hash Set for Fast Lookup:** We convert the first array, `nums1`, into a hash set (`set1`). This operation takes linear time, but it drastically reduces the lookup time for any element from $O(N)$ to $O(1)$ on average.
2. **Sequential Search:** We iterate through the second array, `nums2`. 
3. **Exploiting the Sorted Order:** Because `nums2` is already sorted in non-decreasing (ascending) order, the very first element in `nums2` that we find inside `set1` is mathematically guaranteed to be the *minimum* common value. We don't need to check any further.
4. **Early Exit:** As soon as we find a match, we immediately return that number.
5. **Fallback:** If the loop finishes completely and no elements were found in the set, we return `-1`.

---

# Example Walkthrough

Consider `nums1 = [1, 2, 3]` and `nums2 = [2, 4]`

1. **Build the set:** 
   `set1 = {1, 2, 3}`
2. **Iterate through `nums2`:**
   * **First element (2):** Is `2` in `set1`? Yes! 
   * Since `nums2` is sorted, `2` is the smallest possible candidate.
   * Return `2` immediately.

---

# Complexity Analysis

Time Complexity

O(N + M)

Where `N` is the length of `nums1` and `M` is the length of `nums2`. Converting `nums1` into a set takes $O(N)$ time. Iterating through `nums2` takes up to $O(M)$ time in the worst case. Set lookups take $O(1)$ time on average. Thus, the total time complexity is linear.

Space Complexity

O(N)

We create a hash set from `nums1`, which requires $O(N)$ extra memory to store the unique elements of the first array.

---

# Code

```python
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Add the elements from nums1 to set1
        set1 = set(nums1)

        # Search for each element of nums2 in set1
        # Return the first common element found
        for num in nums2:
            if num in set1:
                return num

        # Return -1 if there are no common elements
        return -1
```