# 🎲 LeetCode 909 - Snakes and Ladders

**Difficulty:** Medium  
**Problem Link:** [LeetCode 909](https://leetcode.com/problems/snakes-and-ladders)

---

## 📘 Problem Description

You are given a `n x n` integer matrix `board` where the cells contain either:
- `-1` meaning no snake or ladder, or
- a number indicating the destination of a **snake** or **ladder**.

The game starts at square 1 and ends at square `n * n`.  
You move forward according to a standard 6-faced dice (1 to 6).  
Your goal is to **reach the final square in the minimum number of moves**.

Return the **minimum number of moves** to reach the final square, or `-1` if not possible.

---

## 🎯 Example

```python
Input:
board = [
 [-1,-1,-1,-1,-1,-1],
 [-1,-1,-1,-1,-1,-1],
 [-1,-1,-1,-1,-1,-1],
 [-1,35,-1,-1,13,-1],
 [-1,-1,-1,-1,-1,-1],
 [-1,15,-1,-1,-1,-1]
]

Output: 4
```

### 💡 Approach

We model this game as a **graph traversal problem:**

- Each square is a node.

- From square `s`, you can move to `s+1` through `s+6` (like rolling a dice).

- - If you land on a square with a **ladder or snake**, you teleport to its destination.

We use **Breadth-First Search (BFS)** to find the **minimum number of moves**.

### 🧠 Helper Logic

- `intToPos(square)` maps a square number (1-based) to a `(row, col)` on the board, taking into account that:

- - Rows alternate between left-to-right and right-to-left direction.

### ⏱️ Complexity

- **Time Complexity:** `O(n^2)` — we visit each square at most once.

- **Space Complexity:** `O(n^2)` — for the queue and visited set.

### 🏷️ Tags

`bfs`, `graph`, `matrix`, `simulation`, `traversal`