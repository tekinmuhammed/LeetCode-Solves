# 3653. XOR After Range Multiplication Queries I

**Difficulty:** Medium 
**Problem Link:** [LeetCode 3653](https://leetcode.com/problems/xor-after-range-multiplication-queries-i/description/)

---

## Problem Description

You are given an integer array `nums` and a 2D integer array `queries` where `queries[i] = [l, r, k, v]`.

For each query:
- Starting from index `l` up to index `r`, multiply every $k^{th}$ element by `v`.
- Formally, update `nums[i] = (nums[i] * v) % (10^9 + 7)` for all $i$ such that $l \le i \le r$ and $(i - l) \pmod k == 0$.

After processing all queries, return the **XOR sum** of all elements in the final `nums` array.

---

## Approach: Direct Simulation

In this version of the problem, the constraints allow for a direct simulation of each query.

### Key Ideas:
1.  **Step-based Updates:** The condition $(i - l) \pmod k == 0$ simply means we start at $l$ and increment the index by $k$ until we exceed $r$. In Python, this is efficiently handled by `range(l, r + 1, k)`.
2.  **Modüler Arithmetic:** Since the values can grow very large, we apply the modulo $10^9 + 7$ at each multiplication step to prevent integer overflow and follow the problem's requirements.
3.  **XOR Accumulation:** Once all range multiplications are complete, we perform a final pass over the array to compute the XOR sum of all elements.
4.  **Bitwise XOR Property:** XOR is associative and commutative, so the order of elements doesn't matter, but here we simply iterate through the final state of the array.

---

## Code

```python
class Solution:
    # Standard modulo constant for competitive programming
    MOD = 10**9 + 7

    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        # Step 1: Process each query sequentially
        for l, r, k, v in queries:
            # range(l, r + 1, k) perfectly captures the (i - l) % k == 0 condition
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % self.MOD

        # Step 2: Calculate the final XOR sum of the modified array
        res = 0
        for x in nums:
            res ^= x

        return res
```

---

## Example Walkthrough

**Input:** `nums = [1, 2, 3], queries = [[0, 2, 2, 3]]`

1.  **Query [0, 2, 2, 3]:**
    - `l=0, r=2, k=2, v=3`.
    - Indices to update: $0$ and $2$ (since $0+2=2 \le 2$).
    - `nums[0] = (1 * 3) % MOD = 3`
    - `nums[2] = (3 * 3) % MOD = 9`
    - `nums` becomes `[3, 2, 9]`.
2.  **Final XOR Sum:**
    - `3 ^ 2 ^ 9`
    - `(0011 ^ 0010) ^ 1001`
    - `0001 ^ 1001 = 1000` (Decimal **8**).

**Result:** `8`

---

## Complexity Analysis

* **Time Complexity:** $O(Q \times \frac{N}{K} + N)$
    - $Q$ is the number of queries. For each query, we visit $N/K$ elements.
    - The final XOR pass takes $O(N)$.
    - In the worst case ($k=1$), each query takes $O(N)$ time.
* **Space Complexity:** $O(1)$ extra space
    - We modify the `nums` array in-place and use a single variable for the XOR result.

---

## Tags
`Array`, `Simulation`, `Bit-Manipulation`, `XOR`, `Modulo-Arithmetic`