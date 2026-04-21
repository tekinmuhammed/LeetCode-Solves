# 1722. Minimize Hamming Distance After Swap Operations

**Difficulty:** Medium
**Problem Link:** [LeetCode 1722](https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/)

---

## Problem Description

You are given two integer arrays, `source` and `target`, both of length `n`. You are also given an array `allowedSwaps` where `allowedSwaps[i] = [ai, bi]` indicates that you can swap the elements at indices `ai` and `bi` in the `source` array. You can perform as many swap operations as you want in any order.

The **Hamming distance** between two arrays of the same length is the number of positions where the elements are different.

Return the **minimum Hamming distance** between `source` and `target` after performing any number of swap operations on `source`.

---

## Approach: Disjoint Set Union (DSU) & Multiset Matching

The core idea is to recognize that swaps are **transitive**. If you can swap index $A$ with $B$, and index $B$ with $C$, you can effectively move the element at index $A$ to index $C$ or arrange the elements $\{A, B, C\}$ in any permutation.

### Key Ideas:
1.  **Component Grouping:** Use a **Union-Find (DSU)** data structure to group indices that are connected through `allowedSwaps`. Any indices in the same connected component can have their values rearranged arbitrarily.
2.  **Multiset Representation:** For each connected component, the pool of values available in `source` can be compared against the values required by `target` at those same indices.
3.  **Greedy Matching:** - For each component, count the frequency of each number in `source`.
    - Iterate through the same indices in `target`. If the required number exists in the component's `source` pool, "use" it (decrement count).
    - If it doesn't exist, it contributes to the Hamming distance.
4.  **Minimization:** By matching as many elements as possible within each component, we minimize the total Hamming distance.



---

## Code

```python
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.fa = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        # Union by rank to keep the tree flat
        if self.rank[rootX] < self.rank[rootY]:
            rootX, rootY = rootY, rootX
        self.fa[rootY] = rootX
        if self.rank[rootX] == self.rank[rootY]:
            self.rank[rootX] += 1

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        n = len(source)
        uf = UnionFind(n)
        
        # Step 1: Build connected components of indices
        for a, b in allowedSwaps:
            uf.union(a, b)

        # Step 2: Group source values by their component root
        # sets[root] = {value: count}
        sets = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            root = uf.find(i)
            sets[root][source[i]] += 1

        # Step 3: Calculate minimum Hamming distance
        ans = 0
        for i in range(n):
            root = uf.find(i)
            target_val = target[i]
            
            # Check if the required target value is available in the component's pool
            if sets[root][target_val] > 0:
                sets[root][target_val] -= 1
            else:
                # If not available, this index must contribute to the distance
                ans += 1
                
        return ans
```

---

## Complexity Analysis

* **Time Complexity:** $O(N + S \cdot \alpha(N))$
    - $N$ is the length of the arrays, $S$ is the number of allowed swaps.
    - $\alpha$ is the inverse Ackermann function (nearly constant), resulting from DSU operations.
    - Building the frequency maps and the final pass both take $O(N)$.
* **Space Complexity:** $O(N)$
    - To store the DSU structure (`fa` and `rank` arrays) and the frequency dictionaries for each component.

---

## Tags
`Union-Find`, `Hash-Table`, `Greedy`, `Graph`, `Permutation`