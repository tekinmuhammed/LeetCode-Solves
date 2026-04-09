# 3655. XOR After Range Multiplication Queries II

**Difficulty:** Hard
**Problem Link:** [LeetCode 3655](https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/description/)

---

## Problem Description

You are given an integer array `nums` and a 2D integer array `queries` where `queries[i] = [l, r, k, v]`.

For each query, update `nums[i] = (nums[i] * v) % (10^9 + 7)` for all $i$ such that $l \le i \le r$ and $(i - l) \pmod k == 0$.

After processing all queries, return the **XOR sum** of all elements in the final `nums` array. In this version, the constraints on $N$ and $Q$ are significantly higher, making a simple simulation $O(Q \cdot N)$ too slow.

---

## Approach: Square Root Decomposition (Step-wise Optimization)

To handle the queries efficiently, we divide them into two categories based on the step size $k$, using a threshold $T = \sqrt{N}$.

### 1. Large Step Sizes ($k \ge \sqrt{N}$)
When $k$ is large, the number of elements to update in the range $[l, r]$ is relatively small (at most $\sqrt{N}$ elements). For these, we can afford to use **direct simulation**.

### 2. Small Step Sizes ($k < \sqrt{N}$)
When $k$ is small, direct simulation could take $O(N)$ per query. Instead, we use a **Multiplicative Difference Array** approach:
- For each unique $k$, we maintain a difference array `dif`.
- For a query $(l, r, v)$, we update `dif[l] *= v` and `dif[R] *= inv(v)`, where $R$ is the first index after $r$ that follows the $k$-step sequence.
- After processing all queries for a specific $k$, we calculate the prefix products with a step of $k$: `dif[i] = dif[i] * dif[i-k]`.
- This effectively applies all multiplications to the correct indices in $O(N)$ for each $k$.

### Key Mathematical Tool: Modular Inverse
Since we need to "undo" a multiplication in the difference array, we use **Fermat's Little Theorem** to find the modular multiplicative inverse:
$$v^{MOD-2} \equiv v^{-1} \pmod{MOD}$$

---

## Code

```python
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        T = int(n**0.5) # Square root threshold

        # Group queries with small k to process them in bulk
        groups = [[] for _ in range(T)]
        for l, r, k, v in queries:
            if k < T:
                groups[k].append((l, r, v))
            else:
                # Large k: Direct simulation is efficient enough
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % mod

        # Process small k using a step-based difference array
        dif = [1] * (n + T)
        for k in range(1, T):
            if not groups[k]:
                continue
            
            # Reset difference array for the current step k
            dif[:] = [1] * len(dif)
            for l, r, v in groups[k]:
                dif[l] = dif[l] * v % mod
                # Calculate the boundary index to stop the multiplication
                R = ((r - l) // k + 1) * k + l
                dif[R] = dif[R] * pow(v, mod - 2, mod) % mod

            # Compute prefix products with step k
            for i in range(k, n):
                dif[i] = dif[i] * dif[i - k] % mod
            
            # Apply the accumulated multipliers to the original nums
            for i in range(n):
                nums[i] = nums[i] * dif[i] % mod

        # Final result is the XOR sum of all modified elements
        res = 0
        for x in nums:
            res ^= x
        return res
```

---

## Example Walkthrough (Small $k$)

Assume $n=6, k=2$ and query is $l=0, r=4, v=3$.
1.  **Mark boundaries:** `dif[0] = 3`, `dif[6] = inv(3)`.
2.  **Prefix Product (step 2):**
    - `dif[2] = dif[2] * dif[0] = 1 * 3 = 3`
    - `dif[4] = dif[4] * dif[2] = 1 * 3 = 3`
    - `dif[6] = dif[6] * dif[4] = inv(3) * 3 = 1`
3.  Indices 0, 2, and 4 are now correctly set to be multiplied by 3.

---

## Complexity Analysis

* **Time Complexity:** $O((Q + N) \sqrt{N})$
    - Processing large $k$ queries: $O(Q \cdot \frac{N}{\sqrt{N}}) = O(Q\sqrt{N})$.
    - Processing small $k$ groups: At most $\sqrt{N}$ groups, each taking $O(N)$ or $O(Q_{small\_k})$ to process. Total: $O(N\sqrt{N})$.
* **Space Complexity:** $O(N + \sqrt{N})$
    - `dif` array takes $O(N)$, and `groups` stores queries.

---

## Tags
`Square-Root-Decomposition`, `Difference-Array`, `Modular-Inverse`, `Math`, `XOR`