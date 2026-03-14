# 1415. The k-th Lexicographical String of All Happy Strings of Length n

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1415](https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)

---

## Problem Description

A **happy string** is a string that:
- Consists only of letters of the set `['a', 'b', 'c']`.
- `s[i] != s[i + 1]` for all values of `i` from `1` to `s.length - 1` (string is 1-indexed).

For example, strings **"abc"**, **"acb"**, **"aba"** are happy strings, while **"aa"**, **"baa"**, **"abcc"** are not.

Given two integers `n` and `k`, consider a list of all happy strings of length `n` sorted lexicographically. Return the $k^{th}$ string of this list or return an **empty string** if there are less than `k` happy strings of length `n`.

---

## Approach: Backtracking (DFS)

Since we need the $k^{th}$ string in **lexicographical order**, we can use a Backtracking (DFS) approach by exploring characters in the order `'a', 'b', 'c'`.

### Key Ideas:
1.  **Exploration Order:** By always trying to add `'a'`, then `'b'`, and finally `'c'`, the DFS tree naturally explores the strings in alphabetical order.
2.  **Happy Condition:** Before adding a character to the current path, we check if it is different from the last added character (`path[-1] != c`).
3.  **Early Exit:** Once we have found $k$ happy strings, there is no need to explore the rest of the state space. We can return immediately.
4.  **Base Case:** When the length of the `path` reaches `n`, we have found a valid happy string and add it to our result list.



---

## Code

```python
class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []

        def dfs(path):
            # Pruning: stop if we already found k strings
            if len(res) >= k:
                return
            
            # Base Case: found a happy string of length n
            if len(path) == n:
                res.append(path)
                return

            # Try 'a', 'b', and 'c' in order to maintain lexicographical sorting
            for c in ['a', 'b', 'c']:
                # Ensure the 'happy' condition: no two adjacent characters are the same
                if not path or path[-1] != c:
                    dfs(path + c)

        dfs("")
        
        # If we found at least k strings, return the k-th one (0-indexed)
        if len(res) < k:
            return ""
        
        return res[k-1]
```

---

## Example Walkthrough

**Input:** `n = 3, k = 9`

1.  **Root:** Start with `""`.
2.  **Level 1:** Try `a`, `b`, `c`.
3.  **Level 2 (under `a`):** Try `ab`, `ac`.
4.  **Level 3 (under `ab`):** Try `aba`, `abc`.
5.  The strings will be generated in this order:
    1. `aba`
    2. `abc`
    3. `aca`
    4. `acb`
    5. `bab` ... and so on.
6.  The 9th string found will be `"cab"`.

---

## Complexity Analysis

* **Time Complexity:** $O(k \cdot n)$ or $O(3 \cdot 2^{n-1})$
    - In the worst case, there are $3 \times 2^{n-1}$ happy strings. We visit each character up to $n$ times. Since we stop at $k$, the complexity is effectively $O(k \cdot n)$.
* **Space Complexity:** $O(n)$
    - The maximum depth of the recursion tree is $n$, which determines the space used by the call stack.

---

## Tags
Backtracking, DFS, String, Lexicographical-Order