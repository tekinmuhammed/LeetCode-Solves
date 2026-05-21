# 3043. Find the Length of the Longest Common Prefix

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3043](https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/)

---

## Problem
You are given two arrays with positive integers `arr1` and `arr2`.

A **prefix** of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit. For example, `123` is a prefix of the integer `12345`, while `234` is not.

A **common prefix** of two integers `a` and `b` is an integer `c`, such that `c` is a prefix of both `a` and `b`. For example, `5655359` and `56554` have a common prefix `5655` while `1223` and `43456` do not have a common prefix.

You need to find the length of the **longest common prefix** between all pairs of integers `(x, y)` such that `x` belongs to `arr1` and `y` belongs to `arr2`.

Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return `0`.

---

# Approach

While prefix problems are often solved using a `Trie` (Prefix Tree) with strings, this solution uses a highly efficient **Mathematical and Hash Set** approach. Instead of slicing strings, it uses integer division (`// 10`) to dynamically generate prefixes.

Steps:

1. **Build a Prefix Set from `arr1`:** 
   * We initialize an empty Hash Set (`arr1_prefixes`).
   * We iterate through each number in `arr1`.
   * For each number, we add it to the set, and then "chop off" its last digit by performing integer division by 10 (`val //= 10`).
   * We repeat this until the number becomes `0` or we encounter a prefix that is already in the set (an early stopping optimization).
2. **Search for Longest Match in `arr2`:**
   * We iterate through each number in `arr2`.
   * For each number, we check if it exists in our `arr1_prefixes` set.
   * If it doesn't, we chop off its last digit (`val //= 10`) and check again. 
   * Since we are checking from the longest possible prefix down to the shortest, the *first* match we find for any number is guaranteed to be its longest common prefix with `arr1`.
3. **Calculate Length:** 
   * Once a match is found (`val > 0`), we calculate its length by converting the numeric prefix to a string (`len(str(val))`).
   * We keep track of the maximum length found across all elements in `arr2`.

---

# Example Walkthrough

Consider `arr1 = [1, 10, 100]` and `arr2 = [1000]`

**Step 1: Process `arr1`**
* `val = 1`: Add `1` -> `val //= 10` -> `0` (Stop).
* `val = 10`: Add `10` -> `1` (Already in set, Stop).
* `val = 100`: Add `100` -> `10` (Already in set, Stop).
* `arr1_prefixes = {1, 10, 100}`

**Step 2: Process `arr2`**
* `val = 1000`. Is `1000` in set? **No**.
* `val //= 10` -> `100`. Is `100` in set? **Yes!**
* Prefix found: `100`. Length: `len(str(100))` = `3`.
* Max prefix length updated to `3`.

Return `3`.

---

# Complexity Analysis

Time Complexity

O((N + M) \times D)

Where `N` is the length of `arr1`, `M` is the length of `arr2`, and `D` is the maximum number of digits in the integers. Since the problem constraints usually limit values to $10^8$ or $10^9$, $D \le 9$. Therefore, $D$ is a constant, making the time complexity effectively **O(N + M)**. Converting to strings and hashing take minimal time since the string length is bounded by a small constant.

Space Complexity

O(N \times D)

We store all unique prefixes of every element in `arr1` inside the hash set. In the worst case, every digit of every number creates a unique prefix. Since $D$ is tightly bounded, the space complexity grows linearly with the size of `arr1`.

---

# Code

```python
class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        arr1_prefixes = set()  # Set to store all prefixes from arr1

        # Step 1: Build all possible prefixes from arr1
        for val in arr1:
            while val not in arr1_prefixes and val > 0:
                # Insert current value as a prefix
                arr1_prefixes.add(val)
                # Generate the next shorter prefix by removing the last digit
                val //= 10

        longest_prefix = 0

        # Step 2: Check each number in arr2 for the longest matching prefix
        for val in arr2:
            while val not in arr1_prefixes and val > 0:
                # Reduce val by removing the last digit if not found in the prefix set
                val //= 10
            if val > 0:
                # Length of the matched prefix using log10 to determine the number of digits
                # Here string conversion is used to count digits
                longest_prefix = max(longest_prefix, len(str(val)))

        return longest_prefix
```