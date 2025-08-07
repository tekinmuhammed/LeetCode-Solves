# 🖌️ LeetCode 2661 - First Completely Painted Row or Column

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2661](https://leetcode.com/problems/first-completely-painted-row-or-column)

---

## 📘 Problem Description

You are given a matrix `mat` and a list `arr` which represents the painting order of numbers in `mat`.

Return the **first index** in `arr` at which either a **row or a column** in `mat` becomes **completely painted**.

---

## 🧪 Example

### Input:
```python
arr = [1,3,4,2]
mat = [[1,4],
       [2,3]]
```

### Output:
```python
2
```

### Explanation:

- Index 0 → Paint 1 → mat becomes [[x, 4], [2, 3]]

- Index 1 → Paint 3 → mat becomes [[x, 4], [2, x]]

- Index 2 → Paint 4 → mat becomes [[x, x], [2, x]]

Now row 0 is fully painted ⇒ return index `2`.

### 🧠 Approach & Intuition

1. Create a **mapping** from number to its (row, col) position in `mat`.

2. Use two counters:

- `row_count[r]` → how many cells are painted in row `r`.

- `col_count[c]` → how many cells are painted in column `c`.

3. Traverse `arr`:

- For each number, update the corresponding row and column counters.

- As soon as one row has all columns painted OR one column has all rows painted → return that index.

### ⏱️ Complexity

- **Time Complexity:** `O(m * n + len(arr))`

- **Space Complexity:** `O(m + n + m * n)`

### 🏷️ Tags

`matrix`, `hashmap`, `simulation`, `counting`

### ✅ Key Insight

By mapping numbers to their positions in the matrix and using counters, we avoid repeated scans and achieve efficient row/column tracking.