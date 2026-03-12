# 3600. Maximize Spanning Tree Stability with Upgrades

**Difficulty:** Hard  
**Problem Link:** [LeetCode 3600](https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/)

---

## Problem Description

You are given a graph with $n$ nodes and a list of `edges`. Each edge has:
- `u, v`: The nodes it connects.
- `s`: The stability value of the edge.
- `must`: A boolean flag. If `1`, this edge **must** be included in the spanning tree.

You are also given an integer `k`, representing the number of "upgrades" you can perform. An upgrade doubles the stability of a single edge ($s \times 2$). 

Your goal is to find a spanning tree such that all "must" edges are included, and the **minimum stability** among all edges in the tree is **maximized**.

---

## Approach

This is a classic "maximize the minimum" problem, which strongly suggests **Binary Search on the Answer**.

### Key Ideas:
1.  **Mandatory Connectivity:** First, we must process all `mustEdges`. If they form a cycle or exceed $n-1$ edges, a valid tree is impossible. These edges define our starting components.
2.  **Binary Search:** We search for the maximum possible minimum stability `mid`. 
    - For a fixed `mid`, we check if we can complete the spanning tree such that every edge has a stability $\ge mid$.
3.  **Greedy Selection:** To satisfy the condition for a specific `mid`:
    - We sort `optionalEdges` by stability in descending order.
    - For each edge, if its stability $s \ge mid$, we use it.
    - If $s < mid$ but $s \times 2 \ge mid$, we can use one of our $k$ upgrades to make it valid.
4.  **DSU (Disjoint Set Union):** We use DSU to efficiently manage connected components and ensure we don't form cycles while adding edges to reach the required $n-1$ edges.



---

## Code

```python
class DSU:
    def __init__(self, parent):
        self.parent = parent

    def find(self, x):
        if self.parent[x] == x:
            return x
        # Path compression
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def join(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[px] = py
            return True
        return False

MAX_STABILITY = 200000

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        ans = -1

        # A spanning tree needs exactly n-1 edges
        if len(edges) < n - 1:
            return -1

        mustEdges = [e for e in edges if e[3] == 1]
        optionalEdges = [e for e in edges if e[3] != 1]

        if len(mustEdges) > n - 1:
            return -1

        # Sort optional edges descending to pick the best ones first
        optionalEdges.sort(key=lambda x: x[2], reverse=True)

        selectedInit = 0
        mustMinStability = MAX_STABILITY
        dsuInit = DSU(list(range(n)))

        # Process mandatory edges
        for u, v, s, must in mustEdges:
            if not dsuInit.join(u, v):
                return -1 # Cycle detected in mandatory edges
            selectedInit += 1
            mustMinStability = min(mustMinStability, s)

        # Binary Search for the maximum possible minimum stability
        l, r = 0, mustMinStability
        while l <= r:
            mid = l + ((r - l + 1) >> 1)
            if mid == 0: # Minimum possible stability
                ans = max(ans, 0)
                l = 1
                continue
                
            dsu = DSU(dsuInit.parent[:])
            selected = selectedInit
            doubledCount = 0

            for u, v, s, must in optionalEdges:
                if selected == n - 1: break
                if dsu.find(u) == dsu.find(v): continue

                if s >= mid:
                    dsu.join(u, v)
                    selected += 1
                elif doubledCount < k and s * 2 >= mid:
                    doubledCount += 1
                    dsu.join(u, v)
                    selected += 1
            
            if selected == n - 1:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans
```

---

## Example Walkthrough

**Input:** $n=3, k=1$, Edges: `[[0,1,5,1], [1,2,3,0], [0,2,2,0]]`

1.  **Mandatory:** Edge `(0,1)` with stability 5 is fixed. `mustMinStability = 5`.
2.  **Binary Search `mid = 4`:**
    - Edge `(1,2)` stability 3. $3 < 4$ but $3 \times 2 = 6 \ge 4$. Use 1 upgrade.
    - Tree complete! `mid = 4` is possible.
3.  **Binary Search `mid = 6`:**
    - Edge `(1,2)` stability 3. $3 \times 2 = 6 \ge 6$. Possible.
    - Edge `(0,1)` is 5. Wait, $5 < 6$. Since it's a "must" edge and we didn't upgrade it, the minimum stability of the tree is 5.
4.  **Final Result:** The algorithm will converge on the optimal value constrained by the weakest link in the mandatory edges or the best available upgraded optional edges.

---

## Complexity Analysis

* **Time Complexity:** $O(E \log E + \log(S) \cdot E \cdot \alpha(n))$
    - $E \log E$ for sorting the edges.
    - $\log(S)$ for binary search (where $S$ is max stability).
    - Inside binary search, we iterate over edges ($E$) and perform DSU operations ($\alpha(n)$ is the inverse Ackermann function).
* **Space Complexity:** $O(n + E)$
    - To store the DSU structure and separate edge lists.

---

## Tags
Binary-Search, Greedy, DSU, MST, Graph-Theory, Spanning-Tree