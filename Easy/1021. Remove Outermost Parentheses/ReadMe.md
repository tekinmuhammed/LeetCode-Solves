# 1021. Remove Outermost Parentheses

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1021](https://leetcode.com/problems/remove-outermost-parentheses/description/)

---

## Problem
Given a perfectly balanced parentheses string, it can be separated into non-overlapping "primitive" blocks. A primitive block is a valid parentheses sequence that cannot be split into two smaller valid sequences side-by-side (for example, `"(())"` is primitive, but `"()()"` is not, because it splits into `"()"` and `"()"`). 

Your objective is to strip away the outermost opening and closing brackets from every primitive block in the given string and return the concatenated result.

Example:

Input  
s = "(()())(())"  

Output  
"()()()"  

Explanation  
The string is composed of two primitive blocks: `(()())` and `(())`.  
Removing the outermost parentheses from each gives `()()` and `()`.  
Concatenating them results in `()()()`.

---

# Approach

To determine the outermost parentheses, we need to track the nesting depth. An outermost opening parenthesis occurs when the depth goes from 0 to 1. An outermost closing parenthesis occurs when the depth returns to 0. 

Your code uses a very clever and concise ordering of operations with a `stack` (acting as a depth tracker) to filter these out automatically:
1. **Closing Bracket (`)`**: If the character is `)`, we immediately pop from the stack. This reduces the depth *before* we decide whether to keep the character. If this was an outermost `)`, the stack is now empty.
2. **Result Appending**: We check if the stack is non-empty. If it is, it means the current character is *inside* a primitive block, so we append it to our result array. (This seamlessly ignores the outermost `)` because the stack was just emptied, and it ignores the outermost `(` because the stack hasn't been populated with it yet).
3. **Opening Bracket (`(`)**: If the character is `(`, we append it to the stack to increase the depth *after* the appending check. 

---

# Code

```python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, stack = [], []
        for c in s:
            if c == ")":
                stack.pop()
            if stack:
                res.append(c)
            if c == "(":
                stack.append(c)
        return "".join(res)
```

---

# Example Walkthrough

Let's trace `s = "(()())"`

1. **`c = '('`**:
   * `c == ')'`? No.
   * `stack` is empty? Yes, skip appending. (This is the outermost `(`)
   * `c == '('`? Yes, `stack.append('(')`. Stack is now `['(']`.

2. **`c = '('`**:
   * `c == ')'`? No.
   * `stack` is empty? No. `res.append('(')`. `res` = `['(']`.
   * `c == '('`? Yes, `stack.append('(')`. Stack is now `['(', '(']`.

3. **`c = ')'`**:
   * `c == ')'`? Yes, `stack.pop()`. Stack is now `['(']`.
   * `stack` is empty? No. `res.append(')')`. `res` = `['(', ')']`.
   * `c == '('`? No.

4. **`c = '('`**:
   * `c == ')'`? No.
   * `stack` is empty? No. `res.append('(')`. `res` = `['(', ')', '(']`.
   * `c == '('`? Yes. Stack is now `['(', '(']`.

5. **`c = ')'`**:
   * `c == ')'`? Yes, `stack.pop()`. Stack is now `['(']`.
   * `stack` is empty? No. `res.append(')')`. `res` = `['(', ')', '(', ')']`.
   * `c == '('`? No.

6. **`c = ')'`**:
   * `c == ')'`? Yes, `stack.pop()`. Stack is now `[]`.
   * `stack` is empty? Yes, skip appending. (This is the outermost `)`)
   * `c == '('`? No.

Result: `"".join(res)` $\rightarrow$ `"()()"`.

---

# Complexity Analysis

Time Complexity

O(N)

Where N is the length of the string `s`. We iterate through the string exactly once. The operations inside the loop (appending to a list, popping from a list) all run in O(1) time. Joining the result list into a string at the end also takes O(N) time.

Space Complexity

O(N)

We maintain a `res` list to build the final string, and a `stack` list to track the depth. In the worst-case scenario (e.g., `s = "(((((())))))"`), both lists will grow proportionally to the size of the input string. 
*(Note: The space complexity could be optimized to O(1) auxiliary space if an integer counter was used instead of the `stack` list, but using the list is a valid and readable approach).*