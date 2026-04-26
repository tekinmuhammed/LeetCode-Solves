# 1559. Detect Cycles in 2D Grid 

**Difficulty:** Medium
**Problem Link:** [LeetCode 1559](https://leetcode.com/problems/detect-cycles-in-2d-grid/description/)

---

## Problem Description 

Given a 2D `grid` of characters, find if there is any **cycle** in the grid.

A cycle is defined as a path of **length 4 or more** in the grid that starts and ends at the same cell. From a given cell, you can move to any of its neighbors (up, down, left, or right) if they have the **same value** as the current cell. Also, you cannot reuse the cell that you just came from.

Return `true` if any cycle of the same value exists, otherwise return `false`.

---

## Approach: Union-Find (DSU) for Cycle Detection 

While cycle detection in grids is often handled with Depth First Search (DFS), using a **Union-Find (Disjoint Set Union)** data structure is a highly efficient and elegant alternative.

### Key Ideas: 
1.  **Linearization:** We map each 2D coordinate $(i, j)$ to a unique 1D index using the formula: $index = i \times n + j$, where $n$ is the number of columns.
2.  **Greedy Connection:** As we iterate through the grid (row by row, column by column), we only need to check two directions for each cell: **Up** (`i-1, j`) and **Left** (`i, j-1`).
3.  **Same-Character Condition:** We only attempt to "unite" two cells if they contain the same character.
4.  **Cycle Logic:** - If two adjacent cells with the same character are **not** in the same set, we `unite` them.
    - If they are **already** in the same set, it means there is another path connecting them, which implies a cycle exists.
5.  **Cycle Length Constraint:** In a grid traversal where we only look at previous neighbors (top/left), finding an existing connection automatically guarantees a cycle length of at least 4, satisfying the problem's requirement.

---

## Code 

```python
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def findset(self, x: int) -> int:
        # Path compression for efficiency
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def findAndUnite(self, x: int, y: int) -> bool:
        parentX, parentY = self.findset(x), self.findset(y)
        if parentX != parentY:
            # Union by size to keep the tree balanced
            if self.size[parentX] < self.size[parentY]:
                parentX, parentY = parentY, parentX
            self.parent[parentY] = parentX
            self.size[parentX] += self.size[parentY]
            return True
        # If parents are the same, a cycle is detected
        return False

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)
        
        for i in range(m):
            for j in range(n):
                # Check neighbor above
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    if not uf.findAndUnite(i * n + j, (i - 1) * n + j):
                        return True
                
                # Check neighbor to the left
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    if not uf.findAndUnite(i * n + j, i * n + j - 1):
                        return True
                        
        return False
```

---

## Example Walkthrough

**Input:** `grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]`

1.  The outer "a" cells will eventually be united.
2.  When the loop reaches the last "a" cell that connects the outer boundary back to the start, `findAndUnite` will return `False` because the start and end are already in the same component.
3.  The function returns `True`.

---

## Complexity Analysis

* **Time Complexity:** $O(M \times N \times \alpha(M \times N))$
    - $M \times N$ is the total number of cells.
    - $\alpha$ is the Inverse Ackermann function, which is nearly constant $O(1)$ for all practical inputs due to path compression and union by size.
* **Space Complexity:** $O(M \times N)$
    - To store the `parent` and `size` arrays in the Union-Find structure.

---

## Tags
`Union-Find`, `Graph`, `Matrix`, `Cycle-Detection`, `Depth-First-Search`