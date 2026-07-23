# 3513. Number of Unique XOR Triplets I

**Difficulty:** Medium 
**Problem Link:** [LeetCode 3513](https://leetcode.com/problems/number-of-unique-xor-triplets-i/description/)
 
--- 
 
## Problem
Given an integer array `nums`, you need to find the number of unique XOR triplets that satisfy the problem's specific conditions. 

*(Note: Based on the provided optimal solution, the problem simplifies mathematically. The actual values inside the `nums` array do not matter; the answer depends entirely on the **length** of the array.)*
 
--- 
 
# Approach 
 
A brute-force approach to find triplets would normally require an $\mathcal{O}(N^3)$ simulation, checking every possible combination of three elements. However, this optimal solution uses a mathematical observation/pattern reduction.

Instead of calculating XOR values, the logic only looks at $N$, the length of the array:
1. **Base Case:** If the array has 2 or fewer elements (`n <= 2`), the answer is simply $n$.
2. **Pattern Recognition for $N > 2$:** The result always evaluates to the **smallest power of 2 that is strictly greater than $n$**.
3. **Bitwise Shift:** To find this next power of 2 efficiently, we initialize `ans = 1`. In a loop, we perform a left bit-shift (`ans <<= 1`, which multiplies `ans` by 2) until `ans` exceeds `n`.  
 
This transforms what sounds like an array-processing problem into a pure mathematical $O(\log n)$ step. 
 
--- 
 
# Code

```python
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        ans = 1
        while ans <= n:
            ans <<= 1
        return ans
```

---

# Example Walkthrough

Let's say `nums` has a length of `5` (e.g., `nums = [1, 2, 3, 4, 5]`).

1. `n = 5`.
2. `n <= 2` is False, so we bypass the base case.
3. Initialize `ans = 1`.
4. Loop iterations:
   * `ans = 1` (1 <= 5) $\rightarrow$ `ans = 2`
   * `ans = 2` (2 <= 5) $\rightarrow$ `ans = 4`
   * `ans = 4` (4 <= 5) $\rightarrow$ `ans = 8`
   * `ans = 8` (8 <= 5 is False) $\rightarrow$ Loop breaks.
5. Return `8`. 

The result for any array of length 5, 6, or 7 will always be `8`.

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(\log n)$

The `while` loop runs exactly $\lfloor \log_2(n) \rfloor + 1$ times, because it multiplies `ans` by 2 at each step. This makes it incredibly fast, effectively running in near-constant time for standard integer sizes.

Space Complexity

$\mathcal{O}(1)$

We only use two integer variables (`n` and `ans`), which take constant extra space. The input array `nums` is not modified or duplicated.