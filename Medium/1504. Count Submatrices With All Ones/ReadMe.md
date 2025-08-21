# 1504. Count Submatrices With All Ones  

**Difficulty:** Medium  
**Link:** [LeetCode 1504](https://leetcode.com/problems/count-submatrices-with-all-ones/)  

---

## Problem Description  

Given a binary matrix `mat`, return the number of submatrices that contain only `1`s.  

A submatrix is a contiguous rectangular block inside the matrix.  

---

## Example  

### Input:  
```python
mat = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
```

### Output:
```python
13
```

### Explanation:

There are 6 submatrices of size `1x1`,
3 submatrices of size `1x2`,
2 submatrices of size `2x1`,
1 submatrix of size `2x2`,
1 submatrix of size `3x1`.
Total = `13`.

### Constraints

- `1 <= rows, cols <= 150`

- `0 <= mat[i][j] <= 1`

### Approach

**Key Ideas:**

- Treat each row as the "base" of a histogram.

- Build a `height` matrix where `height[i][j]` represents the number of consecutive `1`s stacked vertically up to row `i`.

- For each row `i`, iterate through columns `j`:

- - If `height[i][j] > 0`, expand leftwards (`k = j, j-1, ...`) to count all valid rectangles ending at column `j`.

- - Maintain `min_height` while expanding left, ensuring all selected columns form a valid rectangle of ones.

- Accumulate all counts into `total`.

This converts the 2D problem into a histogram-based counting problem row by row.

### Time and Space Complexity

- **Time Complexity:** `O(rows * cols^2)` — for each cell, potentially expand left across the row.

- **Space Complexity:** `O(rows * cols)` — for storing the height matrix.

### Tags

`Dynamic-Programming`, `Matrix`, `Stack`, `Histogram`

### Notes

- The histogram-based approach is intuitive and avoids brute force checking of every submatrix.

- Time complexity can be optimized further using a **monotonic stack** to reduce leftward expansion.