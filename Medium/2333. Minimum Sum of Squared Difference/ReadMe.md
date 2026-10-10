# 2333. Minimum Sum of Squared Difference

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2333](https://leetcode.com/problems/minimum-sum-of-squared-difference/description/)

---

## Problem
You are given two positive integer arrays `nums1` and `nums2`, both of length `n`.

The **sum of squared difference** of arrays `nums1` and `nums2` is defined as the sum of `(nums1[i] - nums2[i])^2` for each `0 <= i < n`.

You are also given two positive integers `k1` and `k2`. You can modify any of the elements of `nums1` by `+1` or `-1` at most `k1` times. Similarly, you can modify any of the elements of `nums2` by `+1` or `-1` at most `k2` times.

Return the minimum **sum of squared difference** after modifying array `nums1` at most `k1` times and modifying array `nums2` at most `k2` times.

---

# Approach

Modifying `nums1[i]` or `nums2[i]` by 1 allows us to decrease the absolute difference `|nums1[i] - nums2[i]|` by 1. Since we want to minimize the sum of squares, and the function $f(x) = x^2$ grows quadratically, we get the largest reduction in the total sum by reducing the **largest absolute differences** first. (For example, reducing a difference from 5 to 4 saves 9, while reducing from 2 to 1 only saves 3).

Furthermore, the separate limits `k1` and `k2` can just be combined into a single pool of operations: `k = k1 + k2`.

Steps:
1. **Calculate Differences**: Compute the absolute differences `d = [|a - b| for a, b in zip(nums1, nums2)]`. 
2. **Early Exit**: If the sum of all differences is less than or equal to `k`, we can reduce every difference to `0`. The answer is `0`.
3. **Sort and Pad**: Sort the differences in descending order. Append a `0` at the end to act as a floor/boundary condition.
4. **Greedy Leveling (Histogram Approach)**:
   * Iterate through the sorted differences. At step `i`, we have a group of `i` elements that share the current maximum difference `d[i-1]`.
   * We calculate the `cost` to reduce all these `i` elements down to the next highest value `d[i]`. The cost is `(d[i-1] - d[i]) * i`.
   * **If `cost <= k`**: We have enough operations to level them all down. We subtract `cost` from `k` and continue to the next iteration.
   * **If `cost > k`**: We don't have enough operations to reach `d[i]`. We distribute our remaining `k` operations evenly among the `i` elements. Each element gets reduced by `q = k // i`. The remainder `r = k % i` means that `r` elements get reduced by one extra unit (`q + 1`). 
5. **Final Computation**: Once the operations are exhausted, we calculate the sum of squares for the modified elements, add the sum of squares for the remaining untouched elements, and return the result.

---

# Code

```python
class Solution:
    def minSumSquareDiff(
        self, nums1: List[int], nums2: List[int], k1: int, k2: int
    ) -> int:
        k = k1 + k2
        d = [abs(a - b) for a, b in zip(nums1, nums2)]
        
        # If we have enough operations to reduce all differences to 0
        if sum(d) <= k:
            return 0

        d.sort(reverse=True)
        d.append(0)
        n = len(nums1)

        for i in range(1, n + 1):
            # Cost to bring the top i elements down to the level of the (i+1)-th element
            cost = (d[i - 1] - d[i]) * i
            
            if cost > k:
                # We can't level them all down to d[i].
                # Distribute the remaining k operations evenly among the i elements.
                q, r = divmod(k, i)
                hi = d[i - 1] - q
                
                return (
                    hi * hi * (i - r)           # Elements reduced by q
                    + (hi - 1) * (hi - 1) * r   # Elements reduced by q + 1
                    + sum(x * x for x in d[i:n]) # Untouched remaining elements
                )
                
            k -= cost
            
        return 0
```

---

# Example Walkthrough

Let `nums1 = [1, 2, 3, 4]`, `nums2 = [2, 10, 20, 19]`, `k1 = 1`, `k2 = 5`.
* `k = 1 + 5 = 6`
* Differences `d = [1, 8, 17, 15]`
* Sort descending: `d = [17, 15, 8, 1]`
* Pad with 0: `d = [17, 15, 8, 1, 0]`

**Iteration `i = 1`:**
* Trying to level `d[0]` (17) down to `d[1]` (15).
* `cost = (17 - 15) * 1 = 2`.
* `cost (2) <= k (6)`. We can do it! 
* `k = 6 - 2 = 4`. The maximum elements are now conceptually `[15, 15, 8, 1, 0]`.

**Iteration `i = 2`:**
* Trying to level the top 2 elements (both 15) down to `d[2]` (8).
* `cost = (15 - 8) * 2 = 14`.
* `cost (14) > k (4)`. We can't reach 8. We must distribute `k=4` across the 2 elements.
* `q, r = divmod(4, 2)` $\rightarrow$ `q = 2, r = 0`.
* Both elements are reduced by 2. New value `hi = 15 - 2 = 13`.
* 2 elements become 13 (r=0 elements become 12).
* Untouched elements from index 2 onwards: `8`, `1`.

**Final calculation:**
* $13^2 \times 2 + 12^2 \times 0 + 8^2 + 1^2$
* $169 \times 2 + 0 + 64 + 1$
* $338 + 65 = 403$.

Return `403`.

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(N \log N)$

Calculating the initial differences takes $\mathcal{O}(N)$. Sorting the array of differences takes $\mathcal{O}(N \log N)$. The greedy leveling pass visits each element at most once, taking $\mathcal{O}(N)$ time. The overall time complexity is dominated by the sorting step.

Space Complexity

$\mathcal{O}(N)$

We create a new array `d` of size $N+1$ to store the absolute differences between `nums1` and `nums2`. Therefore, the auxiliary space is strictly linear with respect to the input size.