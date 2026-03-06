# 1784. Check if Binary String Has at Most One Segment of Ones

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1784](https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/)

---

## Problem Description

Given a binary string `s` **without leading zeros**, return `true` if `s` contains **at most one contiguous segment of ones**. Otherwise, return `false`.

---

## Approach

The problem states that the string `s` does **not** have leading zeros, meaning it always starts with `'1'`. 

### Key Idea:
If the string starts with `'1'`, the only way to have **more than one segment of ones** is if a `'0'` appears and is eventually followed by another `'1'`. 

In other words, if the substring `"01"` exists anywhere in the string, it means:
1.  A segment of ones has ended (at least one `'0'` appeared).
2.  A new segment of ones has started (a `'1'` appeared after that `'0'`).

Therefore, the problem reduces to a simple check: Does the sequence `"01"` exist in the string?

---

## Code

```python
class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # If "01" is not in s, there's at most one segment of ones.
        return "01" not in s
```

---

## Example Walkthrough

**Example 1:**
- **Input:** `s = "1001"`
- **Analysis:** The string contains `"01"` at index 2.
- **Result:** `False` (Two segments of ones: the first '1' and the last '1').

**Example 2:**
- **Input:** `s = "110"`
- **Analysis:** The string does not contain `"01"`.
- **Result:** `True` (Only one segment of ones).

---

## Complexity Analysis

* **Time Complexity:** $O(n)$
    - Python's `in` operator (substring search) performs a scan of the string, which takes linear time relative to the length of the string.
* **Space Complexity:** $O(1)$
    - No additional data structures or memory are used.

---

## Tags
`String`, `Binary-String`, `Greedy`, `Minimalist-Solution`