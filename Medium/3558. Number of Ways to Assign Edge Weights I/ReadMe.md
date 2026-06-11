# 3558. Number of Ways to Assign Edge Weights I

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3558](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/description/)

---

## Problem
There is an undirected tree with `n` nodes labeled from `1` to `n`, rooted at node `1`. The tree is represented by a 2D integer array `edges` of length `n - 1`. 

Initially, all edges have a weight of `0`. You must assign each edge a weight of either `1` or `2`. 

Select any one node `x` at the **maximum depth**. Return the number of ways to assign edge weights in the path from node `1` to `x` such that its total cost is **odd**. Since the answer may be large, return it modulo $10^9 + 7$.

---

# Approach

At first glance, this looks like a complex path-finding and permutation problem. However, it essentially boils down to finding the maximum depth of a tree and applying a clever combinatorial math trick.

Steps:

1. **Find Maximum Depth (`k`):** * The problem only cares about the path from the root (`Node 1`) to a node at the absolute maximum depth.
   * We build an adjacency list `g` to represent the tree and use a **Depth-First Search (DFS)** starting from `1` to calculate this maximum depth. Let's call the number of edges in this longest path `k`.
2. **Combinatorial Math (The Trick):**
   * We have `k` edges on this path. Each edge can independently be assigned a weight of `1` or `2`.
   * Therefore, there are $2^k$ total possible weight combinations for this path.
   * We want the total sum of these weights to be **odd**. For a sum of 1s and 2s to be odd, there must be an *odd number of 1s*.
   * In any set of $2^k$ binary choices, exactly half of the combinations will result in an odd sum, and the other half will result in an even sum.
   * So, the number of valid ways is simply $\frac{2^k}{2} = 2^{k-1}$.
3. **Modular Exponentiation:**
   * Since `k` can be large (up to $10^5$), $2^{k-1}$ will be massive. We use Python's built-in `pow(base, exp, mod)` function to calculate $2^{k-1} \pmod{10^9 + 7}$ efficiently in $O(\log k)$ time.

---

# Example Walkthrough

Consider a tree with `n = 4` and edges `[[1, 2], [2, 3], [3, 4]]`.
The tree is a straight line: `1 -> 2 -> 3 -> 4`.

1. **DFS Traversal:**
   * Node `1` to `2` (depth 1)
   * Node `2` to `3` (depth 2)
   * Node `3` to `4` (depth 3)
   * Maximum depth `k = 3`.
2. **Path Analysis:**
   * Edges to assign: 3.
   * Possible assignments ($2^3 = 8$):
     * `[2, 2, 2]` $\rightarrow$ sum = 6 (even)
     * `[2, 2, 1]` $\rightarrow$ sum = 5 **(odd)**
     * `[2, 1, 2]` $\rightarrow$ sum = 5 **(odd)**
     * `[2, 1, 1]` $\rightarrow$ sum = 4 (even)
     * `[1, 2, 2]` $\rightarrow$ sum = 5 **(odd)**
     * `[1, 2, 1]` $\rightarrow$ sum = 4 (even)
     * `[1, 1, 2]` $\rightarrow$ sum = 4 (even)
     * `[1, 1, 1]` $\rightarrow$ sum = 3 **(odd)**
3. **Calculation:**
   * We need the odd sums. There are exactly 4 valid ways.
   * Using our formula: $2^{3-1} = 2^2 = 4$.
   * Result is `4`.

---

# Complexity Analysis

Time Complexity

O(N)

Where `N` is the number of nodes in the tree. We visit each node and edge exactly once during the DFS traversal. Calculating $2^{k-1} \pmod{10^9+7}$ takes $O(\log N)$ time, which is bounded and dominated by the linear DFS step.

Space Complexity

O(N)

We use $O(N)$ space to store the adjacency list `g` representing the tree. The DFS recursion stack will also take up to $O(N)$ space in the worst-case scenario (a highly skewed tree / linear line).

---

# Code

```python
from typing import List

class Solution:
    MOD = 10**9 + 7

    def dfs(self, g: list, x: int, f: int) -> int:
        max_dep = 0
        for y in g[x]:
            if y == f:
                continue
            max_dep = max(max_dep, self.dfs(g, y, x) + 1)
        return max_dep

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            
        max_dep = self.dfs(g, 1, 0)
        
        # Calculate 2^(max_dep - 1) modulo 10^9 + 7
        return pow(2, max_dep - 1, self.MOD)
```