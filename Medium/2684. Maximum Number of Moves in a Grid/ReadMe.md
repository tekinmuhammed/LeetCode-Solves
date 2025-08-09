# 🟦 LeetCode 2684 - Maximum Number of Moves in a Grid

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2684](https://leetcode.com/problems/maximum-number-of-moves-in-a-grid)

---

## 📘 Problem Description

You are given an `m x n` integer matrix `grid`. You can start from **any cell in the first column**, and move to the **next column** by moving:

- to the cell directly to the right
- to the upper-right cell
- to the lower-right cell

You can only move to a cell if its value is **strictly greater** than the current cell.

Return the **maximum number of moves** you can perform.

---

## 🧪 Example

### Input:
```python
grid = [
    [2,4,3,5],
    [5,4,9,3],
    [3,4,2,11],
    [10,9,13,15]
]
```

## Output:
```python
3
```

## Explanation:

One possible path is: `grid[0][0] → grid[1][1] → grid[2][2] → grid[3][3]`

## 🚀 Approach

We use Dynamic Programming from right to left. For each cell, we check if we can move to any of the 3 cells in the next column (`right`, `upper-right`, `lower-right`) and take the best move count.

**Steps:**
- Initialize a `dp` table of same size as `grid` with zeros.

- Traverse from second-last column to first.

- For each cell `(i, j)`, if a move to a neighboring cell in `(j+1)` is valid (i.e., strictly increasing), update `dp[i][j]`.

Final result is the maximum value in the first column of `dp`.

## ⏱️ Complexity

- **Time Complexity:** O(m × n)

- **Space Complexity:** O(m × n)

Where `m = number of rows`, `n = number of columns`.

### 🏷️ Tags

`dynamic-programming`, `matrix`, `dfs`, `grid-traversal`, `leetcode-medium`