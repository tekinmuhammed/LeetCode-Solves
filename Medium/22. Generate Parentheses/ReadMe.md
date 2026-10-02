# 22. Generate Parentheses

**Difficulty:** Medium  
**Problem Link:** [LeetCode 22](https://leetcode.com/problems/generate-parentheses/description/)

---

## Problem
Given `n` pairs of parentheses, write a function to *generate all combinations of well-formed parentheses*.

Example:

Input  
n = 3  

Output  
["((()))","(()())","(())()","()(())","()()()"]

---

# Approach

To generate all valid combinations, we use a **Backtracking** (Depth-First Search) algorithm. The key to ensuring the parentheses are "well-formed" lies in carefully controlling when we add an open parenthesis `(` and when we add a close parenthesis `)`.

Rules for building a valid sequence:
1. **Adding `(`**: We can add an open parenthesis as long as we haven't used all `n` of them (`open > 0`).
2. **Adding `)`**: We can only add a close parenthesis if there are currently more unclosed `(` than remaining `(` to be placed. In our counter logic, this means `close > open`.
3. **Base Case**: When both `open` and `close` counts drop to `0`, we have formed a complete and valid string of length `2 * n`. 

*Optimization in your code*: Instead of passing and concatenating immutable strings at each recursive step (which creates many intermediate string objects in memory), you pre-allocated a character array `ch` of size `2 * n` and overwrite indices. This is a very memory-efficient way to handle the state in Python.

---

# Code

```python
class Solution:
    def func(self, result, ch, index, open, close):
        # Base case: no more brackets to place
        if open == 0 and close == 0:
            result.append("".join(ch))
            return

        # Try placing an open parenthesis if available
        if open > 0:
            ch[index] = '('
            self.func(result, ch, index + 1, open - 1, close)

        # Try placing a close parenthesis if it's valid to do so
        if close > open:
            ch[index] = ')'
            self.func(result, ch, index + 1, open, close - 1)

    def generateParenthesis(self, n):
        result = []
        ch = [' '] * (2 * n)

        # Start the recursive backtracking
        self.func(result, ch, 0, n, n)

        return result
```

---

# Example Walkthrough

Let's trace `n = 2`

* **Initial call**: `open = 2`, `close = 2`, `index = 0`, `ch = [' ', ' ', ' ', ' ']`
* **Step 1 (`open > 0`)**: Add `(`, call `open = 1`, `close = 2`, `index = 1`. `ch = ['(', ' ', ' ', ' ']`
* **Step 2 (`open > 0`)**: Add `(`, call `open = 0`, `close = 2`, `index = 2`. `ch = ['(', '(', ' ', ' ']`
* **Step 3 (`open` is 0, `close > open`)**: Add `)`, call `open = 0`, `close = 1`, `index = 3`. `ch = ['(', '(', ')', ' ']`
* **Step 4 (`close > open`)**: Add `)`, call `open = 0`, `close = 0`, `index = 4`. `ch = ['(', '(', ')', ')']`
* **Base Case**: `open == 0` and `close == 0`. Append `"(())"` to result. Backtrack.
* **Backtrack to Step 1 (`close > open`)**: Add `)`, call `open = 1`, `close = 1`, `index = 2`. `ch = ['(', ')', ' ', ' ']`
* **Step 5 (`open > 0`)**: Add `(`, call `open = 0`, `close = 1`, `index = 3`. `ch = ['(', ')', '(', ' ']`
* **Step 6 (`close > open`)**: Add `)`, call `open = 0`, `close = 0`, `index = 4`. `ch = ['(', ')', '(', ')']`
* **Base Case**: Append `"()()"` to result. Backtrack.

Result: `["(())", "()()"]`

---

# Complexity Analysis

Time Complexity

$\mathcal{O}\left(\frac{4^n}{\sqrt{n}}\right)$

The time complexity is tied to the $n$-th **Catalan Number**, which bounds the total number of valid parenthesis combinations. Generating each valid combination takes constant time relative to building the array elements, leading to this asymptotic bound. 

Space Complexity

$\mathcal{O}(N)$

The depth of the recursive call stack is exactly $2n$ before hitting the base case. The character array `ch` also takes $\mathcal{O}(N)$ space. Therefore, ignoring the space required to hold the output, the auxiliary space complexity is $\mathcal{O}(N)$.