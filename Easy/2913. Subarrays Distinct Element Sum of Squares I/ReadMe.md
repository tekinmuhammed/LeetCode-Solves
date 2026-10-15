# 2913. Subarrays Distinct Element Sum of Squares I

**Difficulty:** Easy 
**Problem Link:** [LeetCode 2913](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/description/)

---

## Problem
You are given a 0-indexed integer array `nums`.

The **distinct count** of a subarray of `nums` is defined as:
* Let `nums[i..j]` be a subarray of `nums` consisting of all the indices from `i` to `j` such that `0 <= i <= j < nums.length`. The number of distinct values in that subarray is denoted by `count`.

Return the sum of the squares of the distinct counts of all subarrays of `nums`.

Since the answer may be very large, return it modulo $10^9 + 7$.

Example:

Input  
nums = [1, 2, 1]  

Output  
15  

Explanation  
All possible subarrays:
- `[1]`: 1 distinct value, square = 1
- `[2]`: 1 distinct value, square = 1
- `[1]`: 1 distinct value, square = 1
- `[1, 2]`: 2 distinct values, square = 4
- `[2, 1]`: 2 distinct values, square = 4
- `[1, 2, 1]`: 2 distinct values, square = 4

Sum of squares = 1 + 1 + 1 + 4 + 4 + 4 = 15.

---

# Approach

While LeetCode 2913 features small constraints suitable for a straightforward $\mathcal{O}(N^2)$ brute-force check of all subarrays, your solution employs an advanced, highly optimized **Fenwick Tree (Binary Indexed Tree - BIT) with Range Updates / Range Queries** approach. This technique is typically used for the Hard variant (LeetCode 2916) to solve the problem in $\mathcal{O}(N \log N)$ time.

### Core Mathematical Insight
When we extend all subarrays ending at index $i-1$ by appending a new element `A[i]`:
* If `A[i]` has appeared previously at index `j`, the count of distinct elements in subarrays starting from indices $0$ through $j$ **does not change** because the duplicate element is already accounted for.
* For subarrays starting from indices $j+1$ through $i$, the count of distinct elements **increases by 1**.

If we let $count(l)$ be the number of distinct elements in the subarray from index $l$ to $i-1$, updating to index $i$ changes the distinct count sum:
$$\sum_{l=0}^{i} (count(l))^2$$

Using the binomial expansion $(x + 1)^2 = x^2 + 2x + 1$, updating a range $[j, i]$ by incrementing each count by 1 updates the sum of squares as:
$$\sum (count(l) + 1)^2 = \sum (count(l)^2 + 2 \cdot count(l) + 1)$$

### Algorithm Breakdown:
1. **BIT Structures**: A customized `BIT` class maintains two underlying trees (`_tree1` and `_tree2`) to support range additions and range sum queries efficiently in $\mathcal{O}(\log N)$ time.
2. **Last Seen Tracking**: We use a hash map `seen` to track the previous occurrence index of each element. If an element is new, its previous index boundary defaults to `-1`.
3. **Dynamic Range Update**: For each element `A[i]`, we query the range sum of squares from the last occurrence index $j$ to the current index $i$, update the BIT with a delta of `1`, and accumulate the result modulo $10^9 + 7$.

---

# Code

```python
from collections import defaultdict
from typing import List

class BIT:
    def __init__(self, n: int):
        self.size = n
        self._tree1 = defaultdict(int)
        self._tree2 = defaultdict(int)

    def _lowbit(self, index: int) -> int:
        return index & -index

    def add(self, left: int, right: int, delta: int) -> None:
        self._add(left, delta)
        self._add(right + 1, -delta)

    def query(self, left: int, right: int) -> int:
        return self._query(right) - self._query(left - 1)

    def _add(self, index: int, delta: int) -> None:
        index += 1
        if index < 0:
            raise ValueError("index must be a positive integer")

        rawIndex = index
        while index <= self.size:
            self._tree1[index] += delta
            self._tree2[index] += (rawIndex - 1) * delta
            index += self._lowbit(index)

    def _query(self, index: int) -> int:
        index += 1
        if index > self.size:
            index = self.size

        rawIndex = index
        res = 0
        while index > 0:
            res += rawIndex * self._tree1[index] - self._tree2[index]
            index -= self._lowbit(index)
        return res


class Solution:
    def sumCounts(self, A: List[int]) -> int:
        n = len(A)
        res = cur = 0
        bit = BIT(n + 10)
        seen = {}
        mod = 10**9 + 7
        
        for i, a in enumerate(A):
            j = seen.get(a, -1) + 1
            cur += bit.query(j, i) * 2 + i - j + 1
            res += cur
            bit.add(j, i, 1)
            seen[a] = i
            
        return res % mod