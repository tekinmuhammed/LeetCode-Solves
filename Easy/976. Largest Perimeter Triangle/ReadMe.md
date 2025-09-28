# 976. Largest Perimeter Triangle

**Difficulty:** Easy  
**Link:** [LeetCode 976](https://leetcode.com/problems/largest-perimeter-triangle/)

## Problem Description
You are given an integer array `nums`. Return the **largest perimeter** of a triangle formed with **three different lengths** from `nums`.  
If no non-degenerate triangle can be formed, return `0`.

---

### Example 1
**Input:**  
```python
nums = [2,1,2]
```

**Output:**  
```python
5
```

**Explanation:**  
The sides `(2, 2, 1)` can form a triangle, and the perimeter is `5`.

---

### Example 2
**Input:**  
```python
nums = [1,2,1]
```

**Output:**  
```python
0
```

**Explanation:**  
The sides `(1, 2, 1)` cannot form a triangle because `1 + 1` is **not greater** than `2`.

---

## Approach
A valid triangle must satisfy the **triangle inequality**:
\[
a + b > c
\]
for any three sides `a, b, c`, where `c` is the longest side.

### Steps:
1. Sort `nums` in **descending order**.
2. Iterate through the sorted list:
   - For each triplet `(nums[i], nums[i+1], nums[i+2])`, check if it forms a valid triangle.
   - If valid, return the perimeter immediately (since sorting ensures this is the largest possible perimeter).
3. If no valid triangle exists, return `0`.

---

## Complexity Analysis
- **Time Complexity:** `O(n log n)` due to sorting.  
- **Space Complexity:** `O(1)` since sorting is in-place.  

---

## Code Implementation
```python
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)  # Sort from largest to smallest
        for i in range(len(nums) - 2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
```

### Tags

`LeetCade-Easy`