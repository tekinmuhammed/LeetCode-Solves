# 3464. Maximize the Distance Between Points on a Square

**Difficulty:** Hard  
**Problem Link:** [LeetCode 3464](https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/)

---

## Problem Description

You are given an integer `side` representing the length of the side of a square with corners at `(0,0)`, `(0, side)`, `(side, side)`, and `(side, 0)`. You are also given a 2D integer array `points` where each `points[i] = [x, y]` represents a point on the **boundary** of the square, and an integer `k`.

You need to select `k` points from the given `points` such that the **minimum distance** between any two adjacent points (along the boundary) is **maximized**.

Return the maximum possible minimum distance.

---

## Approach: Linearization + Binary Search on Answer

Since the points are on the boundary of a square, the problem can be transformed into finding points on a 1D line of length $4 \times side$ (the perimeter) that is circular.

### Key Ideas:
1.  **Linearization:** We map each 2D point $(x, y)$ to a single 1D coordinate $d$ representing its distance from $(0,0)$ traveling counter-clockwise:
    - If $x=0$: $d = y$
    - If $y=side$: $d = side + x$
    - If $x=side$: $d = 3 \cdot side - y$
    - If $y=0$: $d = 4 \cdot side - x$
2.  **Binary Search on Answer:** The phrase "maximize the minimum distance" is a classic hint for binary search. We search for the largest value `limit` such that we can pick `k` points with all adjacent distances $\ge limit$.
3.  **Greedy Check (Circular):** To check if a `limit` is possible:
    - Since the points are on a circle (boundary), the starting point matters. We try starting from each point in `arr`.
    - From a starting point, we greedily pick the next available point that is at least `limit` away using `bisect_left`.
    - After picking `k` points, we must ensure the distance between the $k^{th}$ point and the $1^{st}$ point (wrapping around the perimeter) is also $\ge limit$.



---

## Code

```python
from bisect import bisect_left

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        """
        :type side: int
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        arr = []
        # Step 1: Linearize 2D boundary points to 1D coordinates
        for x, y in points:
            if x == 0:
                arr.append(y)
            elif y == side:
                arr.append(side + x)
            elif x == side:
                arr.append(side * 3 - y)
            else:
                arr.append(side * 4 - x)
        
        arr.sort()
        n = len(arr)
        perimeter = side * 4
        
        def check(limit: int) -> bool:
            # Try starting from each point to handle the circular constraint
            for i in range(n):
                start_val = arr[i]
                # The k-th point must be picked before this bound to leave 
                # space for the final gap back to start_val
                end_bound = start_val + perimeter - limit
                
                count = 1
                curr_pos = start_val
                
                for _ in range(k - 1):
                    # Greedily find the next point at least 'limit' distance away
                    idx = bisect_left(arr, curr_pos + limit)
                    if idx == n or arr[idx] > end_bound:
                        break
                    curr_pos = arr[idx]
                    count += 1
                
                if count == k:
                    return True
            return False
        
        # Step 2: Binary Search for the maximum possible minimum distance
        lo, hi = 1, side  # hi can be up to perimeter // k
        ans = 0
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
                
        return ans
```

---

## Complexity Analysis

* **Time Complexity:** $O(\log(Perimeter) \cdot N \cdot K \log N)$
    - Binary search runs $\log(4 \cdot side)$ times.
    - The `check` function iterates through $N$ starting points and performs $K$ binary searches (`bisect_left`).
    - *Note: In practice, the number of starting points to check can often be reduced, but for these constraints, this approach passes.*
* **Space Complexity:** $O(N)$
    - To store the linearized and sorted coordinates of the points in `arr`.

---

## Tags
Binary-Search, Greedy, Geometry, Sorting, Circular-Array