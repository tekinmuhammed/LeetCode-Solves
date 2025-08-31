# 37. Sudoku Solver

**Difficulty:** Hard  
**Link:** [LeetCode 37](https://leetcode.com/problems/sudoku-solver/)

---

## Problem Description
Write a program to solve a Sudoku puzzle by filling the empty cells.  
- A valid solution must satisfy all Sudoku rules:  
  1. Each row contains digits 1–9 without repetition.  
  2. Each column contains digits 1–9 without repetition.  
  3. Each of the nine 3x3 sub-boxes contains digits 1–9 without repetition.  

The input board is partially filled, and the puzzle has exactly one solution.

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
[
  ["5","3","4","6","7","8","9","1","2"],
  ["6","7","2","1","9","5","3","4","8"],
  ["1","9","8","3","4","2","5","6","7"],
  ["8","5","9","7","6","1","4","2","3"],
  ["4","2","6","8","5","3","7","9","1"],
  ["7","1","3","9","2","4","8","5","6"],
  ["9","6","1","5","3","7","2","8","4"],
  ["2","8","7","4","1","9","6","3","5"],
  ["3","4","5","2","8","6","1","7","9"]
]
```

### Constraints

- `board.length == 9`

- `board[i].length == 9`

- `board[i][j]` is a digit `'1'-'9'` or `'.'`.

- The puzzle has only one valid solution.

### Approach
**Key Ideas:**

- Preprocess the board:

- - Store numbers already present in each row, column, and 3x3 sub-box.

- - Collect all empty cell positions.

- Use **backtracking** to fill empty cells:

- - For each empty cell, try placing numbers 1–9.

- - Skip numbers already used in the corresponding row, column, or box.

- - If valid, place the number and recurse for the next empty cell.

- - If no valid number can be placed, backtrack (undo and try another).

- Once all cells are filled, the recursion stops.

### Time and Space Complexity

- **Time Complexity:** Exponential in the worst case (`O(9^k)`, where k is the number of empty cells).

- - In practice, efficient pruning (checking row/col/box constraints) makes it fast enough.

- **Space Complexity:** `O(81)` **≈** `O(1)` → Constant space for sets and recursion depth.

### Tags

`Backtracking`, `Recursion`, `Constraint-Satisfaction`, `Matrix`

### Notes

- This is a **classic backtracking problem.**

- Pre-checking rows, columns, and boxes before recursion greatly improves efficiency.

- Although the worst-case complexity is high, the fixed Sudoku board size ensures practical solvability.