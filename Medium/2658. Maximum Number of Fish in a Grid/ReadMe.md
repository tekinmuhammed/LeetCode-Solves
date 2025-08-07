# 🐟 LeetCode 2658 - Maximum Number of Fish in a Grid

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2658](https://leetcode.com/problems/maximum-number-of-fish-in-a-grid)

---

## 🧩 Problem Description

You are given a grid where each cell contains a non-negative integer representing the number of fish at that location.

You can start from any non-zero cell and move in four directions (up, down, left, right) to collect fish. Once you move from a cell, it becomes **0** (visited), and you cannot revisit it.

### Task:

Find the **maximum number of fish** you can collect starting from any cell.

---

## 🔍 Example

### Input:
```python
grid = [
  [0, 2, 1],
  [4, 0, 0],
  [1, 0, 3]
]
```

### Output:
```python
7
```

### Explanation:

Start from (1, 0) → collect 4 → move to (2, 0) → collect 1 → move to (0, 1) → collect 2 → move to (0, 2) → collect 1 → total = 4+1+2+1 = 8
However, since these aren't all connected, the best connected component gives 7 fish.

### 🧠 Approach & Intuition

We treat each **connected component** of non-zero cells as a fishing zone and compute how many fish we can collect using **DFS (Depth-First Search)**.

#### 🔧 Strategy:

- Traverse each cell of the grid.

- If the cell has fish (`> 0`), launch DFS to explore all connected cells.

- Track the total fish collected for that component and update the global maximum.

### ⏱️ Complexity

- **Time Complexity:** `O(m × n)`
Each cell is visited at most once.

- **Space Complexity:** `O(m × n)`
Due to recursion stack in worst-case DFS.

### 🏷️ Tags

`DFS`, `Grid`, `Connected-Components`, `Backtracking`, `Flood-Fill`

### ✅ Key Insight

The key to this problem is recognizing it as a connected component exploration task, where DFS (or BFS) can find the sum of values in each region.