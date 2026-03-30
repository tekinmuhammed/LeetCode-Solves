# 2840. Check if Strings Can be Made Equal With Operations II

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2840](https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/)

---

## Problem Description

You are given two strings `s1` and `s2` of equal length $n$, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:
- Choose two indices `i` and `j` such that `i < j`, the difference `j - i` is **even**, and swap the characters at these two indices.

Return `true` if you can make the strings `s1` and `s2` equal, and `false` otherwise.

---

## Approach: Parity-Based Grouping

The operation allows swapping characters at indices $i$ and $j$ if $(j - i)$ is even. This means:
- If $i$ is even, $j$ must also be even (e.g., $0, 2, 4, \dots$).
- If $i$ is odd, $j$ must also be odd (e.g., $1, 3, 5, \dots$).

### Key Ideas:
1.  **Independent Systems:** Characters at even indices can be moved to any other even index position through a series of swaps. They can **never** move to an odd index. The same applies to characters at odd indices.
2.  **Multiset Equality:** For `s1` to be transformed into `s2`, the collection of characters at even positions in both strings must be identical. Similarly, the collection of characters at odd positions must match.
3.  **Pythonic Implementation:** We use slicing (`[::2]` for even and `[1::2]` for odd) to extract these groups, sort them, and compare them.

---

## Code

```python
class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Strings can be equal if:
        # 1. Characters at even indices in s1 match those in s2 (ignoring order)
        # 2. Characters at odd indices in s1 match those in s2 (ignoring order)
        return (
            sorted(s1[::2]) == sorted(s2[::2]) and
            sorted(s1[1::2]) == sorted(s2[1::2])
        )
```

---

## Example Walkthrough

**Input:** `s1 = "abcdba", s2 = "cabdab"`

1.  **Even Indices (0, 2, 4):**
    - `s1[::2]` $\rightarrow$ "aba" $\rightarrow$ sorted: `['a', 'a', 'b']`
    - `s2[::2]` $\rightarrow$ "cda" $\rightarrow$ sorted: `['a', 'c', 'd']`
    - **No Match!** (Characters are different).

**Result:** `False`

**Input:** `s1 = "abe", s2 = "eba"`
1.  **Even Indices (0, 2):** `s1: "ae"`, `s2: "ea"` $\rightarrow$ Both sort to `['a', 'e']`. **Match!**
2.  **Odd Indices (1):** `s1: "b"`, `s2: "b"` $\rightarrow$ Both sort to `['b']`. **Match!**

**Result:** `True`

---

## Complexity Analysis

* **Time Complexity:** $O(n \log n)$
    - Slicing takes $O(n)$.
    - Sorting the two halves (each of size $n/2$) takes $O(\frac{n}{2} \log \frac{n}{2})$, which simplifies to $O(n \log n)$.
* **Space Complexity:** $O(n)$
    - We create new lists to store the sorted characters of each parity.

---

## Tags
String, Sorting, Slicing, Parity, Multiset