# 1878. Get Biggest Three Rhombus Sums in a Grid

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1878](https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/description/)

---

## Problem Description

A **rhombus sum** is the sum of the elements of a rhombus shape in a grid. The rhombus must have the shape of a square rotated 45 degrees with its corners on the grid cells.

Given an $m \times n$ integer `grid`, return an array of the **three biggest distinct rhombus sums** in descending order. If there are fewer than three distinct sums, return all of them.

**Note:** The rhombus sum is only the sum of the elements on its **boundary**. A single cell is also considered a rhombus of size 0.

---

## Approach: Diagonal Prefix Sums

To efficiently calculate the sum of the four boundaries of each possible rhombus, we use a 2D prefix sum approach optimized for diagonals.

### Key Ideas:
1.  **Diagonal Prefix Sums:** We create two auxiliary matrices:
    - `sum1`: Stores prefix sums for diagonals moving from **top-left to bottom-right**.
    - `sum2`: Stores prefix sums for diagonals moving from **top-right to bottom-left**.
2.  **Rhombus Geometry:** A rhombus is defined by its top vertex $(i, j)$ and its size. For a rhombus with vertical distance $k$ between top and bottom:
    - **Top:** $(ux, uy) = (i, j)$
    - **Bottom:** $(dx, dy) = (i+k, j)$
    - **Left:** $(lx, ly) = (i+k/2, j-k/2)$
    - **Right:** $(rx, ry) = (i+k/2, j+k/2)$
3.  **$O(1)$ Calculation:** Using `sum1` and `sum2`, the sum of each of the four sides can be calculated in constant time. Since the vertices are shared between sides, we subtract the four vertex values once at the end to avoid double-counting.
4.  **Tracking Top 3:** A helper class `Answer` manages the storage of the three largest **distinct** sums using basic comparison logic.



---

## Code

```python
class Answer:
    def __init__(self):
        # Stores the top 3 unique sums
        self.ans = [0, 0, 0]

    def put(self, x: int):
        _ans = self.ans
        # Update logic to maintain descending order and uniqueness
        if x > _ans[0]:
            _ans[0], _ans[1], _ans[2] = x, _ans[0], _ans[1]
        elif x != _ans[0] and x > _ans[1]:
            _ans[1], _ans[2] = x, _ans[1]
        elif x != _ans[0] and x != _ans[1] and x > _ans[2]:
            _ans[2] = x

    def get(self) -> List[int]:
        return [num for num in self.ans if num != 0]


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        # sum1: top-left to bottom-right diagonals
        # sum2: top-right to bottom-left diagonals
        sum1 = [[0] * (n + 2) for _ in range(m + 1)]
        sum2 = [[0] * (n + 2) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum1[i][j] = sum1[i - 1][j - 1] + grid[i - 1][j - 1]
                sum2[i][j] = sum2[i - 1][j + 1] + grid[i - 1][j - 1]

        ans = Answer()
        for i in range(m):
            for j in range(n):
                # A single cell (size 0 rhombus)
                ans.put(grid[i][j])
                
                # Iterate through all possible rhombus sizes (k is the vertical length)
                for k in range(i + 2, m, 2):
                    ux, uy = i, j # Top
                    dx, dy = k, j # Bottom
                    lx, ly = (i + k) // 2, j - (k - i) // 2 # Left
                    rx, ry = (i + k) // 2, j + (k - i) // 2 # Right

                    if ly < 0 or ry >= n:
                        break

                    # Boundary sum calculation using diagonal prefix sums
                    boundary_sum = (
                        (sum2[lx + 1][ly + 1] - sum2[ux][uy + 2]) +   # Top-Left side
                        (sum1[rx + 1][ry + 1] - sum1[ux][uy]) +       # Top-Right side
                        (sum1[dx + 1][dy + 1] - sum1[lx][ly]) +       # Bottom-Left side
                        (sum2[dx + 1][dy + 1] - sum2[rx][ry + 2]) -   # Bottom-Right side
                        (grid[ux][uy] + grid[dx][dy] + grid[lx][ly] + grid[rx][ry]) # Subtract shared vertices
                    )
                    ans.put(boundary_sum)

        return ans.get()
```

---

## Example Walkthrough

**Input:** `grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]`

1.  **Diagonal Sums:** The code pre-calculates the diagonal reach for every cell.
2.  **Cell (2, 2):** Value 200. This is added as a size-0 rhombus.
3.  **Rhombus at (2,2) with k=2:** - Vertices: Top(1,2), Bottom(3,2), Left(2,1), Right(2,3).
    - Boundary sum is calculated using the segments.
4.  **Result:** The `Answer` class keeps only the top 3 unique values like `[228, 216, 211]`.

---

## Complexity Analysis

* **Time Complexity:** $O(m \cdot n \cdot \min(m, n))$
    - Pre-calculating diagonal sums: $O(m \cdot n)$.
    - Nested loops for each cell and each possible size: $O(m \cdot n \cdot \min(m, n))$.
* **Space Complexity:** $O(m \cdot n)$
    - Required to store the `sum1` and `sum2` prefix sum matrices.

---

## Tags
`Matrix`, `Prefix-Sum`, `Geometry`, `Sorting`, `Grid-Traversal`