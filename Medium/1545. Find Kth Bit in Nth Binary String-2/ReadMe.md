# 1545. Find Kth Bit in Nth Binary String

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1545](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/)

---

## Problem Description

Given two positive integers `n` and `k`, the binary string $S_n$ is formed as follows:
- $S_1 = "0"$
- $S_i = S_{i-1} + "1" + reverse(invert(S_{i-1}))$ for $i > 1$

Where `+` denotes concatenation, `reverse(x)` reverses the string `x`, and `invert(x)` replaces all '0's with '1's and vice versa.

Return the $k^{th}$ bit in $S_n$. It is guaranteed that $k$ is valid for the given $n$.

---

## Approach

The string length grows exponentially ($2^n - 1$). Generating the entire string would be inefficient in terms of memory and time. Instead, we use a **Recursive (Divide and Conquer)** approach by observing the structure of $S_n$.

### Key Ideas:
1.  **Symmetry:** $S_n$ is composed of three parts:
    - Left part: $S_{n-1}$
    - Middle part: `"1"` at position $2^{n-1}$
    - Right part: `reverse(invert(S_{n-1}))`
2.  **Recursive Cases:**
    - If $k$ is exactly the middle position ($mid = 2^{n-1}$), the bit is always **'1'**.
    - If $k < mid$, the bit is the same as the $k^{th}$ bit in $S_{n-1}$.
    - If $k > mid$, the bit is at a symmetric position in $S_{n-1}$, but **inverted**.
3.  **Mirror Mapping:** To find the corresponding index in the left half for a position $k$ in the right half:
    - `mirrored_index = mid - (k - mid)`

---

## Code

```python
class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def helper(n, k):
            # Base Case: S_1 is always "0"
            if n == 1:
                return '0'
            
            # Length of S_n is 2^n - 1, so middle index is 2^(n-1)
            mid = 1 << (n - 1)
            
            if k == mid:
                return '1'
            elif k < mid:
                # Look into the left part (S_{n-1})
                return helper(n - 1, k)
            else:
                # Look into the right part (reverse + invert of S_{n-1})
                # Find the symmetric position in the first half
                mirrored = mid - (k - mid)
                bit = helper(n - 1, mirrored)
                # Invert the bit found
                return '1' if bit == '0' else '0'
        
        return helper(n, k)
```

---

## Example Walkthrough

**Input:** `n = 3, k = 1`

1. `n = 3, k = 1`: $mid = 4$. Since $1 < 4$, call `helper(2, 1)`.
2. `n = 2, k = 1`: $mid = 2$. Since $1 < 2$, call `helper(1, 1)`.
3. `n = 1, k = 1`: Base case reached, return **'0'**.

**Input:** `n = 4, k = 11`

1. `n = 4, k = 11`: $mid = 8$. Since $11 > 8$, find `mirrored = 8 - (11 - 8) = 5`. Call `helper(3, 5)` and invert the result.
2. `n = 3, k = 5`: $mid = 4$. Since $5 > 4$, find `mirrored = 4 - (5 - 4) = 3`. Call `helper(2, 3)` and invert the result.
3. ... (continues until base case)

---

## Complexity Analysis

* **Time Complexity:** `O(n)`
    * In each step, we reduce **n** by 1. Since we only make one recursive call at a time, the depth of the recursion tree is $n$.
* **Space Complexity:** `O(n)`
    * Due to the recursion stack depth. No large strings are stored in memory.

---

## Tags
Recursion, Binary-String, Divide-and-Conquer, Bit-Manipulation