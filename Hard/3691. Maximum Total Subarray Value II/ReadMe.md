# 3691. Maximum Total Subarray Value II

**Difficulty:** Hard
**Problem Link:** [LeetCode 3691](https://leetcode.com/problems/maximum-total-subarray-value-ii/description/)

---

## Problem
You are given an integer array `nums` of length `n` and an integer `k`. You need to choose exactly `k` **distinct** non-empty subarrays of `nums`. 

The value of a subarray is defined as: `max(subarray) - min(subarray)`.
The total value is the sum of the values of all `k` chosen subarrays. 

Return the maximum possible total value you can achieve.

---

# Approach

To find the top $k$ distinct subarrays with the maximum values efficiently, we can combine a **Sparse Table** for fast Range Minimum/Maximum Queries (RMQ) with a **Priority Queue (Max-Heap)** to greedily extract the best subarrays.

### 1. Fast Range Queries using Sparse Table
Since we will need to repeatedly find the maximum and minimum elements of various subarrays `[l, r]`, doing this linearly would cause a Time Limit Exceeded (TLE) error. Instead, we precompute a **Sparse Table**. 
* Building the Sparse Table takes $O(N \log N)$ time.
* Once built, any `queryMax(l, r)` or `queryMin(l, r)` operates in strict $O(1)$ time.

### 2. Monotonicity of Subarray Values
The value of a subarray is $V(l, r) = \text{max}(l, r) - \text{min}(l, r)$. 
For a fixed left boundary `l`, as we expand the right boundary `r` further to the right, the maximum element can only stay the same or increase, and the minimum element can only stay the same or decrease. 
Therefore, for any fixed `l`, the value $V(l, r)$ is **monotonically increasing** with `r`. The absolute best subarray starting at index `l` is always the one ending at the very end of the array, `n - 1`.

### 3. K-th Largest Extraction via Max-Heap
* We initialize a Max-Heap with the absolute best subarray for every possible starting index `l`. So we push `n` elements into the heap: `(V(l, n - 1), l, n - 1)`.
* We extract the maximum value from the heap $k$ times to add to our `ans`.
* **The clever part:** When we pop a subarray `[l, r]` from the heap, the *next best* subarray starting at that exact same `l` is simply `[l, r - 1]`. If `r > l`, we compute $V(l, r - 1)$ and push it right back into the heap.
* This guarantees that we explore the search space strictly in descending order of subarray values without computing all $O(N^2)$ possibilities.

---

# Example Walkthrough

Assume we have an array of length `5` and we need `k = 3` distinct subarrays.

1. **Precomputation:** Build `stMax` and `stMin` tables in $O(N \log N)$.
2. **Initialize Heap:** For every index `l` from `0` to `4`, calculate $V(l, 4)$ and push to the max-heap. 
   Heap contains: `[ (V(0,4), 0, 4), (V(1,4), 1, 4), ... ]`
3. **Extraction 1:**
   * Pop the maximum. Suppose it's `(V(0, 4), 0, 4)`.
   * Add $V(0, 4)$ to `ans`.
   * Since $4 > 0$, the next best subarray starting at `0` is `[0, 3]`. Push `(V(0, 3), 0, 3)` to the heap.
4. **Extraction 2:**
   * Pop the maximum. Suppose it's `(V(1, 4), 1, 4)`.
   * Add $V(1, 4)$ to `ans`.
   * Push `(V(1, 3), 1, 3)` to the heap.
5. **Extraction 3:**
   * Pop the maximum. Add to `ans`. Push the next candidate.
6. Return `ans`.

---

# Complexity Analysis

Time Complexity

O((N + K) \log N)

* **Sparse Table Construction:** Creating the $O(\log N)$ layers for both `stMax` and `stMin` takes $O(N \log N)$ time.
* **Heap Initialization:** Inserting `N` elements into the heap using `heapify` takes $O(N)$ time.
* **Queries:** We pop and push to the heap exactly $K$ times. Each heap operation takes $O(\log N)$ time, resulting in $O(K \log N)$.
* Overall time is dominated by $O((N + K) \log N)$.

Space Complexity

O(N \log N)

The Sparse Tables (`stMax` and `stMin`) require $O(N \log N)$ space. The Priority Queue (`pq`) stores at most $N$ elements at any given time, taking $O(N)$ space. Total auxiliary space is $O(N \log N)$.

---

# Code

```python
import heapq
from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        logn = n.bit_length()
        
        # Build Sparse Tables for O(1) RMQ (Range Minimum/Maximum Query)
        stMax = [[0] * logn for _ in range(n)]
        stMin = [[0] * logn for _ in range(n)]
        for i in range(n):
            stMax[i][0] = stMin[i][0] = nums[i]
            
        for j in range(1, logn):
            step = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                stMax[i][j] = max(stMax[i][j - 1], stMax[i + step][j - 1])
                stMin[i][j] = min(stMin[i][j - 1], stMin[i + step][j - 1])

        def queryMax(l: int, r: int) -> int:
            j = (r - l + 1).bit_length() - 1
            return max(stMax[l][j], stMax[r - (1 << j) + 1][j])

        def queryMin(l: int, r: int) -> int:
            j = (r - l + 1).bit_length() - 1
            return min(stMin[l][j], stMin[r - (1 << j) + 1][j])

        # Initialize Max-Heap with the best possible subarray for each starting index 'l'
        # Since heapq is a min-heap, we use negative values to simulate a max-heap
        pq = [
            (-(queryMax(l, n - 1) - queryMin(l, n - 1)), l, n - 1)
            for l in range(n)
        ]
        heapq.heapify(pq)
        
        ans = 0
        while k:
            negVal, l, r = heapq.heappop(pq)
            ans -= negVal
            k -= 1
            
            # If we can shrink the subarray from the right, push the next best candidate
            if r > l:
                heapq.heappush(
                    pq, (-(queryMax(l, r - 1) - queryMin(l, r - 1)), l, r - 1)
                )
                
        return ans
```