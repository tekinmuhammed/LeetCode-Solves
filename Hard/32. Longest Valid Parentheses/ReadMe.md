# 32. Longest Valid Parentheses

**Difficulty:** Hard  
**Problem Link:** [LeetCode 32](https://leetcode.com/problems/longest-valid-parentheses/description/)

---

## Problem
Given a string containing just the characters `'('` and `')'`, return the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input  
s = "(()"  

Output  
2  
(Explanation: The longest valid parentheses substring is "()".)

Example 2:

Input  
s = ")()())"  

Output  
4  
(Explanation: The longest valid parentheses substring is "()()".)

---

# Approach

While this problem can be solved using a Stack or Dynamic Programming, the most optimal solution in terms of space utilizes a **Two-Pass Counter (Greedy)** approach. 

We maintain two counters: `left` (for open parentheses) and `right` (for close parentheses). 

1. **Left-to-Right Pass**: 
   * Iterate through the string. Increment `left` for `'('` and `right` for `')'`.
   * Whenever `left == right`, we have found a perfectly balanced valid substring. We update our maximum length to `2 * right`.
   * If `right > left`, the sequence is broken (too many closing brackets), so we reset both counters to 0.

2. **Right-to-Left Pass**:
   * The left-to-right pass has a blind spot: strings with excess open parentheses like `"(()"`. In this case, `left` never equals `right`, and the counter is never reset.
   * To fix this, we do a second pass from right to left.
   * Now, if `left > right`, the sequence is broken, and we reset the counters. When `left == right`, we update the max length to `2 * left`.

This clever two-pass logic guarantees we find the maximum valid substring without needing extra memory.

---

# Code

*(Note: Minor syntax fixes applied to `2right` and `2left` for valid Python multiplication)*

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, maxi = 0, 0, 0
        
        # Left to Right Pass
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
                
            if left == right:
                maxi = max(maxi, 2 * right)
            elif right > left:
                left = right = 0
                
        left = right = 0

        # Right to Left Pass
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
                
            if left == right:
                maxi = max(maxi, 2 * left)
            elif left > right:
                left = right = 0
                
        return maxi
```

---

# Example Walkthrough

Let's trace `s = "(()"`

**Pass 1: Left to Right**
* `i = 0, s[0] = '('`: `left = 1, right = 0`.
* `i = 1, s[1] = '('`: `left = 2, right = 0`.
* `i = 2, s[2] = ')'`: `left = 2, right = 1`. 
* End of pass. `maxi` is still `0` because `left` never equaled `right`, and `right` never exceeded `left`.

**Pass 2: Right to Left (Counters reset to 0)**
* `i = 2, s[2] = ')'`: `left = 0, right = 1`.
* `i = 1, s[1] = '('`: `left = 1, right = 1`. 
  * **Match!** `left == right`. `maxi = max(0, 2 * 1) = 2`.
* `i = 0, s[0] = '('`: `left = 2, right = 1`.
  * `left > right` $\rightarrow$ sequence breaks, counters reset: `left = 0, right = 0`.
* End of pass.

Result: `maxi = 2`.

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(N)$

Where $N$ is the length of the string. We iterate through the string exactly twice (once forward, once backward). Each iteration performs $\mathcal{O}(1)$ basic arithmetic and comparison operations. Therefore, the time complexity is strictly linear.

Space Complexity

$\mathcal{O}(1)$

We only use three integer variables (`left`, `right`, and `maxi`). No stacks, arrays, or DP tables are allocated, making the space complexity $\mathcal{O}(1)$ (constant extra space).