# 396. Rotate Function

**Difficulty:** Medium 
**Problem Link:** [LeetCode 396](https://leetcode.com/problems/rotate-function/description/)

---

## Problem Description

You are given an integer array `nums` of length `n`.

Assume $B_k$ to be an array obtained by rotating the array `nums` by $k$ positions clock-wise. We define the **rotation function** $F$ on `nums` as:

$F(k) = 0 \cdot B_k[0] + 1 \cdot B_k[1] + \dots + (n - 1) \cdot B_k[n - 1]$

Return the **maximum value** of $F(0), F(1), \dots, F(n - 1)$.

---

## Approach: Mathematical Derivation ($O(n)$)

Calculating each $F(k)$ independently would take $O(n^2)$ time, which is too slow. However, there is a mathematical relationship between $F(k)$ and $F(k-1)$ that allows us to compute each subsequent value in $O(1)$ time.

### Key Logic:
Let $S$ be the sum of all elements in `nums`.
Consider an example with $n=4$:
*   $F(0) = 0a + 1b + 2c + 3d$
*   $F(1) = 0d + 1a + 2b + 3c$

Subtracting $F(0)$ from $F(1)$:
$F(1) - F(0) = a + b + c - 3d$

We can rewrite this as:
$F(1) - F(0) = (a + b + c + d) - 4d$
$F(1) = F(0) + S - n \cdot d$ (where $d$ is the element that "rotated" to the 0th index).

**General Formula:**
$F(k) = F(k-1) + \text{sum}(nums) - n \cdot \text{nums}[n-k]$



---

## Code
```python
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initial setup: calculate F(0), n, and the total sum of nums
        f, n, numSum = 0, len(nums), sum(nums)
        
        # Calculate F(0) using the standard definition
        for i, num in enumerate(nums):
            f += i * num
            
        res = f
        
        # Iteratively calculate F(k) based on F(k-1)
        # We start from the end of the array to simulate clockwise rotation
        for i in range(n - 1, 0, -1):
            # Applying the formula: F(k) = F(k-1) + sum - n * last_element
            f = f + numSum - n * nums[i]
            res = max(res, f)
            
        return res
```

---

## Complexity Analysis

* **Time Complexity:** $O(n)$
    - We calculate the sum of the array in $O(n)$.
    - We calculate $F(0)$ in $O(n)$.
    - We iterate through the array once to calculate subsequent rotation values in $O(n)$.
* **Space Complexity:** $O(1)$
    - We only use a few integer variables (`f`, `n`, `numSum`, `res`) to store the state.

---

## Tags
`Array`, `Math`, `Dynamic-Programming`, `Sliding-Window`
