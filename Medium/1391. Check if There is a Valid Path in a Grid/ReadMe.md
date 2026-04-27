# 1391. Check if There is a Valid Path in a Grid

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1391](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/)

---

## Problem Description

You are given an `m x n` grid. Each cell in the grid represents a street. There are 6 types of streets:
- **1:** Left and Right connection.
- **2:** Upper and Lower connection.
- **3:** Left and Lower connection.
- **4:** Right and Lower connection.
- **5:** Left and Upper connection.
- **6:** Right and Upper connection.

You start at the cell `(0, 0)` and want to reach the cell `(m - 1, n - 1)`. You can move between two adjacent cells if and only if there is a street connecting them.

Return `true` if there is a valid path from the top-left to the bottom-right cell, otherwise return `false`.



---

## Approach: Disjoint Set Union (DSU)

The problem can be viewed as a connectivity problem in a graph. Each cell is a node, and two cells are connected by an edge if their street types allow them to connect.

### Key Ideas:
1.  **Directional Matching:** A connection is only valid if *both* cells agree. For example, if cell A is type 1 (Left-Right) and cell B is to its right, they can only connect if cell B also has a left-facing connection (type 1, 4, or 6).
2.  **Disjoint Set Union (DSU):** We initialize a DSU structure where each cell is its own component. We then iterate through each cell and "merge" it with its neighbors if a valid connection exists.
3.  **Linearization:** We convert 2D coordinates `(x, y)` to a 1D ID `x * n + y` for the DSU.
4.  **Final Check:** After processing all possible connections, if the component containing `(0, 0)` is the same as the one containing `(m - 1, n - 1)`, a path exists.

---

## Code

```python
class Solution:
    class DisjointSet:
        def __init__(self, n):
            # f[i] stores the parent of element i
            self.f = list(range(n))

        def find(self, x):
            # Path compression for efficiency
            if x == self.f[x]:
                return x
            self.f[x] = self.find(self.f[x])
            return self.f[x]

        def merge(self, x, y):
            # Union operation to connect two components
            rootX = self.find(x)
            rootY = self.find(y)
            if rootX != rootY:
                self.f[rootX] = rootY

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        ds = Solution.DisjointSet(m * n)

        def getId(x, y):
            return x * n + y

        # Helper functions to detect if neighbors can connect to the current cell
        def detectL(x, y):
            if y - 1 >= 0 and grid[x][y - 1] in [1, 4, 6]:
                ds.merge(getId(x, y), getId(x, y - 1))

        def detectR(x, y):
            if y + 1 < n and grid[x][y + 1] in [1, 3, 5]:
                ds.merge(getId(x, y), getId(x, y + 1))

        def detectU(x, y):
            if x - 1 >= 0 and grid[x - 1][y] in [2, 3, 4]:
                ds.merge(getId(x, y), getId(x - 1, y))

        def detectD(x, y):
            if x + 1 < m and grid[x + 1][y] in [2, 5, 6]:
                ds.merge(getId(x, y), getId(x + 1, y))

        # Check neighbors based on the current cell's pipe type
        def handler(x, y):
            t = grid[x][y]
            if t == 1:
                detectL(x, y); detectR(x, y)
            elif t == 2:
                detectU(x, y); detectD(x, y)
            elif t == 3:
                detectL(x, y); detectD(x, y)
            elif t == 4:
                detectR(x, y); detectD(x, y)
            elif t == 5:
                detectL(x, y); detectU(x, y)
            elif t == 6:
                detectR(x, y); detectU(x, y)

        for i in range(m):
            for j in range(n):
                handler(i, j)

        # Check if start and end are in the same component
        return ds.find(getId(0, 0)) == ds.find(getId(m - 1, n - 1))
```

---

## Complexity Analysis

* **Time Complexity:** $O(M \times N \times \alpha(M \times N))$
    - We traverse each cell once ($M \times N$).
    - Each DSU operation (find/merge) takes nearly constant time $O(\alpha(M \times N))$ where $\alpha$ is the Inverse Ackermann function.
* **Space Complexity:** $O(M \times N)$
    - To store the parent array `f` in the Disjoint Set structure.

---

## Tags
Union-Find, Graph, Matrix, Breadth-First-Search, Depth-First-Search