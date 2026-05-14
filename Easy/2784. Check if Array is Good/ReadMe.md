# 2784. Check if Array is Good

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2784](https://leetcode.com/problems/check-if-array-is-good/description/)

---

## Problem
You are given an integer array `nums`. We consider an array **good** if it is a permutation of an array `base[n]`.

`base[n] = [1, 2, ..., n - 1, n, n]` (in other words, it is an array of length `n + 1` which contains `1` to `n - 1` exactly once, plus two occurrences of `n`).

Return `true` if the given array is good, otherwise return `false`.

*(Note: In the context of the code below, let `L` be the length of `nums`. If `nums` is good, its maximum element must be `L - 1`, and this element must appear exactly twice, while all elements from `1` to `L - 2` must appear exactly once.)*

---

# Approach

A brute-force approach would be to sort the array and compare it directly to a generated `base` array, which takes $O(N \log N)$ time. We can optimize this to $O(N)$ by using a frequency counting array.

Since an array of length `n` is only "good" if it contains numbers exactly from `1` to `n - 1` with a specific frequency, we can iterate through `nums` and track the counts:

1. **Length Validation:** Let `n = len(nums)`. The maximum allowed number in a good array of length `n` is `n - 1`.
2. **Frequency Array:** We initialize a `count` array of size `n` with zeros to keep track of how many times we've seen each number.
3. **Iterate & Validate:** For each number `a` in `nums`:
   * If `a >= n`, the number is strictly out of the allowed bounds. We immediately return `False`.
   * If `a < n - 1` and we have already seen it (`count[a] > 0`), it's an illegal duplicate. Return `False`.
   * If `a == n - 1` (the maximum element) and we have already seen it twice (`count[a] > 1`), it has appeared too many times. Return `False`.
   * Otherwise, we increment its count (`count[a] += 1`).
4. If the loop completes without triggering any `False` conditions, the pigeonhole principle guarantees that the array exactly matches the required permutation. We return `True`.

---

# Example Walkthrough

Consider `nums = [1, 3, 3, 2]`  
Length `n = 4`.  
Valid good array should contain: `1, 2, 3, 3`.

Initialize `count = [0, 0, 0, 0]`

1. **First element (`1`):**
   * `1 < 4` (valid)
   * `count[1] == 0` (valid)
   * Update: `count = [0, 1, 0, 0]`
2. **Second element (`3`):**
   * `3 == 4 - 1` (this is our max element)
   * `count[3] == 0` (valid)
   * Update: `count = [0, 1, 0, 1]`
3. **Third element (`3`):**
   * `3 == 4 - 1` 
   * `count[3] == 1`, which is not `> 1` yet. (valid, we need exactly two of these)
   * Update: `count = [0, 1, 0, 2]`
4. **Fourth element (`2`):**
   * `2 < 3`
   * `count[2] == 0` (valid)
   * Update: `count = [0, 1, 1, 2]`

Loop finishes without errors. Return `True`.

---

# Complexity Analysis

Time Complexity

O(N)

We iterate through the `nums` array exactly once. The array indexing and logical checks inside the loop take $O(1)$ time each.

Space Complexity

O(N)

We create a `count` array of length `N` (where `N` is the length of `nums`) to store the frequencies of the elements.

---

# Code

```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        count = [0] * n
        for a in nums:
            if a >= n:
                return False
            if a < n - 1 and count[a] > 0:
                return False
            if a == n - 1 and count[a] > 1:
                return False
            count[a] += 1
        return True
```