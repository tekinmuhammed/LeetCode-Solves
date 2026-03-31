# 3474. Lexicographically Smallest Generated String

**Difficulty:** Hard  
**Problem Link:** [LeetCode 3474](https://leetcode.com/problems/lexicographically-smallest-generated-string/description/)

---

## Problem Description

Given two strings `str1` and `str2`, you need to construct a string `s` of length `len(str1) + len(str2) - 1` such that:
1. For every index `i` where `str1[i] == 'T'`, the substring `s[i : i + len(str2)]` is exactly equal to `str2`.
2. For every index `i` where `str1[i] == 'F'`, the substring `s[i : i + len(str2)]` is **not** equal to `str2`.

Return the **lexicographically smallest** string `s` that satisfies these conditions. If no such string exists, return an empty string `""`.

---

## Approach: Two-Pass Greedy

To find the lexicographically smallest string, we start with the smallest possible character ('a') for all positions and then apply constraints.

### Key Ideas:
1.  **Fixed Constraints ('T'):** - In the first pass, we process all 'T' indicators in `str1`. 
    - If `str1[i] == 'T'`, we must place `str2` starting at `s[i]`.
    - We mark these positions as `fixed`. If a conflict occurs (a position is already fixed with a different character), the construction is impossible.
2.  **Negative Constraints ('F'):**
    - In the second pass, we process 'F' indicators. 
    - If `str1[i] == 'F'`, we check if the current substring `s[i : i + len(str2)]` is equal to `str2`.
    - If it matches, we must change at least one character to break the match.
3.  **Lexicographical Minimization:**
    - To keep the string as small as possible, we only change a character if an 'F' constraint is violated.
    - When a change is needed, we look for the **rightmost** position in the current substring that is **not fixed**.
    - Changing the rightmost available character to 'b' (the next smallest option) ensures the string remains lexicographically smallest.

---

## Code

```python
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        n, m = len(str1), len(str2)
        # Initialize with 'a' (smallest char) and track fixed indices
        s = ["a"] * (n + m - 1)
        fixed = [False] * (n + m - 1)

        # First Pass: Process 'T' constraints (Mandatory matches)
        for i, ch in enumerate(str1):
            if ch == "T":
                for j in range(m):
                    pos = i + j
                    char_to_place = str2[j]
                    if fixed[pos] and s[pos] != char_to_place:
                        return ""  # Conflict found
                    s[pos] = char_to_place
                    fixed[pos] = True

        # Second Pass: Process 'F' constraints (Forbidden matches)
        for i, ch in enumerate(str1):
            if ch == "F":
                # Check if current substring matches str2
                match = True
                for j in range(m):
                    if s[i + j] != str2[j]:
                        match = False
                        break
                
                if match:
                    # Must change a character. To keep it smallest, 
                    # change the rightmost non-fixed character to 'b'.
                    changed = False
                    for j in range(m - 1, -1, -1):
                        pos = i + j
                        if not fixed[pos]:
                            s[pos] = "b"
                            changed = True
                            break
                    
                    if not changed:
                        return ""  # No characters could be changed

        return "".join(s)
```

---

## Example Walkthrough

**Input:** `str1 = "TFF", str2 = "ab"`

1.  **Initial:** `s = ["a", "a", "a", "a"]`, `fixed = [F, F, F, F]`
2.  **Process 'T' at index 0:** - `s[0:2]` becomes `"ab"`. `s = ["a", "b", "a", "a"]`.
    - `fixed = [T, T, F, F]`.
3.  **Process 'F' at index 1:**
    - Substring `s[1:3]` is `"ba"`. Not equal to `"ab"`. OK.
4.  **Process 'F' at index 2:**
    - Substring `s[2:4]` is `"aa"`. Not equal to `"ab"`. OK.

**Output:** `"abaa"`

---

## Complexity Analysis

* **Time Complexity:** $O(n \times m)$
    - We iterate through `str1` ($n$) and for each index, we potentially iterate through `str2` ($m$) twice (once for 'T' pass, once for 'F' pass).
* **Space Complexity:** $O(n + m)$
    - We store the resulting string and the `fixed` boolean array of length $n + m - 1$.

---

## Tags
`Greedy`, `String`, `Construction`, `Lexicographical-Order`, `Hard-Logic`