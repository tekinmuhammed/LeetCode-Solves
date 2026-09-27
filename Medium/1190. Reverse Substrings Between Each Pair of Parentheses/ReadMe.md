# 1190. Reverse Substrings Between Each Pair of Parentheses

**Difficulty:** Medium 
**Problem Link:** [LeetCode 1190](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/)

---

## Problem 
You are given a string `s` that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one. Your result should not contain any brackets.
 
Example: 
 
Input   
s = "(u(love)i)"   
 
Output   
"iloveu" 
 
Explanation  
1. Reverse the innermost substring "love" $\rightarrow$ "(uevoli)".
2. Reverse the whole string "uevoli" $\rightarrow$ "iloveu".

---

# Approach 
 
To solve this problem efficiently, we can use a **Stack** and a dynamic **Result Array**. The trick is to avoid building strings with brackets and then removing them later. Instead, we only build the final characters and remember *where* the brackets would have been.
 
Steps: 
1. **Result Array (`result`)**: We maintain a list of characters that are currently outside of any unclosed, processed brackets.
2. **Stack (`open_parentheses_indices`)**: When we encounter an opening parenthesis `(`, we push the *current length* of the `result` array onto the stack. This length represents the starting index of the characters that will eventually need to be reversed once we find the matching `)`.
3. **Appending Characters**: For any normal lowercase letter, we simply append it to the `result` array.
4. **Reversing**: When we encounter a closing parenthesis `)`, we pop the last saved index from the stack. This index tells us exactly where the current innermost group of characters started in our `result` array. We then reverse the slice of the `result` array from that index to the end (`result[start:] = result[start:][::-1]`).
5. **Final Output**: Once the loop finishes, the `result` array contains the fully processed string without any parentheses. We join it and return.
 
--- 
 
# Code 

```python
from collections import deque

class Solution:
    def reverseParentheses(self, s: str) -> str:
        open_parentheses_indices = deque()
        result = []

        for current_char in s:
            if current_char == "(":
                # Store the current length as the start index
                # for future reversal
                open_parentheses_indices.append(len(result))
            elif current_char == ")":
                start = open_parentheses_indices.pop()
                # Reverse the substring between the matching parentheses
                result[start:] = result[start:][::-1]
            else:
                # Append non-parenthesis characters to the processed list
                result.append(current_char)
        return "".join(result)
```

---
 
# Example Walkthrough 
 
Let's trace `s = "(u(love)i)"`
 
1. **`(`**: `result = []`, stack appends `0`. `stack = [0]`
2. **`u`**: `result = ['u']`
3. **`(`**: `result = ['u']`, stack appends length 1. `stack = [0, 1]`
4. **`l, o, v, e`**: Appended to result. `result = ['u', 'l', 'o', 'v', 'e']`
5. **`)`**:
   * Pop from stack $\rightarrow$ `start = 1`.
   * Reverse `result[1:]` (which is `['l', 'o', 'v', 'e']`).
   * `result = ['u', 'e', 'v', 'o', 'l']`
6. **`i`**: Appended to result. `result = ['u', 'e', 'v', 'o', 'l', 'i']`
7. **`)`**:
   * Pop from stack $\rightarrow$ `start = 0`.
   * Reverse `result[0:]` (the whole array).
   * `result = ['i', 'l', 'o', 'v', 'e', 'u']`

Result: `"".join(result)` $\rightarrow$ `"iloveu"`.
 
--- 
 
# Complexity Analysis 
 
Time Complexity 
 
$\mathcal{O}(N^2)$ in the worst case. 
Where $N$ is the length of the string. In the worst-case scenario with deeply nested parentheses like `((((a))))`, we perform a reversal operation for every closing parenthesis. Reversing a slice takes time proportional to the length of the slice, leading to $1 + 2 + 3 + ... + N/2$ operations, which is $\mathcal{O}(N^2)$. For average cases, it performs very fast.

Space Complexity

$\mathcal{O}(N)$

We use a `result` array to store the characters (up to length $N$) and a `deque` to store indices of open parentheses (up to $N/2$ items). The overall space complexity is proportional to the input size.