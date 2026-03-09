a# 3129. Find All Possible Stable Binary Arrays I

**Difficulty:** Medium/Hard  
**Problem Link:** [LeetCode 3129](https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/)

---

## Problem Description

Given three positive integers `zero`, `one`, and `limit`, return the number of **stable** binary arrays that can be formed.

A binary array is **stable** if:
1. It contains exactly `zero` number of 0s.
2. It contains exactly `one` number of 1s.
3. Each **subsegment** of identical elements has a length of **at most** `limit`.

Since the answer may be very large, return it **modulo $10^9 + 7$**.

---

## Approach: Dynamic Programming

The problem requires counting combinations with specific constraints on consecutive elements. A **3D Dynamic Programming** approach is ideal for tracking the count of used digits and the last placed digit.

### DP State:
$DP[i][j][k]$ represents the number of stable arrays using $i$ zeros and $j$ ones, ending with digit $k$ (where $k=0$ or $k=1$).

### Transition Logic:
To find $DP[i][j][0]$ (ending in 0):
1.  **Base Case:** We can append a `0` to any stable array that used $i-1$ zeros and $j$ ones, whether it ended in `0` or `1`.
    - $DP[i][j][0] = DP[i-1][j][0] + DP[i-1][j][1]$
2.  **Constraint Handling:** If the number of zeros $i$ exceeds the `limit`, we must subtract the invalid cases. An invalid case occurs when we have `limit + 1` consecutive zeros.
    - This happens if the sequence ended with a `1` followed by exactly `limit` zeros, and we just added another `0`.
    - The number of such cases is $DP[i - (limit + 1)][j][1]$.

The same logic applies symmetrically to $DP[i][j][1]$.



---

## Code

```python
class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        """
        :type zero: int
        :type one: int
        :type limit: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # dp[i][j][k]: number of stable arrays using i zeros, j ones, ending with k
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base cases: Arrays consisting of only one type of digit within the limit
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
            
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Calculate arrays ending in 0
                # Add all stable arrays from the previous step (i-1 zeros)
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                # Subtract cases that violate the limit (limit + 1 consecutive zeros)
                if i > limit:
                    # Subtract arrays that were stable at (i-limit-1, j) and ended with 1
                    # because adding (limit + 1) zeros now makes them unstable.
                    dp[i][j][0] = (dp[i][j][0] - dp[i-limit-1][j][1] + MOD) % MOD
                
                # Calculate arrays ending in 1 (symmetric logic)
                dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                if j > limit:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j-limit-1][0] + MOD) % MOD
                    
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
```

---

## Example Walkthrough

**Input:** `zero = 1, one = 1, limit = 2`

1.  **Initialize:** `dp[1][0][0] = 1` ("0"), `dp[0][1][1] = 1` ("1")
2.  **Iteration (i=1, j=1):**
    - `dp[1][1][0] = (dp[0][1][0] + dp[0][1][1]) = (0 + 1) = 1` (Array: "10")
    - `dp[1][1][1] = (dp[1][0][0] + dp[1][0][1]) = (1 + 0) = 1` (Array: "01")
3.  **Result:** `dp[1][1][0] + dp[1][1][1] = 2` ("10" and "01")

---

## Complexity Analysis

* **Time Complexity:** $O(zero \times one)$
    - We use a nested loop to fill the 2D matrix (zeros by ones). Each operation inside is $O(1)$.
* **Space Complexity:** $O(zero \times one)$
    - We store a 3D table of size `(zero + 1) * (one + 1) * 2`.

---

## Tags
Dynamic-Programming, Combinatorics, Prefix-Sum-Optimization, Array