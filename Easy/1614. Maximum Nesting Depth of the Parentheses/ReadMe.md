# 1614. Maximum Nesting Depth of the Parentheses

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1614](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/)

---

## Problem
A string is a **valid parentheses string** (denoted VPS) if it meets one of the following:
* It is an empty string `""`, or a single character not equal to `"("` or `")"`,
* It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are VPS's, or
* It can be written as `(A)`, where `A` is a VPS.

We can similarly define the **nesting depth** `depth(S)` of any VPS `S` as follows:
* `depth("") = 0`
* `depth(C) = 0`, where `C` is a string with a single character not equal to `"("` or `")"`.
* `depth(A + B) = max(depth(A), depth(B))`, where `A` and `B` are VPS's.
* `depth("(" + A + ")") = 1 + depth(A)`, where `A` is a VPS.

Given a VPS represented as string `s`, return the **nesting depth** of `s`.

Example:

Input  
s = "(1+(2*3)+((8)/4))+1"  

Output  
3  

Explanation  
Digit 8 is inside of 3 nested parentheses in the string.

---

# Approach

To find the maximum nesting depth, we need to track how many open parentheses `(` are currently unclosed as we read the string from left to right. 

This solution uses a **Stack** (`st`) to simulate the nesting process:
1. **Initialize State**: Maintain a `st` list (acting as a stack) to hold open parentheses and an `ans` variable to keep track of the maximum depth seen so far.
2. **Iterate**: Go through each character `c` in the string `s`.
3. **Push**: If the character is an open parenthesis `(`, append it to the stack. This increases our current depth.
4. **Pop**: If the character is a closing parenthesis `)`, pop the top element from the stack. This decreases our current depth.
5. **Update Maximum**: After processing any character, the current depth is simply the length of the stack (`len(st)`). We update `ans` with the maximum of `ans` and the current stack length.
6. **Return**: Once the loop completes, `ans` holds the maximum nesting depth.

*(Note: Because the problem guarantees `s` is a valid parentheses string, we don't need to worry about popping from an empty stack.)*

---

# Code

```python
class Solution:
    def maxDepth(self, s: str) -> int:
        ans, st = 0, []
        for c in s:
            if c == '(':
                st.append(c)
            elif c == ')':
                st.pop()
            ans = max(ans, len(st))
        return ans
```

---

# Example Walkthrough

Let's trace `s = "(1+(2))"`

1. **`c = '('`** $\rightarrow$ `st = ['(']`, `len = 1`. `ans = max(0, 1) = 1`.
2. **`c = '1'`** $\rightarrow$ Ignore. `ans = max(1, 1) = 1`.
3. **`c = '+'`** $\rightarrow$ Ignore. `ans = max(1, 1) = 1`.
4. **`c = '('`** $\rightarrow$ `st = ['(', '(']`, `len = 2`. `ans = max(1, 2) = 2`.
5. **`c = '2'`** $\rightarrow$ Ignore. `ans = max(2, 2) = 2`.
6. **`c = ')'`** $\rightarrow$ Pop stack. `st = ['(']`, `len = 1`. `ans = max(2, 1) = 2`.
7. **`c = ')'`** $\rightarrow$ Pop stack. `st = []`, `len = 0`. `ans = max(2, 0) = 2`.

Result is `2`.

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(N)$

Where $N$ is the length of the string `s`. We iterate through the string exactly once. Appending to and popping from a list in Python both operate in $\mathcal{O}(1)$ time. 

Space Complexity

$\mathcal{O}(N)$

In the worst-case scenario (e.g., `s = "(((((())))))"`), all open parentheses are stored in the stack before any are closed. Thus, the list `st` can grow up to a size proportional to $N$. 

*(Optimization Note: The space complexity can easily be reduced to $\mathcal{O}(1)$ by replacing the list `st` with a simple integer counter that increments on `(` and decrements on `)`.)*