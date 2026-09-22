# 3525. Find X Value of Array II

**Difficulty:** Hard 
**Problem Link:** [LeetCode 3525](https://leetcode.com/problems/find-x-value-of-array-ii/description/)

---

## Problem
You are given an integer array `nums`, an integer `k`, and a 2D array of `queries`. Each query is represented as `[index, value, start, x]`.

For each query, you must perform two steps:
1. **Update**: Change the element at `nums[index]` to `value`.
2. **Query**: Consider the subarray starting at index `start` and going to the end of the array (`nums[start...n-1]`). Find the number of **prefix subarrays** of this subarray whose product modulo `k` equals `x`.

Return an array containing the answers to all queries.

---

# Approach

Because we have point updates and range queries, a **Segment Tree** is the perfect data structure. However, storing just the product of a range isn't enough; we need to count prefixes. 

We can design the Segment Tree such that every node (representing an array segment `[L, R]`) maintains:
1. **`mul`**: The total product of all elements in the segment `[L, R]` modulo `k`.
2. **`pre`**: An array of size `k` where `pre[r]` stores the number of prefix subarrays of `[L, R]` whose product modulo `k` evaluates to `r`.

**How to merge two Segment Tree nodes (Left and Right)?**
When we combine a Left segment and a Right segment to form a parent segment:
* The new total product is simply `(Left.mul * Right.mul) % k`.
* The prefixes of the parent segment come from two sources:
  1. **Entirely within the Left segment**: These are exactly the prefixes of the Left segment. We just copy `Left.pre`.
  2. **Spanning across into the Right segment**: These consist of the *entire* Left segment multiplied by a prefix of the Right segment. For every remainder `x` that exists in `Right.pre`, it contributes to the parent's remainder at `(Left.mul * x) % k`.

This logic allows us to update elements in $\mathcal{O}(K \log N)$ time and query ranges in $\mathcal{O}(K \log N)$ time.

---

# Code

```python
class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.k = k
        n = len(nums)
        size = 2 << n.bit_length()

        # tree[o] = pre + [mul]
        self.tree = [[0] * (k + 1) for _ in range(size)]

        self.build(nums, 1, 0, n - 1)

    def makeLeaf(self, o: int, value: int) -> None:
        info = [0] * (self.k + 1)
        r = value % self.k
        info[r] = 1
        info[self.k] = r  # mul
        self.tree[o] = info

    def mergePre(self, left: List[int], right: List[int]) -> List[int]:
        pre = [0] * (self.k + 1)

        mul_L = left[self.k]
        mul_R = right[self.k]

        # Remainder of the product of the entire interval
        pre[self.k] = (mul_L * mul_R) % self.k

        # Case 1: Entirely within the left interval
        for x in range(self.k):
            pre[x] = left[x]

        # Case 2: Contains the entire left interval, followed by a prefix of the right interval
        for x in range(self.k):
            pre[(mul_L * x) % self.k] += right[x]

        return pre

    def maintain(self, o: int) -> None:
        self.tree[o] = self.mergePre(
            self.tree[o * 2],
            self.tree[o * 2 + 1],
        )

    def build(self, nums: List[int], o: int, l: int, r: int) -> None:
        if l == r:
            self.makeLeaf(o, nums[l])
            return

        m = (l + r) // 2
        self.build(nums, o * 2, l, m)
        self.build(nums, o * 2 + 1, m + 1, r)
        self.maintain(o)

    def update(self, o: int, l: int, r: int, index: int, value: int) -> None:
        if l == r:
            self.makeLeaf(o, value)
            return

        m = (l + r) // 2
        if index <= m:
            self.update(o * 2, l, m, index, value)
        else:
            self.update(o * 2 + 1, m + 1, r, index, value)

        self.maintain(o)

    def query(self, o: int, l: int, r: int, L: int, R: int) -> List[int]:
        if L <= l and r <= R:
            return self.tree[o]

        m = (l + r) // 2
        if R <= m:
            return self.query(o * 2, l, m, L, R)
        if L > m:
            return self.query(o * 2 + 1, m + 1, r, L, R)

        left = self.query(o * 2, l, m, L, R)
        right = self.query(o * 2 + 1, m + 1, r, L, R)
        return self.mergePre(left, right)


class Solution:
    def resultArray(
        self, nums: List[int], k: int, queries: List[List[int]]
    ) -> List[int]:
        n = len(nums)
        seg = SegmentTree(nums, k)

        ans = []
        for index, value, start, x in queries:
            seg.update(1, 0, n - 1, index, value)
            pre = seg.query(1, 0, n - 1, start, n - 1)
            ans.append(pre[x])

        return ans
```

---

# Example Walkthrough

Imagine a scenario where we merge two nodes in the Segment Tree.
Let `k = 5`. 
Left child represents `[2]`. Right child represents `[3]`.

1. **Left Child Leaf (`value = 2`)**:
   * `mul` = 2 % 5 = `2`
   * `pre[2]` = `1` (prefix `[2]`)
   
2. **Right Child Leaf (`value = 3`)**:
   * `mul` = 3 % 5 = `3`
   * `pre[3]` = `1` (prefix `[3]`)

3. **Merging to Parent**:
   * **New `mul`**: `(2 * 3) % 5 = 1`
   * **Case 1 (Left prefixes)**: Copy `Left.pre`. So, `pre[2] = 1`.
   * **Case 2 (Spanning prefixes)**: Multiply Left's `mul` (which is 2) by every remainder in `Right.pre`. 
     * Right has `pre[3] = 1`.
     * New remainder = `(2 * 3) % 5 = 1`. 
     * Add Right's count to this new remainder: `pre[1] += 1`.
   * **Final Parent Node State**: `mul = 1`, `pre[2] = 1`, `pre[1] = 1`. (Represents prefixes `[2]` and `[2, 3]`).

Whenever a query asks for subarrays starting at `start`, the segment tree quickly fetches the pre-calculated node covering `[start, n-1]` and returns `pre[x]`.

---

# Complexity Analysis

Time Complexity

* **Tree Construction**: $\mathcal{O}(N \cdot K)$. There are $\approx 4N$ nodes, and merging takes $\mathcal{O}(K)$ steps.
* **Point Update**: $\mathcal{O}(K \log N)$. The tree depth is $\log N$. At each of the $\log N$ levels, we perform a merge taking $\mathcal{O}(K)$.
* **Range Query**: $\mathcal{O}(K \log N)$. We visit at most $\approx 2 \log N$ nodes and merge them.
* **Total Time Complexity**: $\mathcal{O}((N + Q) \cdot K \log N)$, where $Q$ is the number of queries. This easily passes constraints for moderately small $K$.

Space Complexity

$\mathcal{O}(N \cdot K)$

The Segment Tree array is allocated with a size of roughly $4N$. Each node in the tree stores a list of size $K + 1$. Thus, the total space is strictly proportional to $N \times K$.