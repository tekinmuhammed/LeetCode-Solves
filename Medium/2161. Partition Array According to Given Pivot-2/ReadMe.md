# 2161. Partition Array According to Given Pivot

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2161](https://leetcode.com/problems/partition-array-according-to-given-pivot/description/)

---

## Problem
You are given a **0-indexed** integer array `nums` and an integer `pivot`. Rearrange `nums` such that the following conditions are satisfied:
1. Every element less than `pivot` appears **before** every element greater than `pivot`.
2. Every element equal to `pivot` appears **in between** the elements less than and greater than `pivot`.
3. The **relative order** of the elements less than `pivot` and the elements greater than `pivot` is maintained.

Return `nums` after the rearrangement.

---

# Approach

The problem requires a **stable partition**, meaning the original relative order of the elements must be preserved. A straightforward and highly readable way to achieve this is by categorizing the elements into separate lists as we iterate through the original array.

Steps:

1. **Initialize Categories:** Create three separate arrays: `less`, `equal`, and `greater`.
2. **Sequential Categorization:** Iterate through the `nums` array from left to right. Because we process the array sequentially, the relative order is automatically preserved.
   * If the current number is strictly less than the `pivot`, append it to the `less` array.
   * If it is strictly greater than the `pivot`, append it to the `greater` array.
   * If it is exactly equal to the `pivot`, append it to the `equal` array.
3. **Merge Categories:** Once the categorization is complete, concatenate the three arrays in the required order: `less` + `equal` + `greater`. In Python, `extend()` does this efficiently in-place for the base list.
4. **Return Result:** Return the combined `less` array.

---

# Example Walkthrough

Consider `nums = [9, 12, 5, 10, 14, 3, 10]` and `pivot = 10`

**Step 1 & 2: Categorization (Left to Right)**
* `9` < 10  $\rightarrow$ `less = [9]`
* `12` > 10 $\rightarrow$ `greater = [12]`
* `5` < 10  $\rightarrow$ `less = [9, 5]`
* `10` == 10 $\rightarrow$ `equal = [10]`
* `14` > 10 $\rightarrow$ `greater = [12, 14]`
* `3` < 10  $\rightarrow$ `less = [9, 5, 3]`
* `10` == 10 $\rightarrow$ `equal = [10, 10]`

**Step 3: Merge**
* Combine `less` and `equal`: `[9, 5, 3] + [10, 10]` $\rightarrow$ `[9, 5, 3, 10, 10]`
* Combine with `greater`: `[9, 5, 3, 10, 10] + [12, 14]` $\rightarrow$ `[9, 5, 3, 10, 10, 12, 14]`

**Result:** `[9, 5, 3, 10, 10, 12, 14]`

---

# Complexity Analysis

Time Complexity

O(N)

Where `N` is the number of elements in the `nums` array. We iterate through the array exactly once to distribute the elements. The `extend()` operations take time proportional to the sizes of the `equal` and `greater` lists, which together sum up to at most `N`. Thus, the overall time complexity is strictly linear.

Space Complexity

O(N)

We create three new arrays (`less`, `equal`, `greater`) which collectively store exactly `N` elements. Therefore, the extra space required is proportional to the size of the input array.

---

# Code

```python
from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greater = []

        # Group elements while maintaining their relative order
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)

        # Concatenate the lists
        less.extend(equal)
        less.extend(greater)

        return less
```