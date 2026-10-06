# 921. Minimum Add to Make Parentheses Valid

**Difficulty:** Medium  
**Problem Link:** [LeetCode 921](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/)

---

## Problem
A parentheses string is valid if and only if:
* It is the empty string,
* It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or
* It can be written as `(A)`, where `A` is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.

For example, if `s = "()))"`, you can insert an opening parenthesis to be `"(()))"` or a closing parenthesis to be `"())))"`.

Return the **minimum number of moves** required to make `s` valid.

Example 1:

Input  
s = "())"  

Output  
1  

Example 2:

Input  
s = "((("  

Output  
3  

---

# Approach

Instead of using a Stack (which would require $\mathcal{O}(N)$ space), we can solve this using a **Greedy Counter** approach in $\mathcal{O}(1)$ space. We only need to track the unmatched parentheses.

Steps:
1. **Track Unmatched Open Brackets**: Maintain a counter `open_brackets` for the `'('` characters that haven't been matched yet.
2. **Track Required Additions**: Maintain a counter `min_adds_required` for the `')'` characters that appear without a preceding `'('`.
3. **Iterate Through the String**:
   * If the character is `'('`, we simply increment `open_brackets`.
   * If the character is `')'`, we check if we have any unmatched `'('` available (`open_brackets > 0`). 
     * If yes, they match! We decrement `open_brackets`.
     * If no, we have an invalid `)` that cannot be matched. We must add a `(` to fix it, so we increment `min_adds_required`.
4. **Final Calculation**: After the loop, `min_adds_required` holds the number of `(` we need to add to the left, and `open_brackets` holds the number of `)` we need to add to the right. The total additions required is their sum.

---

# Code

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        min_adds_required = 0

        for c in s:
            if c == "(":
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    min_adds_required += 1

        # Add the remaining open brackets as closing brackets would be required.
        return min_adds_required + open_brackets
```

---

# Example Walkthrough

Let's trace `s = "())("`

* **Initial State**: `open_brackets = 0`, `min_adds_required = 0`
* **c = '('**: 
  * Increment `open_brackets` $\rightarrow$ 1
* **c = ')'**: 
  * `open_brackets > 0`, so they match. Decrement `open_brackets` $\rightarrow$ 0
* **c = ')'**: 
  * `open_brackets` is 0 (no open brackets available). 
  * Increment `min_adds_required` $\rightarrow$ 1 (We must insert a `(` before this)
* **c = '('**: 
  * Increment `open_brackets` $\rightarrow$ 1

**End of Loop**: 
* `min_adds_required = 1` (Needed one `(`)
* `open_brackets = 1` (Needed one `)`)
* Total additions = 1 + 1 = `2`.

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(N)$

Where $N$ is the length of the string `s`. We iterate through the string exactly once. The operations inside the loop are simple conditional checks and arithmetic additions, which take $\mathcal{O}(1)$ time.

Space Complexity

$\mathcal{O}(1)$

We only use two integer variables (`open_brackets` and `min_adds_required`) regardless of the size of the input string. This makes the space complexity constant.