# 3740. Minimum Distance Between Three Equal Elements I

**Difficulty:** Easy
**Problem Link:** [LeetCode 3740](https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/description/)

---

## Problem Description

You are given an integer array `nums`. You need to find three indices `i`, `j`, and `k` such that:
1.  $0 \le i < j < k < nums.length$
2.  $nums[i] == nums[j] == nums[k]$

The **distance** between these three elements is defined as the sum of their pairwise absolute differences: $|i - j| + |j - k| + |k - i|$.

Return the **minimum possible distance**. If no such three indices exist, return `-1`.

---

## Approach: Brute Force with Greedy Optimization

Since this is the first version of the problem with smaller constraints, we can use a nested loop approach to find all triplets of equal elements.

### Key Ideas:
1.  **Iterative Search:** We use three nested loops to pick indices $i$, $j$, and $k$ where $i < j < k$.
2.  **Equality Check:** For every triplet, we check if $nums[i] == nums[j]$ and then if $nums[j] == nums[k]$.
3.  **Distance Calculation:** For $i < j < k$, the sum of distances simplifies mathematically:
    $$(j - i) + (k - j) + (k - i) = 2 \times (k - i)$$
    Instead of calculating the full sum every time, we find the minimum $k - i$ and multiply the final result by 2.
4.  **Greedy Break:** For fixed $i$ and $j$, the very first $k$ we find ($k > j$) will always provide the smallest possible $k - i$ for that specific $i, j$ pair. Therefore, we can `break` the innermost loop early.

---

## Code

```python
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Initialize with a value larger than any possible distance
        ans = n + 1

        # Triple nested loops to find i < j < k
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                # Optimization: Only proceed to find 'k' if nums[i] and nums[j] match
                if nums[i] != nums[j]:
                    continue
                
                for k in range(j + 1, n):
                    # Check if the third element completes the triplet
                    if nums[j] == nums[k]:
                        # Update the minimum distance (k - i)
                        ans = min(ans, k - i)
                        # Greedy optimization: further k values will only increase the distance
                        break

        # Return -1 if no triplet was found, otherwise return the calculated distance
        return -1 if ans == n + 1 else ans * 2
```

---

## Example Walkthrough

**Input:** `nums = [1, 1, 2, 1, 1]`

1.  **Triplet 1:** $i=0, j=1, k=3$. $nums[0]=1, nums[1]=1, nums[3]=1$.
    - Distance: $2 \times (3 - 0) = 6$. `ans = 3`.
2.  **Triplet 2:** $i=0, j=1, k=4$. (Skipped by `break` because $k=3$ was smaller).
3.  **Triplet 3:** $i=1, j=3, k=4$. $nums[1]=1, nums[3]=1, nums[4]=1$.
    - Distance: $2 \times (4 - 1) = 6$. `ans` stays `3`.
4.  **Result:** `3 * 2 = 6`.

---

## Complexity Analysis

* **Time Complexity:** $O(N^3)$
    - In the worst case (all elements are equal), we check all possible triplets. However, the `continue` and `break` statements significantly improve the average runtime.
* **Space Complexity:** $O(1)$
    - We only use a single variable `ans` to store the minimum distance.

---

## Tags
`Array`, `Brute-Force`, `Optimization`, `Math`