# 3629. Minimum Jumps to Reach End via Prime Teleportation

**Difficulty:** Medium
**Problem Link:** [LeetCode 3629](https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/description/)

---

## Problem 
You are given a 0-indexed integer array `nums` of length `n`. You are initially positioned at the last index (`n - 1`) and you want to reach the first index (`0`). 

In one jump, you can move from index `i` to:
* `i - 1` (if `i > 0`)
* `i + 1` (if `i < n - 1`)
* Any index `j` such that `nums[j]` is a prime factor of `nums[i]`.

Return the **minimum number of jumps** required to reach index `0`.

---

# Approach 

The problem asks for the shortest path in an unweighted graph where edges are defined by adjacency (`i-1`, `i+1`) and number theory (prime factors). The best algorithm for the shortest path in an unweighted graph is **Breadth-First Search (BFS)**.

To solve this efficiently, we must handle the prime factorization quickly and avoid traversing the same graph edges multiple times (which would cause a Time Limit Exceeded - TLE error).

Steps:

1. **Global Precomputation (Sieve of Eratosthenes):**  
   * Since the maximum value in `nums` can be large (up to $10^6$), calculating prime factors on the fly for each element is too slow. 
   * We use a modified Sieve of Eratosthenes globally to precompute the distinct prime factors for every number up to $10^6$. This runs once and serves all test cases efficiently.
2. **Build Teleportation Edges:** 
   * We iterate through the array `nums` and build a map (`edges`). 
   * If an element is a prime number (identified by having exactly 1 unique prime factor), we map this prime number to its index `i`.
3. **Breadth-First Search (BFS):** 
   * We initialize a queue starting from the target index `n - 1`.
   * For the current index `i`, we can move to its adjacent neighbors `i - 1` and `i + 1`.
   * For teleportation, we look at all prime factors of `nums[i]`. We can jump to any index `j` where `nums[j]` is exactly that prime factor.
4. **Optimization (Crucial Step):** 
   * After we use a prime factor `p` to teleport, we **clear** its list of indices (`edges[p].clear()`). This ensures that we don't redundantly process the same prime factor from different nodes, keeping our time complexity linear relative to the number of edges.

---

# Example Walkthrough 

Consider a simplified array:
`nums = [2, 4, 8, 3, 6]`

1. **Precomputation & Edges:** 
   * `nums[0] = 2` (Prime) -> `edges[2] = [0]`
   * `nums[3] = 3` (Prime) -> `edges[3] = [3]`

2. **BFS Initialization:** 
   * Start at index `4` (`nums[4] = 6`). Jump count = `0`.
   
3. **First BFS Level:** 
   * From index `4`, adjacent moves: index `3` (added to queue).
   * Prime factors of `6` are `2` and `3`. 
   * Teleport using prime `2`: `edges[2]` gives index `0` (added to queue).
   * Teleport using prime `3`: `edges[3]` gives index `3` (already seen/added).
   * Clear `edges[2]` and `edges[3]`.
   
4. **Second BFS Level:** 
   * Queue contains `[3, 0]`.
   * We pop `3`.
   * We pop `0` -> Target reached! 
   * Return Jump count + 1 = `1`.

The minimum jumps to go from the end (index 4) to the start (index 0) is **1** (by teleporting via shared prime factor `2`).

---

# Complexity Analysis 

Time Complexity

O(N + M \log \log M)

Where `N` is the length of `nums` and `M` is the maximum possible value in `nums` ($10^6$). The global sieve takes $O(M \log \log M)$. The BFS runs in $O(N)$ time because each index is added to the queue at most once, and due to `edges[p].clear()`, each teleportation group is processed at most once.

Space Complexity

O(N + M)

The `factors` array for the sieve takes $O(M)$ space. The `edges` dictionary, `seen` array, and BFS queue take $O(N)$ space in the worst case. 

---

# Code

```python
from collections import defaultdict
from typing import List

# Global Precomputation of prime factors using a Sieve 
MX = 1_000_001
factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not factors[i]:
        for j in range(i, MX, i):
            factors[j].append(i)

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        edges = defaultdict(list)
        
        # Map primes to their indices 
        for i, a in enumerate(nums):
            if len(factors[a]) == 1:
                edges[a].append(i)
                
        res = 0
        seen = [False] * n
        seen[-1] = True
        q = [n - 1]
        
        # BFS to find the shortest path 
        while True:
            q2 = []
            for i in q:
                if i == 0:
                    return res
                
                # Check adjacent index (left) 
                if i > 0 and not seen[i - 1]:
                    seen[i - 1] = True
                    q2.append(i - 1)
                    
                # Check adjacent index (right) 
                if i < n - 1 and not seen[i + 1]:
                    seen[i + 1] = True
                    q2.append(i + 1)
                    
                # Check teleportation via prime factors 
                for p in factors[nums[i]]:
                    for j in edges[p]:
                        if not seen[j]:
                            seen[j] = True
                            q2.append(j)
                    # Clear the edges to prevent redundant processing (O(N) guarantee) 
                    edges[p].clear()
                    
            q = q2
            res += 1
```