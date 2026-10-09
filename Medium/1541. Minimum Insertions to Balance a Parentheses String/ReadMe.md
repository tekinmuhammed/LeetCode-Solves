# 1541. Minimum Insertions to Balance a Parentheses String

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1541](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description/)

---

## Problem
Given a parentheses string `s` containing only the characters `'('` and `')'`. A parentheses string is balanced if:
* Any left parenthesis `'('` must have a corresponding **two consecutive right parentheses** `"))"`.
* Left parenthesis `'('` must go before the corresponding two right parentheses `"))"`.

In other words, we treat `'('` as an open bracket and `"))"` as a single close bracket. 
You can insert the characters `'('` and `')'` at any position of the string to balance it if needed.

Return the **minimum number of insertions** needed to make `s` balanced.

Example:

Input  
s = "))())("  

Output  
3  

Explanation  
Add '(' to match the first "))", add ')' to match the second ")", and add "))" to match the last "(".

---

# Approach

We can solve this problem in a single pass using a **Greedy Counter** approach. Instead of using a stack, we use variables to track unmatched left parentheses and the number of insertions we've been forced to make.

Because a single `'('` requires exactly two `')'` characters right next to each other, we iterate through the string using a `while` loop so we can manually control the index (e.g., skipping ahead when we find two consecutive `)`).

Steps:
1. **Initialize Trackers**: `insertions` for the total brackets we manually add, and `left_count` for unmatched `'('` brackets.
2. **Iterate Through `s`**:
   * If the current character is `'('`: 
     Increment `left_count` and move to the next character.
   * If the current character is `')'`:
     * First, we need an open parenthesis for it. If `left_count > 0`, we have one available, so we decrement `left_count`. If `left_count == 0`, we are forced to insert an opening parenthesis `(`, so we increment `insertions`.
     * Second, we need a second `)` to complete the `"))"` pair. We check the very next character. If it is also `')'`, great! We consume it by advancing the index by 2. If it's not `')'` (or we are at the end of the string), we must insert a closing parenthesis, so we increment `insertions` and advance the index by 1.
3. **Final Cleanup**: After the loop finishes, we might have leftover unmatched `'('` brackets (meaning `left_count > 0`). Each one requires two `)` brackets to close. So we add `left_count * 2` to our `insertions`.

---

# Code

```python
class Solution:
    def minInsertions(self, s: str) -> int:
        length = len(s)
        insertions = left_count = index = 0

        while index < length:
            if s[index] == "(":
                left_count += 1
                index += 1
            else:
                # We encountered a ')'
                if left_count > 0:
                    left_count -= 1
                else:
                    # Missing an opening '(', so insert one
                    insertions += 1
                
                # Check if the next character is also ')'
                if index < length - 1 and s[index + 1] == ")":
                    index += 2
                else:
                    # Missing the second ')', so insert one
                    insertions += 1
                    index += 1

        # Add 2 closing brackets for every unmatched opening bracket
        insertions += left_count * 2
        return insertions
```

---

# Example Walkthrough

Let's trace `s = "))()"`

* **Initial State**: `insertions = 0`, `left_count = 0`, `index = 0`

1. **`index = 0`, `s[0] = ')'`**:
   * `left_count` is 0. We need a `(`, so `insertions += 1` $\rightarrow 1$.
   * Check next char: `s[1] == ')'`. It matches! 
   * Consume both: `index += 2`. `index` is now 2.

2. **`index = 2`, `s[2] = '('`**:
   * Increment `left_count` $\rightarrow 1$.
   * `index += 1`. `index` is now 3.

3. **`index = 3`, `s[3] = ')'`**:
   * `left_count > 0`, so we use it. `left_count -= 1` $\rightarrow 0$.
   * Check next char: `index < length - 1` is False (we are at the end).
   * Missing the second `)`, so `insertions += 1` $\rightarrow 2$.
   * `index += 1`. `index` is now 4.

4. **End of Loop**: `index` (4) is not `< length` (4).
   * Cleanup: `insertions += left_count * 2` $\rightarrow 2 + 0 = 2$.
   
Result: `2` (We made it `"())(())"`).

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(N)$

Where $N$ is the length of the string `s`. We traverse the string exactly once from left to right. Sometimes we skip a character by advancing the index by 2, but we never go backward. Thus, it operates in strict linear time.

Space Complexity

$\mathcal{O}(1)$

We use a few integer variables (`length`, `insertions`, `left_count`, `index`) to track our counts and indices. No additional space that scales with the input size is used, yielding a constant space complexity.