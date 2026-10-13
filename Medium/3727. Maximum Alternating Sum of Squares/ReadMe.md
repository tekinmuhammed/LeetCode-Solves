# 3727. Maximum Alternating Sum of Squares

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3727](https://leetcode.com/problems/maximum-alternating-sum-of-squares/)

---

## Problem
You are given an integer array `nums`. You may rearrange the elements in any order.

The alternating score of an array `arr` is defined as:
* $\text{score} = arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + \dots$

Return an integer denoting the maximum possible alternating score of `nums` after rearranging its elements.

Example:

Input  
nums = [1, 2, 3] 

Output  
12 

Explanation  
A possible rearrangement is `[2, 1, 3]`.  
$\text{score} = 2^2 - 1^2 + 3^2 = 4 - 1 + 9 = 12$.

---

# Approach

To maximize the alternating sum of squares, we can analyze the mathematical structure of the score formula:
$$\text{score} = arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + \dots$$

Notice that:
1. Elements at **even indices** ($0, 2, 4, \dots$) contribute **positively** to the score.
2. Elements at **odd indices** ($1, 3, 5, \dots$) contribute **negatively** to the score.

Since squaring any number makes it non-negative, the original sign of each element doesn't matter; only its squared magnitude matters. To maximize the total score, we want the **largest** squares to occupy the positive positions (even indices) and the **smallest** squares to occupy the negative positions (odd indices).

Steps:
1. **Square Each Element**: Replace every element in `nums` with its square ($nums[i] = nums[i] \times nums[i]$). This standardizes everything into non-negative magnitude values.
2. **Sort the Squares**: Sort the array in ascending order. After sorting, the smallest squared values will be at the beginning of the array, and the largest will be at the end.
3. **Partition and Sum**: 
   * The first $\lfloor n / 2 \rfloor$ elements are the smallest squares, which should be subtracted (negative positions).
   * The remaining elements are the largest squares, which should be added (positive positions).
4. **Compute Final Score**: Return the sum of the second half minus the sum of the first half.

---

# Code

```python
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] *= nums[i]
        nums.sort()
        return -sum(nums[: n // 2]) + sum(nums[n // 2 :])
```