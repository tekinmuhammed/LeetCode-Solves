# 1848. Minimum Distance to the Target Element

**Difficulty:** Easy
**Problem Link:** [LeetCode 1848](https://leetcode.com/problems/minimum-distance-to-the-target-element/description/)

---

## Problem Description

Given an integer array `nums` (0-indexed) and two integers `target` and `start`, find an index `i` such that `nums[i] == target` and `abs(i - start)` is **minimized**.

Return `abs(i - start)`.

It is **guaranteed** that `target` exists in `nums`.

---

## Approach: Linear Scan

To find the minimum distance, we need to check every index where the `target` appears and calculate its distance from the `start` position.

### Key Ideas:
1.  **Full Traversal:** We iterate through the array using `enumerate` to keep track of both the current value and its index `i`.
2.  **Distance Calculation:** When we find an element that equals the `target`, we calculate the absolute difference: `abs(i - start)`.
3.  **Updating Minimum:** We compare this distance with our current minimum (`res`) and update it if the new distance is smaller.
4.  **Initial Value:** We initialize `res` with the length of the array (or any value larger than any possible distance) to ensure the first found target updates the variable.

---

## Code

```python
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        # Initialize res with the maximum possible distance
        res = len(nums)
        
        for i, num in enumerate(nums):
            # Check if current number is our target
            if num == target:
                # Calculate absolute distance and update result if it's a new minimum
                distance = abs(i - start)
                if distance < res:
                    res = distance
                    
        return res