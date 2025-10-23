# 3195. Find the Minimum Area to Cover All Ones I

**Difficulty:** Medium
**Link:** [LeetCode 3195](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/)  

---

## Problem Description  

You are given a `m x n` binary grid `g`.  

Return the **minimum area of a rectangle** that covers all the cells with `1`.  

The rectangle's sides must be parallel to the axes.  

---

## Example  

### Input:  
```python
g = [
  [0,1,0],
  [1,1,1],
  [0,1,0]
]
```

### Output:
```python
9
```

### Explanation:

The smallest rectangle that covers all `1`s has top-left corner `(0,0)` and bottom-right corner `(2,2)`.
Its area is `(2-0+1) * (2-0+1) = 9`.

### Constraints

- `1 <= m, n <= 100`

- `g[i][j]` is either `0` or `1`

- It is guaranteed that there is at least one `1` in the grid

### Approach

**Key Ideas:**

- The goal is to find the bounding box that encloses all `1`s.

- Compute:

- - `min_row`: first row index with at least one `1`

- - `max_row`: last row index with at least one `1`

- - `min_col`: first column index with at least one `1`

- - `max_col`: last column index with at least one `1`

- The rectangle area is:
```python
(max_row - min_row + 1) * (max_col - min_col + 1)
```

- In the given solution:

- - A helper `f` scans rows/columns forward (`q=1`) and backward (`q=-1`) to find boundaries.

- -  Transposing the matrix (`zip(*g)`) is used to reuse the same function for columns.

### Time and Space Complexity

- **Time Complexity:** `O(m * n)` — scanning rows and columns once.

-  **Space Complexity:** `O(1)` (ignoring transpose step which is `O(m*n)` but reused in place).

### Tags

`Array`, `Matrix`, `Greedy`

### Notes

-  Concise one-liner solution using Python’s `next` and `zip` for transposition.

- Can also be implemented in a more explicit style by manually scanning for min/max row and column indices.