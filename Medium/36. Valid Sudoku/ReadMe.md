# 36. Valid Sudoku

**Difficulty:** Medium  
**Link:** [LeetCode 36](https://leetcode.com/problems/valid-sudoku/)

---

## Problem Description
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1–9 without repetition.  
2. Each column must contain the digits 1–9 without repetition.  
3. Each of the nine 3x3 sub-boxes must contain the digits 1–9 without repetition.  

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.  
- Only the filled cells are considered.

---

## Example

### Input:
```python
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
```

### Output:
```python
True
```

### Constraints

- `board.length == 9`

- `board[i].length == 9`

- `board[i][j]` is a digit `'1'-'9'` or `'.'`.

### Approach
**Key Ideas:**

- Use three arrays of sets to track numbers in rows, columns, and 3x3 sub-boxes.

- For each cell:

- - Skip if empty (`"."`).

- - Check if the number already exists in the corresponding row, column, or box.

- - If so, return `False`.

- - Otherwise, add it to the sets.

- If no violations are found, return `True`.

### Time and Space Complexity

- **Time Complexity:** `O(1)` → The board size is fixed (81 cells).

- **Space Complexity:** `O(1)` → Only 27 sets are used (constant size).

### Tags

`Hash-Set`, `Matrix`, `Simulation`, `Sudoku-Validation`

### Notes

- This solution checks validity but **does not solve** the Sudoku.

- Using sets ensures O(1) lookups for duplicates.