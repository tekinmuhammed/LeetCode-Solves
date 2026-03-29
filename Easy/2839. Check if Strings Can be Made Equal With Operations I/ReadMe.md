# 2839. Check if Strings Can be Made Equal With Operations I

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2839](https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/description/)

---

## Problem Description

You are given two strings `s1` and `s2`, both of length 4, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:
- Choose two indices `i` and `j` such that `j - i = 2`, then swap the characters at these two indices in the string.

Return `true` if you can make the strings `s1` and `s2` equal, and `false` otherwise.

---

## Approach: Index Parity Analysis

The core constraint is the swap operation: you can only swap characters if the distance between their indices is exactly **2**. This leads to an important observation:

### Key Ideas:
1.  **Isolation by Parity:** - A character at an **even index** (0 or 2) can only be swapped with another character at an **even index**.
    - A character at an **odd index** (1 or 3) can only be swapped with another character at an **odd index**.
2.  **Independent Groups:** The problem effectively splits the 4-character string into two independent groups of 2 characters each.
3.  **Condition for Equality:** For `s1` to become `s2`, the **multiset** (the specific characters and their counts) of characters at even indices must be identical for both strings. The same must hold true for the odd indices.
4.  **Sorting for Comparison:** By sorting the characters at each parity, we can easily check if the sets are identical.

---

## Code

```python
class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Group and sort characters at even indices (index 0 and 2)
        s1_even = sorted([s1[0], s1[2]])
        s2_even = sorted([s2[0], s2[2]])
        
        # Group and sort characters at odd indices (index 1 and 3)
        s1_odd = sorted([s1[1], s1[3]])
        s2_odd = sorted([s2[1], s2[3]])
        
        # The strings can be made equal if both even and odd sets match
        return s1_even == s2_even and s1_odd == s2_odd
```

---

## Example Walkthrough

**Input:** `s1 = "abcd", s2 = "cdab"`

1.  **Even Parity (Indices 0, 2):**
    - `s1[0, 2]` is `['a', 'c']` $\rightarrow$ sorted: `['a', 'c']`
    - `s2[0, 2]` is `['c', 'a']` $\rightarrow$ sorted: `['a', 'c']`
    - **Match!**
2.  **Odd Parity (Indices 1, 3):**
    - `s1[1, 3]` is `['b', 'd']` $\rightarrow$ sorted: `['b', 'd']`
    - `s2[1, 3]` is `['d', 'b']` $\rightarrow$ sorted: `['b', 'd']`
    - **Match!**

**Result:** `True`

---

## Complexity Analysis

* **Time Complexity:** $O(1)$
    - Since the string length is fixed at 4, the number of operations is constant regardless of the input.
* **Space Complexity:** $O(1)$
    - We only use a small, fixed amount of space to store and sort the 2-character lists.

---

## Tags
`String`, `Sorting`, `Parity`, `Logic`