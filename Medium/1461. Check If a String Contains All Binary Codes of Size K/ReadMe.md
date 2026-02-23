# 1461. Check If a String Contains All Binary Codes of Size K

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1461](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/)

---

## Problem
Given a binary string `s` and an integer `k`, return `true` if **every binary code of length `k`** is a substring of `s`. Otherwise return `false`.

A binary code of length `k` is any binary string of size `k` containing only `0` and `1`.

Example:

Input  
s = "00110110", k = 2  

Output  
true

Explanation  
Possible binary codes of length 2:  
00, 01, 10, 11  

All of them appear in the string.

---

# Approach

The key idea is to track all unique binary substrings of length `k`.

Total possible binary codes of size `k`:

2^k

If we manage to see all of them while scanning the string, we can immediately return `True`.

Instead of extracting substrings every time (which is slower), we use a **rolling binary window**.

This works like a sliding window that keeps the last `k` bits as a number.

Steps:

1. Calculate how many codes we need.
2. Use a set to store seen codes.
3. Build the current window using bit operations.
4. Keep only the last `k` bits using a mask.
5. Once the window size reaches `k`, store it.
6. If the set size becomes `2^k`, return `True`.

---

# Code

```python
class Solution(object):
    def hasAllCodes(self, s, k):
        need = 1 << k
        seen = set()

        num = 0
        mask = need - 1

        for i in range(len(s)):
            num = ((num << 1) & mask) | int(s[i])

            if i >= k - 1:
                seen.add(num)
                if len(seen) == need:
                    return True

        return False
```

---

# Example Walkthrough

Example:

s = "00110110"  
k = 2

Binary codes of length 2:

00  
01  
10  
11  

While scanning the string we see:

00  
01  
11  
10  

Once all four are discovered, we return `True`.

---

# Complexity Analysis

Time Complexity

O(n)

We scan the string once.

Space Complexity

O(2^k)

In the worst case we store every possible binary code.
