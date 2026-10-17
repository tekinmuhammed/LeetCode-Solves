# 3551. Minimum Swaps to Sort by Digit Sum

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3551](https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/description/)

---

## Problem
You are given an integer array `nums`. You can swap any two elements of the array any number of times.

You need to sort the array based on a custom sorting key:
1. Primary key: The **sum of the digits** of each number in ascending order.
2. Secondary key (tie-breaker): The **actual value** of the number itself in ascending order.

Return the **minimum number of swaps** required to sort the array according to these rules.

Example:

Input  
nums = [14, 12, 11]  

Output  
1  

Explanation  
- Digit sums:
  - `14` $\rightarrow$ $1 + 4 = 5$
  - `12` $\rightarrow$ $1 + 2 = 3$
  - `11` $\rightarrow$ $1 + 1 = 2$
- Sorted order by digit sum (and value): `[11, 12, 14]`
- Original array: `[14, 12, 11]`
- Swapping index 0 (`14`) and index 2 (`11`) gives `[11, 12, 14]`, which is sorted. Total swaps = 1.

---

# Approach

Finding the minimum number of swaps to sort an array is a classic graph theory problem equivalent to finding the **number of cycles in a permutation graph**. 

For any permutation, if the elements are partitioned into $C$ independent cycles, the minimum number of swaps required to sort them is always **$N - C$**, where $N$ is the length of the array.

Steps:
1. **Digit Sum Calculation**: Compute the sum of digits for every element in `nums` and store them in a parallel array `digitSum`.
2. **Determine Target Positions**: 
   * Create an array of indices `[0, 1, ..., n-1]`.
   * Sort these indices using a custom key: primary key is `digitSum[i]`, and the secondary tie-breaker is `nums[i]`.
   * The sorted indices tell us the **target position** each element should move to. We map this into a `targetPos` array where `targetPos[idx] = pos`.
3. **Cycle Decomposition**: 
   * Use a `visited` boolean array to track which elements have been processed.
   * Iterate through each index from `0` to `n-1`. If an index has not been visited, it marks the start of a new permutation cycle.
   * Follow the chain of `targetPos` links until we loop back to the start, marking all elements in the cycle as visited and incrementing our cycle count.
4. **Calculate Swaps**: Return `n - cycles`.

---

# Code

```python
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        digitSum = [0] * n
        
        # Step 1: Compute digit sum for each number
        for i, v in enumerate(nums):
            s = 0
            while v > 0:
                s += v % 10
                v //= 10
            digitSum[i] = s

        # Step 2: Determine target positions after sorting by custom key
        indices = list(range(n))
        indices.sort(key=lambda i: (digitSum[i], nums[i]))

        targetPos = [0] * n
        for pos, idx in enumerate(indices):
            targetPos[idx] = pos

        # Step 3: Count cycles in the permutation graph
        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = targetPos[j]

        # Step 4: Minimum swaps = N - cycles
        return n - cycles