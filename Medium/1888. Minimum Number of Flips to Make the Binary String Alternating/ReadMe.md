# 1888. Minimum Number of Flips to Make the Binary String Alternating

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1888](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/)

---

## Problem Description

You are given a binary string `s`. You can perform two types of operations:
- **Type-1:** Remove the first character of `s` and append it to the end.
- **Type-2:** Choose any character of `s` and flip it (0 to 1 or 1 to 0).

Return the **minimum** number of Type-2 operations to make `s` **alternating**.

An alternating string is a string where no two adjacent characters are equal (e.g., `"0101"` or `"1010"`).

---

## Approach

The Type-1 operation allows us to cyclically shift the string. The core challenge is finding which cyclic shift requires the fewest flips. Instead of simulating every shift, we use a **Sliding Window** on a doubled string.

### Key Ideas:
1.  **Doubling the String:** To simulate all possible Type-1 operations (cyclic shifts) in linear time, we concatenate the string with itself: `s = s + s`. Any window of size $n$ in this new string represents a possible version of `s` after some Type-1 operations.
2.  **Target Patterns:** There are only two possible alternating patterns of length $2n$:
    - `alt1`: `010101...`
    - `alt2`: `101010...`
3.  **Sliding Window:** We maintain a window of size $n$ and track how many characters in the current window differ from `alt1` and `alt2`.
4.  **Efficiency:** As the window moves:
    - Add the new character's difference to the total.
    - Remove the character that left the window from the total.
    - Update the global minimum result.

---

## Code

```python
class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # Double the string to simulate all cyclic shifts
        s = s + s
        
        # Create the two possible target alternating patterns
        alt1 = ""
        alt2 = ""
        for i in range(2 * n):
            alt1 += "0" if i % 2 == 0 else "1"
            alt2 += "1" if i % 2 == 0 else "0"
        
        diff1 = diff2 = 0
        res = float('inf')
        left = 0
        
        # Slide a window of size n across the 2n length string
        for right in range(2 * n):
            # Add new character at 'right' to current differences
            if s[right] != alt1[right]:
                diff1 += 1
            if s[right] != alt2[right]:
                diff2 += 1
            
            # If window exceeds size n, remove the leftmost character
            if (right - left + 1) > n:
                if s[left] != alt1[left]:
                    diff1 -= 1
                if s[left] != alt2[left]:
                    diff2 -= 1
                left += 1
            
            # Once window is exactly size n, record the minimum flips
            if (right - left + 1) == n:
                res = min(res, diff1, diff2)
        
        return res
```

---

## Example Walkthrough

**Input:** `s = "111000"` ($n=6$)
1.  **Doubled String:** `111000111000`
2.  **Patterns:** - `alt1: 010101...`
    - `alt2: 101010...`
3.  **Window 1 (indices 0-5):** `111000` vs `010101` -> `diff1=3`, `diff2=3`
4.  **Shifted Window (indices 1-6):** `110001` vs `101010` -> ...
5.  **Result:** The algorithm finds the window that minimizes these differences across all cyclic shifts.

---

## Complexity Analysis

* **Time Complexity:** $O(n)$
    - Constructing `alt1` and `alt2` takes $O(n)$.
    - The sliding window loop runs $2n$ times, with each operation inside being $O(1)$.
* **Space Complexity:** $O(n)$
    - We store the doubled string and the two target patterns, all of which are proportional to $n$.

---

## Tags
String, Sliding-Window, Greedy, Dynamic-Programming