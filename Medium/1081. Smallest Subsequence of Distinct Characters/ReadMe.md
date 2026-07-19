# 1081. Smallest Subsequence of Distinct Characters

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1081](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/)

*(Note: This problem is exactly the same as [316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/))*

---

## Problem
Given a string `s`, return the lexicographically smallest subsequence of `s` that contains all the distinct characters of `s` exactly once.

Example:
Input: `s = "cbacdcbc"`
Output: `"acdb"`

---

# Approach

To achieve the lexicographically smallest subsequence, we should try to keep our sequence in alphabetical order as much as possible. A **Monotonic Stack** combined with a **Greedy Strategy** is perfect for this.

The core idea is: when we want to add a new character to our result, if the last added character is alphabetically larger than the new one AND we know the last character will appear again later in the string, we can safely discard the last character and replace it with the new one to improve the lexicographical order.

Steps:

1. **Count Frequencies:** First, iterate through the string and count how many times each character appears using a `num` array. This tells us if a character will appear again later.
2. **Track Visited Characters:** Use a `vis` array to keep track of characters currently inside our stack. We don't want to add duplicate characters.
3. **Iterate and Build (Monotonic Stack):** 
   * Loop through the string character by character.
   * If the current character `ch` is already in the stack (`vis[idx] == 1`), we simply decrement its remaining count (`num[idx] -= 1`) and skip it.
   * If it's not in the stack, we perform a `while` loop: as long as the stack is not empty, the top of the stack is alphabetically greater than `ch`, **AND** the top character's remaining count is strictly greater than `0` (meaning we can pick it up later), we `pop` it from the stack and mark it as unvisited (`vis = 0`).
   * Push the current `ch` into the stack and mark it as visited (`vis = 1`).
   * Decrement the remaining count of `ch`.
4. **Form the Result:** The elements remaining in the stack form the lexicographically smallest valid subsequence. Join them into a string.

---

# Example Walkthrough

Consider `s = "bcabc"`

1. **Initial Counts:** `b: 2, c: 2, a: 1`
2. **Iteration:**
   * **Char 'b':** Stack is empty. Push 'b'. 
     * *Stack:* `['b']`, *Counts:* `b:1, c:2, a:1`
   * **Char 'c':** 'c' > 'b'. Push 'c'. 
     * *Stack:* `['b', 'c']`, *Counts:* `b:1, c:1, a:1`
   * **Char 'a':** 'a' < 'c'. Can we pop 'c'? Yes, remaining 'c' > 0. Pop 'c'.
     * 'a' < 'b'. Can we pop 'b'? Yes, remaining 'b' > 0. Pop 'b'.
     * Push 'a'.
     * *Stack:* `['a']`, *Counts:* `b:1, c:1, a:0`
   * **Char 'b':** 'b' > 'a'. Push 'b'.
     * *Stack:* `['a', 'b']`, *Counts:* `b:0, c:1, a:0`
   * **Char 'c':** 'c' > 'b'. Push 'c'.
     * *Stack:* `['a', 'b', 'c']`, *Counts:* `b:0, c:0, a:0`

Result: `"abc"`.

---

# Complexity Analysis

Time Complexity

O(N)

Where `N` is the length of the string `s`. We iterate through the string twice: once to count the characters and once to build the stack. During the stack-building phase, each character is pushed and popped at most once. Therefore, the time complexity is strictly linear.

Space Complexity

O(1)

The sizes of the `num` and `vis` arrays are fixed at 26 (the number of lowercase English letters). The `stk` will also hold a maximum of 26 characters since all duplicates are ignored. Therefore, the auxiliary space used is constant $O(1)$ (or $O(|\Sigma|)$ where $\Sigma$ is the alphabet size).

---

# Code

```python
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        vis = [0] * 26
        num = [0] * 26

        # Count occurrences of each character
        for ch in s:
            num[ord(ch) - ord("a")] += 1
            
        stk = []

        for ch in s:
            idx = ord(ch) - ord("a")
            
            # If character is not already in our constructed string
            if not vis[idx]:
                # Pop characters that are lexicographically larger and appear later
                while stk and stk[-1] > ch:
                    top_idx = ord(stk[-1]) - ord("a")
                    if num[top_idx] > 0:
                        vis[top_idx] = 0
                        stk.pop()
                    else:
                        break
                        
                # Add current character
                vis[idx] = 1
                stk.append(ch)
                
            # Decrement the count of the current character
            num[idx] -= 1

        return "".join(stk)
```