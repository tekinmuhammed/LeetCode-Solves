# 🟦 LeetCode 1277 - Count Square Submatrices with All Ones

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1277](https://leetcode.com/problems/count-square-submatrices-with-all-ones)

---

## 📘 Problem Description

Given a binary matrix (only 0s and 1s), count how many square submatrices have all ones.

---

## 🧪 Example

### Input:
```python
matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
```

## Output:
```python
15
```

## Explanation:

There are 15 squares with all 1s:

- 10 of size 1x1

- 4 of size 2x2

- 1 of size 3x3

## 🚀 Approach

We use dynamic programming to track the size of the largest square that ends at each cell.

- `dp[i][j]` represents the size of the largest square whose bottom-right corner is at `(i, j)`.

- If `matrix[i][j] == 1`, we calculate `dp[i][j]` as:

```python
dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
We accumulate each dp[i][j] into a counter.
```

## ⏱️ Complexity

- Time Complexity: `O(m × n)`

- Space Complexity: `O(m × n)`

Where `m` is number of rows and `n` is number of columns in the matrix.

## 🏷️ Tags

`dynamic-programming`, `matrix`, `2d-dp`, `leetcode-medium`, `python`

## 📝 Notes

- This is a classic 2D DP problem.

- You can optimize space by using a single row (space optimization), but clarity is often more important for interviews or study purposes.