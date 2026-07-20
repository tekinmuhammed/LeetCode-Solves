# 1081. Smallest Subsequence of Distinct Characters

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1081](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/)

---

## Problem
Given a string `s`, return the **lexicographically smallest subsequence** of `s` that contains all the distinct characters of `s` exactly once.

Example:

Input  
s = "bcabc"  

Output  
"abc"

Explanation  
The distinct characters are 'a', 'b', and 'c'. The possible subsequences containing all distinct characters exactly once are "bca", "bac", "cab", and "abc". Among these, "abc" is the lexicographically smallest.

---

# Approach

To ensure the result is the lexicographically smallest possible string, we use a **Monotonic Stack** combined with greedy logic. 

We want to build the string by picking characters one by one. If we find a character that is alphabetically smaller than the last character we picked, we should remove the last character—**but only if we know it will appear again later in the string**.

Steps:

1. **Frequency Array (`num`)**: Count how many times each character appears in the string. This tells us if we can afford to discard a character later.
2. **Visited Array (`vis`)**: Track which characters are currently in our stack so we don't add duplicates.
3. **Iterate and Filter**: For each character in the string:
   * If it is already in the stack (`vis[idx] == 1`), just decrement its remaining count and skip.
   * If it is not in the stack, compare it with the top of the stack.
   * **Pop Condition**: While the stack is not empty, the top element is strictly greater than the current character (`stk[-1] > ch`), and the top element still has remaining occurrences in the string (`num[top_idx] > 0`), we pop it from the stack and mark it as unvisited.
   * Push the current character into the stack and mark it as visited.
   * Decrement the character's remaining frequency.
4. Finally, join the characters in the stack to form the result string.

---

# Code

```python
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        vis = [0] * 26
        num = [0] * 26

        for ch in s:
            num[ord(ch) - ord("a")] += 1
        stk = []

        for ch in s:
            idx = ord(ch) - ord("a")
            if not vis[idx]:
                while stk and stk[-1] > ch:
                    top_idx = ord(stk[-1]) - ord("a")
                    if num[top_idx] > 0:
                        vis[top_idx] = 0
                        stk.pop()
                    else:
                        break
                vis[idx] = 1
                stk.append(ch)
            num[idx] -= 1

        return "".join(stk)
```

---

# Example Walkthrough

Example:

s = "bcabc"

1. **Initial Counts**: `{'a': 1, 'b': 2, 'c': 2}`

2. **Step-by-step Execution**:
   * **'b'**: Stack is empty. Push 'b'.  
     `stk = ['b']`, counts: `{'a': 1, 'b': 1, 'c': 2}`
   * **'c'**: 'c' > 'b'. Push 'c'.  
     `stk = ['b', 'c']`, counts: `{'a': 1, 'b': 1, 'c': 1}`
   * **'a'**: 'a' < 'c'. 'c' has remaining count > 0, so pop 'c'.  
     'a' < 'b'. 'b' has remaining count > 0, so pop 'b'.  
     Push 'a'.  
     `stk = ['a']`, counts: `{'a': 0, 'b': 1, 'c': 1}`
   * **'b'**: 'b' > 'a'. Push 'b'.  
     `stk = ['a', 'b']`, counts: `{'a': 0, 'b': 0, 'c': 1}`
   * **'c'**: 'c' > 'b'. Push 'c'.  
     `stk = ['a', 'b', 'c']`, counts: `{'a': 0, 'b': 0, 'c': 0}`

Result: **"abc"**

---

# Complexity Analysis

Time Complexity

O(n)

We iterate through the string twice (once to count, once to process). Each character is pushed and popped from the stack at most once, making it a linear time operation.

Space Complexity

O(1)

The space used by the `vis` and `num` arrays is strictly bounded to 26 elements. The stack can hold at most 26 unique characters. Since this size does not scale with the input string length, the space complexity is constant $O(1)$.