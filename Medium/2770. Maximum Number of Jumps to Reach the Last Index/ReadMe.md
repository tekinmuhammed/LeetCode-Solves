# 2770. Maximum Number of Jumps to Reach the Last Index

**Difficulty:** Medium
**Problem Link:** [LeetCode 2770](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/description/)

---

## Problem 
You are given a **0-indexed** integer array `nums` of length `n` and an integer `target`.

You are initially positioned at index `0`. In one step, you can jump from index `i` to any index `j` such that:
* `0 <= i < j < n`
* `-target <= nums[j] - nums[i] <= target`

Return the **maximum number of jumps** you can make to reach index `n - 1`. 
If there is no way to reach index `n - 1`, return `-1`.

---

# Approach 

This problem asks for the *maximum* path length in a Directed Acyclic Graph (DAG) where edges are determined by the `target` constraint. To solve this efficiently without recalculating the same paths, we can use **Dynamic Programming** via a **Memoized Depth-First Search (DFS)**.

Steps:

1. **State Definition:** Let `dfs(i)` be the maximum number of jumps required to reach the last index (`n - 1`) starting from index `i`.
2. **Base Case:** If `i == len(nums) - 1`, we are already at the target index. The number of jumps needed from here is `0`.
3. **Recursive Step:** 
   * We initialize the result for the current index to negative infinity (`-inf`). This acts as a flag indicating that reaching the end might be impossible from this node.
   * We iterate through all possible next jump destinations `j` where `j > i`.
   * We check the jump condition: `abs(nums[i] - nums[j]) <= target`.
   * If valid, we take the jump and add `1` to the result of the recursive call `dfs(j)`. We keep track of the maximum jumps among all valid choices.
4. **Memoization (`@cache`):** Python's built-in `@cache` decorator saves the results of `dfs(i)`. If we visit the same index again from a different path, it returns the cached result in O(1) time, avoiding redundant calculations.
5. **Final Check:** We call `dfs(0)`. If the result is less than 0, it means no valid path reached the end, so we return `-1`. Otherwise, we return the calculated maximum jumps. 

---

# Example Walkthrough 

Consider:   
`nums = [1, 3, 6, 4, 1, 2]`
`target = 2`

* **Start at index 0 (`nums[0] = 1`)**: 
  * Can we jump to index 1 (`nums[1] = 3`)? `|1 - 3| = 2 <= 2`. **Yes**.
  * Can we jump to index 4 (`nums[4] = 1`)? `|1 - 1| = 0 <= 2`. **Yes**.
  * Can we jump to index 5 (`nums[5] = 2`)? `|1 - 2| = 1 <= 2`. **Yes**.

* The DFS explores all these paths: 
  * Path 1: `0 -> 1 -> 3 -> 5` (Values: 1 -> 3 -> 4 -> 2). Total jumps = 3. 
  * Path 2: `0 -> 4 -> 5` (Values: 1 -> 1 -> 2). Total jumps = 2. 
  * Path 3: `0 -> 5` (Values: 1 -> 2). Total jumps = 1. 

The recursive `max()` function bubbles up the longest successful path, which is **3 jumps**. 

---

# Complexity Analysis 

Time Complexity 

O(N^2)

Where `N` is the length of `nums`. Thanks to memoization, we compute `dfs(i)` exactly once for each of the `N` indices. Inside the function, we loop over up to `N` elements to find the next valid jump. Thus, the total time bound is $O(N^2)$.

Space Complexity 

O(N) 

The space complexity is determined by the maximum depth of the recursion stack and the memory required to store the cache, both of which take up to $O(N)$ space in the worst-case scenario.

---

# Code 

```python
from functools import cache
from typing import List
from math import inf

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i: int):
            if i == len(nums) - 1:
                return 0

            res = -inf
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) <= target:
                    res = max(res, dfs(j) + 1)
            return res

        ans = dfs(0)
        return -1 if ans < 0 else ans
```