# 1277. Count Square Submatrices with All Ones  

**Difficulty:** Medium  
**Link:** [LeetCode 1277](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)  

---

## Problem Description  

Given a `m x n` binary matrix, return the number of square submatrices with all ones.  

A square submatrix is defined as a contiguous block within the matrix where both the width and height are equal, and every element inside the block is `1`.  

---

## Example  

### Input:  
```python
matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
```

### Output:
```python
15
```

## Explanation:

- `10` squares of size `1x1`

- `4` squares of size `2x2`

- `1` square of size `3x3`
Total = `15`

## Constraints

- `1 <= m, n <= 300`

- `0 <= matrix[i][j] <= 1`

## Approach

**Key Ideas:**

- **Use Dynamic Programming (DP)** to count the maximum size of a square submatrix ending at each cell `(i, j)`.

- If `matrix[i][j] == 1`, then the largest square ending at `(i, j)` is:

```python
1 + min(top, left, top-left)
```

where:

- - `top = dp[i-1][j]`

- - `left = dp[i][j-1]`

- -  `top-left = dp[i-1][j-1]`

- The sum of all `dp[i][j]` values gives the total number of square submatrices.

### Time and Space Complexity

- **Time Complexity:** `O(m * n)` — iterate through all cells once.

- **Space Complexity:** `O(m * n)` — DP matrix of the same size as input.

- - Can be optimized to `O(n)` by using a rolling array.

### Tags

`Dynamic-Programming`, `Matrix`

### Notes

- Elegant DP solution leveraging previous computations to avoid brute force.

- Space can be optimized further without affecting clarity.