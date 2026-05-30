# 3161. Block Placement Queries

**Difficulty:** Hard
**Problem Link:** [LeetCode 3161](https://leetcode.com/problems/block-placement-queries/description/)

---

## Problem
There is an infinite number line with its origin at 0 and extending towards the positive x-axis. 
 
You are given a 2D array `queries`, which contains two types of queries:
1. `[1, x]`: Build an obstacle at coordinate `x`.
2. `[2, x, sz]`: Check if it is possible to place a block of size `sz` anywhere in the range `[0, x]` such that the block entirely lies in the range `[0, x]`. A block cannot overlap with any obstacle, but it can touch them.
 
Return a boolean array `results`, where `results[i]` is `true` if you can place the block specified in the `i`-th query of type 2, and `false` otherwise.
 
--- 
 
# Approach 
 
This problem requires us to dynamically track the sizes of gaps between obstacles and efficiently query the maximum gap within a specific range. A naive approach would result in a Time Limit Exceeded (TLE) error. 
 
To achieve optimal performance, this solution combines two powerful data structures: a **Segment Tree** and a **SortedList**.
 
### Data Structures Used: 
1. **SortedList (`self.st`)**: Keeps track of all the coordinates where obstacles are placed. This allows us to find the immediately preceding and succeeding obstacles of any given coordinate `x` in $O(\log N)$ time.
2. **Segment Tree (`self.seg`)**: Stores the maximum gap sizes. The value at index `idx` in the segment tree represents the distance from the *previous* obstacle to the obstacle at `idx`. The segment tree is built over the coordinate domain `[0, 50000]`. 
 
### Handling Queries: 
* **Initialization:** We assume obstacles at `0` and `50000` (the maximum possible coordinate constraint). The gap at `50000` is initialized to `50000`.
* **Type 1 (Build Obstacle at `x`):** * We use the `SortedList` to find the obstacle immediately before `x` (let's call it `l`) and the obstacle immediately after `x` (let's call it `r`).
  * Placing an obstacle at `x` splits the existing gap between `l` and `r` into two new smaller gaps: `[l, x]` and `[x, r]`.
  * We update the Segment Tree: the gap size ending at `x` becomes `x - l`, and the gap size ending at `r` becomes `r - x`.
  * Finally, we insert `x` into the `SortedList`.
* **Type 2 (Check for space `sz` before `x`):**
  * We find the last obstacle placed strictly before or at `x` (let's call it `pre`).
  * The maximum available space before `x` is the maximum of two values:
    1. The partial gap from the last obstacle `pre` up to our boundary `x` (`x - pre`).
    2. The maximum full gap completely to the left of `pre`, which we find by querying our Segment Tree in the range `[0, pre]`.
  * If this maximum space is `>= sz`, the result is `True`; otherwise, `False`.
 
--- 
 
# Complexity Analysis 
 
Time Complexity 
 
O(Q \log M) 
 
Where `Q` is the number of queries and `M` is the maximum coordinate boundary (50000).  
- Finding neighbors and inserting into `SortedList` takes $O(\log Q)$ time.
- Updating the Segment Tree and querying the maximum range takes $O(\log M)$ time per operation.
Since both operations are strictly logarithmic, the overall time complexity easily scales within the constraints.

Space Complexity 
 
O(M + Q) 
 
The Segment Tree array requires $4 \times M$ space, where $M = 50000$. The `SortedList` will store at most $Q$ elements (one for each Type 1 query). Therefore, the memory usage is linearly proportional to the coordinate limit and the number of queries.

---

# Code

```python
from sortedcontainers import SortedList
from typing import List

class Solution:
    def __init__(self):
        self.seg = []
        self.st = SortedList()
        self.mx = 50000

    def update(self, idx: int, val: int, p: int, l: int, r: int) -> None:
        if l == r:
            self.seg[p] = val
            return

        mid = (l + r) >> 1
        if idx <= mid:
            self.update(idx, val, p << 1, l, mid)
        else:
            self.update(idx, val, p << 1 | 1, mid + 1, r)

        self.seg[p] = max(self.seg[p << 1], self.seg[p << 1 | 1])

    def query(self, L: int, R: int, p: int, l: int, r: int) -> int:
        if L <= l and r <= R:
            return self.seg[p]

        mid = (l + r) >> 1
        res = 0
        if L <= mid:
            res = max(res, self.query(L, R, p << 1, l, mid))
        if R > mid:
            res = max(res, self.query(L, R, p << 1 | 1, mid + 1, r))

        return res

    def getResults(self, queries: List[List[int]]) -> List[bool]:
        self.mx = 50000
        # Initialize segment tree array (size 4 * max_coordinate)
        self.seg = [0] * (self.mx << 2)
        # Boundaries
        self.st = SortedList([0, self.mx])
        self.update(self.mx, self.mx, 1, 0, self.mx)
        
        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]
                # Find the next obstacle 'r'
                idx = min(len(self.st) - 1, self.st.bisect_right(x))
                r = self.st[idx]
                # Find the previous obstacle 'l'
                l = self.st[idx - 1] if idx > 0 else self.st[0]
                
                # Update the gaps in the segment tree
                self.update(x, x - l, 1, 0, self.mx)
                self.update(r, r - x, 1, 0, self.mx)
                self.st.add(x)
            else:
                x, sz = q[1], q[2]
                # Find the closest obstacle before or at 'x'
                idx = min(len(self.st) - 1, self.st.bisect_right(x))
                pre = self.st[0] if idx == 0 else self.st[idx - 1]

                # Max space is either the distance from the last obstacle to 'x', 
                # or the maximum gap between any two obstacles before 'pre'
                max_space = max(x - pre, self.query(0, pre, 1, 0, self.mx))
                ans.append(max_space >= sz)

        return ans
```