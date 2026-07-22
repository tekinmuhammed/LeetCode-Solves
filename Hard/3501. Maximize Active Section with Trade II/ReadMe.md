# 3501. Maximize Active Section with Trade II

**Difficulty:** Hard
**Problem Link:** [LeetCode 3501](https://leetcode.com/problems/maximize-active-section-with-trade-ii/description/)

--- 
 
## Problem 
Given a binary string `s` and a 2D integer array `queries` where each query is of the form `[l, r]`, you need to calculate the maximum possible active sections for each query. 
 
The base number of active sections is the total count of `'1'`s in the entire string. For each query range `[l, r]`, you are allowed to "trade" (or convert) up to **two adjacent blocks of `'0'`s** into `'1'`s to maximize the total number of `'1'`s. Only the portions of the `'0'` blocks that fall within the query boundaries `[l, r]` can be converted.
 
Return an array of integers, where each integer is the answer to the corresponding query. 
 
--- 
 
# Approach 
 
To process multiple queries efficiently without rescanning the string every time, we need to preprocess the string into blocks and use advanced data structures to quickly query maximums in a given range. 
 
Steps: 
1. **Block Parsing**: 
   Iterate through the string `s` to find all contiguous blocks of `'0'`s. We store the length of each block, along with its start and end indices. 
2. **Precomputing Adjacency**: 
   Since we can trade up to two *adjacent* blocks of `'0'`s (separated by a block of `'1'`s), we create an array `tmpSum` where each element is the sum of two adjacent `'0'` blocks: `tmpSum[i] = zeroBlocks[i] + zeroBlocks[i + 1]`.
3. **Segment Tree**: 
   We build a **Segment Tree** over the `tmpSum` array. This allows us to find the maximum pair of adjacent `'0'` blocks within any index range in $O(\log M)$ time.
4. **Query Processing with Binary Search**: 
   For each query `[l, r]`:
   * Use `bisect_left` and `bisect_right` to quickly find which `'0'` blocks intersect with the range `[l, r]`.
   * **Boundary Handling**: The first and last blocks in the range might be partially cut off by `l` or `r`. We calculate their bounded lengths (`firstLen` and `lastLen`).
   * **Max Gain Calculation**: The best trade inside the query can come from:
     1. The truncated first block + the second block.
     2. The second-to-last block + the truncated last block.
     3. Any two adjacent fully contained blocks between the first and last blocks (using our Segment Tree query).
   * Add the maximum of these options to the total count of `'1'`s in the string.
 
--- 
 
# Code 

```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.seg = [0] * (self.n << 2)

        if self.n:
            self.build(1, 0, self.n - 1)

    def build(self, p: int, l: int, r: int) -> None:
        if l == r:
            self.seg[p] = self.arr[l]
            return

        mid = (l + r) >> 1

        self.build(p << 1, l, mid)
        self.build(p << 1 | 1, mid + 1, r)

        self.seg[p] = max(self.seg[p << 1], self.seg[p << 1 | 1])

    def query(self, L: int, R: int) -> int:
        if L > R:
            return 0

        def _query(p: int, l: int, r: int) -> int:
            if L <= l and r <= R:
                return self.seg[p]

            mid = (l + r) >> 1
            res = 0

            if L <= mid:
                res = max(res, _query(p << 1, l, mid))

            if R > mid:
                res = max(res, _query(p << 1 | 1, mid + 1, r))

            return res

        return _query(1, 0, self.n - 1)


class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
        n = len(s)
        cnt1 = s.count("1")

        zeroBlocks = []
        blockLeft = []
        blockRight = []

        i = 0
        while i < n:
            st = i

            while i < n and s[i] == s[st]:
                i += 1

            if s[st] == "0":
                zeroBlocks.append(i - st)
                blockLeft.append(st)
                blockRight.append(i - 1)

        m = len(zeroBlocks)
        if (
            m < 2
        ):  # continuous 0 blocks less than 2 segments, return the answer directly
            return [cnt1] * len(queries)

        tmpSum = [zeroBlocks[i] + zeroBlocks[i + 1] for i in range(m - 1)]
        seg = SegmentTree(tmpSum)
        ans = []

        from bisect import bisect_left, bisect_right

        for l, r in queries:
            i = bisect_left(blockRight, l)
            j = bisect_right(blockLeft, r) - 1

            # at most 1 continuous block of 0s within the substring
            if i > m - 1 or j < 0 or i >= j:
                ans.append(cnt1)
                continue

            firstLen = (
                blockRight[i] - max(blockLeft[i], l) + 1
            )  # actual length of the first consecutive block of 0s in the substring

            lastLen = (
                min(blockRight[j], r) - blockLeft[j] + 1
            )  # actual length of the last consecutive block of 0s in the substring

            # exactly 2 consecutive 0 blocks within the substring
            if i + 1 == j:
                bestGain = firstLen + lastLen
                ans.append(cnt1 + bestGain)
                continue

            val1 = firstLen + zeroBlocks[i + 1]
            val2 = zeroBlocks[j - 1] + lastLen
            val3 = seg.query(i + 1, j - 2)

            bestGain = max(val1, val2, val3)
            ans.append(cnt1 + bestGain)

        return ans
```

---

# Complexity Analysis

Time Complexity

- **Preprocessing:** $\mathcal{O}(N)$ to scan the string and build the blocks, where $N$ is the length of the string.
- **Segment Tree Construction:** $\mathcal{O}(M)$ where $M$ is the number of `'0'` blocks ($M \le N/2$).
- **Query Processing:** For each of the $Q$ queries, binary search takes $\mathcal{O}(\log M)$ and querying the segment tree takes $\mathcal{O}(\log M)$.
- **Total Time Complexity:** $\mathcal{O}(N + Q \log M)$, which is extremely efficient and fast enough to pass typical competitive programming constraints.

Space Complexity

- **Storage Arrays:** $\mathcal{O}(M)$ to store lengths and indices of the `'0'` blocks.
- **Segment Tree:** $\mathcal{O}(M)$ since the array size in a segment tree is bounded by $4M$.
- **Total Space Complexity:** $\mathcal{O}(N)$ bounded by the string size.