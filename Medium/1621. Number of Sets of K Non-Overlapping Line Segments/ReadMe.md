# 1621. Number of Sets of K Non-Overlapping Line Segments

**Difficulty:** Medium
**Problem Link:** [LeetCode 1621](https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/description/)

---

## Problem
Given $n$ points on a 1-D plane, where the points are numbered from $0$ to $n-1$. You are asked to draw $k$ non-overlapping line segments. 

* The segments are allowed to share endpoints (e.g., a segment from $0$ to $1$ and a segment from $1$ to $2$ are valid and non-overlapping).
* Return the number of ways we can draw the $k$ line segments. Since the answer can be huge, return it **modulo** $10^9 + 7$.

Example:

Input  
n = 4, k = 2  

Output  
5  

Explanation  
The two line segments can be drawn in 5 ways:
1. [0,1] and [1,2]
2. [0,1] and [2,3]
3. [0,2] and [2,3]
4. [1,2] and [2,3]
5. [0,1] and [1,3]

---

# Approach

A standard Dynamic Programming approach would define $dp[i][j]$ as the number of ways to draw $i$ segments using the first $j$ points. However, a naive state transition takes $\mathcal{O}(N)$ time, leading to an overall $\mathcal{O}(K \cdot N^2)$ time complexity, which would result in a Time Limit Exceeded (TLE) error.

To optimize this, we can use **1D Dynamic Programming combined with Prefix Sums**.

Steps:
1. **State Initialization**: We start with `dp = [1] * n`. This represents the base case of $0$ segments: there is exactly $1$ way to draw $0$ segments for any number of points.
2. **Prefix Sums Array**: We maintain a `prefix_sums` array where `prefix_sums[j + 1]` stores the sum of valid configurations from the previous iteration. This allows us to calculate the transition for the next segment in $\mathcal{O}(1)$ time instead of $\mathcal{O}(N)$.
3. **Iterate for $K$ Segments**: We loop $k$ times. For each segment:
   * We cannot draw a segment with only $1$ point, so `dp[0] = 0`.
   * For the remaining points, the number of ways to form segments up to point $j$ is the sum of:
     * The number of ways ignoring point $j$ (`dp[j - 1]`).
     * The number of ways to add a new segment ending at point $j$, which is fetched instantly from our `prefix_sums[j]`.
4. **Modulo Arithmetic**: At every addition, we take modulo $10^9 + 7$ to prevent overflow and comply with the problem constraints.
5. The final answer lies in `dp[n - 1]`.

---

# Code

```python
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [1] * n
        prefix_sums = [0] * (n + 1)
        
        for j in range(n):
            prefix_sums[j + 1] = (prefix_sums[j] + dp[j]) % mod
            
        for _ in range(k):
            dp[0] = 0
            for j in range(1, n):
                dp[j] = (dp[j - 1] + prefix_sums[j]) % mod
            for j in range(n):
                prefix_sums[j + 1] = (prefix_sums[j] + dp[j]) % mod
                
        return dp[n - 1]
```

---

# Example Walkthrough

Let `n = 4`, `k = 2`.

**Initial state (0 segments):**
`dp` = `[1, 1, 1, 1]`  
`prefix_sums` = `[0, 1, 2, 3, 4]`

**Iteration 1 (1 segment):**
* `dp[0]` = `0`
* `dp[1]` = `dp[0] + prefix_sums[1]` = `0 + 1 = 1` 
* `dp[2]` = `dp[1] + prefix_sums[2]` = `1 + 2 = 3` 
* `dp[3]` = `dp[2] + prefix_sums[3]` = `3 + 3 = 6`  
`dp` becomes `[0, 1, 3, 6]` (Ways to make 1 segment out of 1, 2, 3, 4 points).  
Recalculate `prefix_sums`: `[0, 0, 1, 4, 10]`

**Iteration 2 (2 segments):**
* `dp[0]` = `0`
* `dp[1]` = `0 + 0 = 0` (Can't make 2 segments with 2 points).
* `dp[2]` = `0 + 1 = 1` 
* `dp[3]` = `1 + 4 = 5` 
`dp` becomes `[0, 0, 1, 5]`.

Result is `dp[3] = 5`.

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(N \cdot K)$

We have an outer loop running $K$ times. Inside, we have two independent loops that iterate $N$ times each. Calculating the transitions using the prefix sums takes $\mathcal{O}(1)$ per state, making the overall time complexity strictly proportional to $N \times K$.

Space Complexity

$\mathcal{O}(N)$

We optimized the standard 2D DP table down to two 1D arrays: `dp` and `prefix_sums`, both of size $\approx N$. Thus, the space complexity is $\mathcal{O}(N)$.