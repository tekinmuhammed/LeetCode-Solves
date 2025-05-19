# 🟨 LeetCode 2257 - Count Unguarded Cells in the Grid

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2257](https://leetcode.com/problems/count-unguarded-cells-in-the-grid)

---

## 📘 Problem Description

You are given the dimensions of a grid (`m` rows and `n` columns), as well as the positions of **guards** and **walls**. A guard can see in four directions (up, down, left, right) until their view is blocked by either a wall or another guard.

You need to count and return the number of **unguarded** cells in the grid.

---

## 🧪 Example

### Input:
```python
m = 4
n = 6
guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]
```

## Output:
```python
7
```

## 🚀 Approach

- Create a 2D grid to represent the state of each cell:

- - `0`: empty

- - `1`: wall

- - `2`: guard

- - `3`: guarded (watched by a guard)

- For each guard, simulate its vision in the 4 cardinal directions until a wall or another guard blocks the view.

- Finally, count the cells that are still marked as `0`.

## ⏱️ Complexity

- **Time Complexity:** O((m + n) * G), where G is the number of guards (each guard may scan an entire row or column).

- **Space Complexity:** O(m * n)

## 🏷️ Tags
`simulation`, `grid`, `matrix`, `visibility`, `guards`, `leetcode-medium`