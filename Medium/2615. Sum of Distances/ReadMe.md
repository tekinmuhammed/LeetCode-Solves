# 2615. Sum of Distances

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2615](https://leetcode.com/problems/sum-of-distances/)

---

## Problem Description

You are given a 0-indexed integer array `nums`. There is a new array `arr` of the same length where `arr[i]` is the sum of $|i - j|$ for all $j$ such that `nums[i] == nums[j]` and $i \neq j$.

Return the array `arr`.

---

## Approach: Grouping Indices + Prefix Sum Optimization

A naive solution would be to compare every pair of indices with the same value, resulting in $O(N^2)$ time complexity, which is too slow for $N = 10^5$. Instead, we can use a hash map to group indices and apply a mathematical formula to calculate the distances in linear time.

### Key Ideas:
1.  **Grouping:** Use a hash map to store a list of all indices for each unique value in `nums`.
2.  **Mathematical Simplification:** For a sorted list of indices $[x_0, x_1, \dots, x_{sz-1}]$ belonging to the same value, the sum of distances for the $i^{th}$ index $x_i$ is:
    $$res[x_i] = \sum_{j=0}^{i-1} (x_i - x_j) + \sum_{j=i+1}^{sz-1} (x_j - x_i)$$
3.  **Prefix Sums:** We can rewrite the sum as:
    $$res[x_i] = \left( i \cdot x_i - \sum_{j=0}^{i-1} x_j \right) + \left( \sum_{j=i+1}^{sz-1} x_j - (sz - 1 - i) \cdot x_i \right)$$
    By maintaining a running prefix sum (`prefix_total`) and knowing the grand total of the indices in the group (`total`), we can compute the sum of distances for each index in $O(1)$.
4.  **Final Formula:**
    $$res[x_i] = total - 2 \cdot prefix\_total + x_i \cdot (2i - sz)$$

---

## Code

```python
from collections import defaultdict

class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        """
        :type nums: list[int]
        :rtype: list[int]
        """
        n = len(nums)
        # Step 1: Group all indices by their value
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)
            
        res = [0] * n
        
        # Step 2: Calculate the sum of distances for each group
        for group in groups.values():
            total = sum(group)
            prefix_total = 0
            sz = len(group)
            
            for i, idx in enumerate(group):
                # Apply the optimized prefix-sum distance formula
                # res[idx] = (left_sum) + (right_sum)
                res[idx] = total - prefix_total * 2 + idx * (2 * i - sz)
                
                # Update prefix_total for the next index in the group
                prefix_total += idx
                
        return res
```

---

## Example Walkthrough

**Input:** `nums = [1, 3, 1, 1, 2]`

1.  **Grouping:** `1: [0, 2, 3]`, `3: [1]`, `2: [4]`
2.  **Processing Group `1` (indices 0, 2, 3):**
    - Total = 5, sz = 3.
    - **i=0, idx=0:** $5 - 2(0) + 0(2 \cdot 0 - 3) = 5$.
    - **i=1, idx=2:** $5 - 2(0) + 2(2 \cdot 1 - 3) = 5 - 0 - 2 = 3$. (Prefix sum becomes 2)
    - **i=2, idx=3:** $5 - 2(2) + 3(2 \cdot 2 - 3) = 5 - 4 + 3 = 4$.
3.  **Groups with one element:** Distances are always 0.

**Output:** `[5, 0, 3, 4, 0]`

---

## Complexity Analysis

* **Time Complexity:** $O(N)$
    - We iterate through the array once to build the groups: $O(N)$.
    - We iterate through each group once. Since the total number of elements in all groups is $N$, the calculation takes $O(N)$.
* **Space Complexity:** $O(N)$
    - The hash map `groups` and the result array `res` both require $O(N)$ space.

---

## Tags
Array, Hash-Table, Prefix-Sum, Math, Medium-Logic