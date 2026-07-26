# 628. Maximum Product of Three Numbers

**Difficulty:** Easy  
**Problem Link:** [LeetCode 628](https://leetcode.com/problems/maximum-product-of-three-numbers/description/)

---
 
## Problem 
Given an integer array `nums`, find three numbers whose product is maximum and return the maximum product.
 
Example 1: 
 
Input  
nums = [1, 2, 3]  

Output  
6  

Example 2:

Input  
nums = [-10, -10, 5, 2]  

Output  
500  
(Explanation: -10 * -10 * 5 = 500)

---

# Approach

To find the maximum product of three numbers in an array, we don't need to check every combination. The maximum product can only come from two scenarios:
1. **Three largest positive numbers:** If the array has all positive numbers (or a mix), the three largest numbers will yield a large positive product.
2. **Two smallest negative numbers and the largest positive number:** Multiplying two negative numbers results in a positive number. If the array has very small (highly negative) numbers, multiplying the two smallest numbers together and then multiplying by the largest positive number might yield the absolute highest product.

Instead of sorting the entire array—which would take $\mathcal{O}(N \log N)$ time—we can use Python's `heapq` module (`nlargest` and `nsmallest`) to find just the 3 largest and 2 smallest numbers in a single pass. 

*   `a, b, c` = The 3 largest numbers (where `a` is the absolute largest).
*   `x, y` = The 2 smallest numbers.

We simply calculate the products of both scenarios (`a * b * c` and `a * x * y`) and return the maximum.

---

# Code

```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Note: LeetCode automatically imports nlargest and nsmallest from heapq
        (a, b, c), (x, y) = nlargest(3, nums), nsmallest(2, nums)
        return max(a * b * c, a * x * y)
```

---

# Example Walkthrough

Let's use `nums = [-10, -10, 1, 3, 2]`

1. **Find Largest and Smallest:**
   * `nlargest(3, nums)` returns `[3, 2, 1]`. So, `a = 3, b = 2, c = 1`.
   * `nsmallest(2, nums)` returns `[-10, -10]`. So, `x = -10, y = -10`.
2. **Calculate Scenarios:**
   * Scenario 1 (Three largest): `a * b * c` = `3 * 2 * 1` = `6`
   * Scenario 2 (Two smallest negatives + largest): `a * x * y` = `3 * -10 * -10` = `300`
3. **Return Max:**
   * `max(6, 300)` = `300`.

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(N)$

Finding the `k` largest or smallest elements using a heap takes $\mathcal{O}(N \log k)$ time. Since $k$ is at most 3 (a constant), the time complexity simplifies to $\mathcal{O}(N)$. This is faster than sorting the whole array.

Space Complexity

$\mathcal{O}(1)$

We only store 5 variables (3 for the largest, 2 for the smallest) regardless of the size of the input array `nums`. Therefore, the space complexity is constant.