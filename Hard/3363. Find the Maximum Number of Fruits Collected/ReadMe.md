# LeetCode 3363 - Find the Maximum Number of Fruits Collected

## 📝 Problem Description

You are given a square `n x n` matrix `fruits`, where `fruits[i][j]` represents the number of fruits you can collect from row `i` and column `j`.

You must collect fruits in **three parts**:

1. Take all fruits along the **main diagonal** (i.e., `fruits[0][0]`, `fruits[1][1]`, ..., `fruits[n-1][n-1]`).
2. Then, collect fruits by choosing a path from **top to bottom** that avoids the diagonal. In each row, you may move to the **same**, **left**, or **right** column.
3. After that, **transpose** the matrix and perform the same top-down traversal again.

Return the **maximum total number of fruits** that can be collected.

---

## 💡 Example

### Input
```python
fruits = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

### Output
```python
Diagonal = 1 + 5 + 9 = 15  
+ max non-diagonal top-down path (original)  
+ max non-diagonal top-down path (transposed)
= total maximum fruits
```

### 📊 Complexity

- **Time Complexity:** `O(n^2)`

- - Each dynamic programming pass and matrix transpose takes quadratic time.

- **Space Complexity:** `O(n)`

- - Only uses two 1D arrays for state tracking in DP.

### ✅ Key Points

- Collect main diagonal values first.

- Apply top-down DP twice: once on the original matrix, once on the transposed version.

- In each DP step, allow movements to adjacent columns only (same, left, right).

- Avoid overlapping with the diagonal collection.