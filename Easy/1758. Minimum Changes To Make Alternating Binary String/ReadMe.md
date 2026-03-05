# 1758. Minimum Changes To Make Alternating Binary String

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1758](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/)

---

## Problem Description

Given a binary string `s`, return the minimum number of operations needed to make `s` **alternating**.

A string is called alternating if no two adjacent characters are equal. For example, the string `"0101"` is alternating, while the string `"0100"` is not.

An operation consists of changing `'0'` to `'1'` or vice versa.

---

## Approach

The core idea is to realize that there are only **two possible alternating patterns** for any given length $n$:
1.  **Pattern 1:** Starts with '0' (e.g., `010101...`)
2.  **Pattern 2:** Starts with '1' (e.g., `101010...`)

### Key Ideas:
- We iterate through the string `s` once.
- For each character at index `i`, we check if it matches what **Pattern 1** should have and what **Pattern 2** should have at that position.
- **Pattern 1 Logic:**
    - If `i` is even, character should be `'0'`.
    - If `i` is odd, character should be `'1'`.
- **Pattern 2 Logic:**
    - If `i` is even, character should be `'1'`.
    - If `i` is odd, character should be `'0'`.
- We count the number of mismatches for both patterns and return the minimum of the two.

> **Pro Tip:** In reality, `change2` is always equal to `len(s) - change1`. However, calculating both explicitly as done in the code is very clear and easy to follow.

---

## Code

```python
class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        change1 = 0  # pattern starting with '0' -> 010101...
        change2 = 0  # pattern starting with '1' -> 101010...
        
        for i in range(len(s)):
            if i % 2 == 0:
                # Even indices
                if s[i] != '0':
                    change1 += 1
                if s[i] != '1':
                    change2 += 1
            else:
                # Odd indices
                if s[i] != '1':
                    change1 += 1
                if s[i] != '0':
                    change2 += 1
        
        return min(change1, change2)
```

---

## Example Walkthrough

**Input:** `s = "0110"`

1.  **Index 0 (Even):** `s[0] = '0'`. Matches Pattern 1, Mismatches Pattern 2. (`change2 = 1`)
2.  **Index 1 (Odd):** `s[1] = '1'`. Matches Pattern 1, Mismatches Pattern 2. (`change2 = 2`)
3.  **Index 2 (Even):** `s[2] = '1'`. Mismatches Pattern 1, Matches Pattern 2. (`change1 = 1`)
4.  **Index 3 (Odd):** `s[3] = '0'`. Mismatches Pattern 1, Matches Pattern 2. (`change1 = 2`)

**Final Counts:** `change1 = 2`, `change2 = 2`.  
**Result:** `min(2, 2) = 2`.

---

## Complexity Analysis

* **Time Complexity:** $O(n)$
    - We perform a single pass through the string of length $n$.
* **Space Complexity:** $O(1)$
    - We only use two integer variables (`change1`, `change2`) regardless of the input size.

---

## Tags
String, Greedy, Simulation