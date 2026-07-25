# 3536. Maximum Product of Two Digits 

**Difficulty:** Easy
**Problem Link:** [LeetCode 3536](https://leetcode.com/problems/maximum-product-of-two-digits/description/)
---

## Problem
Given a positive integer `n`, return the maximum possible product of any two of its digits.

Example:

Input  
n = 4926  

Output  
54

Explanation  
The digits of the number are 4, 9, 2, and 6. The largest two digits are 9 and 6. Their product is 9 * 6 = 54.

---

# Approach 
 
To maximize the product of two digits, we simply need to find the **two largest digits** in the number.  
 
Instead of converting the integer to a string, sorting the digits, and picking the top two (which takes extra space and time), we can process the number mathematically:
1. Initialize two variables, `first` and `second`, to 0 to keep track of the highest and second-highest digits.
2. Use a `while` loop to extract the last digit of the number using the modulo operator (`x = n % 10`).
3. Compare the extracted digit `x` with our tracked maximums:
   * If `x` is greater than `first`, update `second` to be the old `first`, and set `first` to `x`. 
   * Else if `x` is not greater than `first` but is greater than `second`, update `second` to `x`. 
4. Remove the last digit from `n` using integer division (`n //= 10`) and repeat until `n` becomes 0. 
5. Return the product of `first` and `second`. 
 
--- 
 
# Code 

```python
class Solution:
    def maxProduct(self, n: int) -> int:
        first, second = 0, 0
        while n > 0:
            x = n % 10
            if x > first:
                first, second = x, first
            elif x > second:
                second = x
            n //= 10
        return first * second
```

---
 
# Example Walkthrough

Let's trace the algorithm for `n = 4926`.

Initial state: `first = 0`, `second = 0`

1. **n = 4926**:
   * `x = 4926 % 10 = 6`
   * `6 > first (0)` $\rightarrow$ `second = 0`, `first = 6`
   * `n //= 10` $\rightarrow$ `n = 492`

2. **n = 492**:
   * `x = 492 % 10 = 2`
   * `2 > first (6)` is False.
   * `2 > second (0)` is True $\rightarrow$ `second = 2`
   * `n //= 10` $\rightarrow$ `n = 49`
 
3. **n = 49**:
   * `x = 49 % 10 = 9`
   * `9 > first (6)` is True $\rightarrow$ `second = 6`, `first = 9`
   * `n //= 10` $\rightarrow$ `n = 4`
 
4. **n = 4**:
   * `x = 4 % 10 = 4`
   * `4 > first (9)` is False.
   * `4 > second (6)` is False.
   * `n //= 10` $\rightarrow$ `n = 0`

Loop terminates.
Return `first * second` $\rightarrow$ `9 * 6 = 54`.

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(D)$

Where $D$ is the number of digits in `n`. Mathematically, this is $\mathcal{O}(\log_{10} n)$. Since an integer typically has a limited number of digits (e.g., up to 10 for a 32-bit integer), this effectively runs in $\mathcal{O}(1)$ constant time.

Space Complexity

$\mathcal{O}(1)$

The algorithm only uses a few integer variables (`first`, `second`, `x`) regardless of the size of `n`. No strings or arrays are created.