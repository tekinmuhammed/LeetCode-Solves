# 3197. Find the Minimum Area to Cover All Ones II  

**Difficulty:** Hard  
**Link:** [LeetCode 3197](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/)  

---

## Problem Description  

You are given a binary matrix `grid` (with values `0` and `1`).  

Your task is to divide the matrix into **three non-overlapping rectangles** such that:  
- All `1`s in the matrix are covered.  
- The total area of these three rectangles is minimized.  

Return the minimum possible sum of the areas of the three rectangles.  

---

## Example  

### Input:  
```python
grid = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
]
```

### Output:
```python
9
```

### Constraints

- `3 <= grid.length, grid[0].length <= 30`

- `grid[i][j]` is either `0` or `1`

- There is at least one `1` in the grid

### Approach

**Key Ideas:**

- The problem requires partitioning the matrix into **three rectangles** that cover all ones.

- For each possible partition, compute the **minimum bounding rectangle** that contains all ones inside the subgrid.

- Try different ways of dividing the matrix:

- - Horizontally into 3 parts

- - Vertically into 3 parts

- - **“L-shaped” divisions** into 3 parts

- To avoid missing vertical vs. horizontal cases, rotate the grid once and re-run the same logic.

**Helper Functions in the Code:**

- `minimumArea2(grid, u, d, l, r)`:
Finds the bounding rectangle containing all `1`s in the subgrid defined by row range `[u, d]` and column range `[l, r]`.

- If no `1` exists in the subgrid, return a large sentinel value (`sys.maxsize // 3`).

- rotate(grid)`:
Returns a rotated version of the grid (90° clockwise). This allows handling both horizontal and vertical partitions uniformly.

- `solve(grid)`:
Enumerates all possible partitions (horizontal cuts, vertical cuts, L-shapes) and computes the minimum total area.

- Finally, the algorithm runs `solve(grid)` and `solve(rotated grid)`, returning the smaller result.

### Time and Space Complexity

- **Time Complexity:** `O(n^3 * m)` in the worst case (due to nested loops checking partitions).

- **Space Complexity:** `O(n * m)` for storing rotated grids.

### Tags

`Matrix`, `Divide-and-Conquer`, `Enumeration`, `Geometry`

### Notes

- The problem is solved by **brute-forcing all possible partitions** but in a structured way (horizontal, vertical, and L-shapes).

- Using grid rotation helps avoid duplicating logic for vertical vs. horizontal cases.