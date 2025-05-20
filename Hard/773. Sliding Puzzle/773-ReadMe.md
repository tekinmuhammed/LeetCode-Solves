# 🧩 LeetCode 773 - Sliding Puzzle

**Difficulty:** Hard  
**Problem Link:** [LeetCode 773](https://leetcode.com/problems/sliding-puzzle/)

---

## 📘 Problem Description

You are given a `2x3` board with tiles numbered from `1` to `5` and one empty space represented as `0`.  
You can move the tiles **horizontally or vertically** into the empty space.  
Return the minimum number of moves to reach the target state:

1 2 3
4 5 0

If it's impossible to reach the target, return `-1`.

---

## 🧪 Example

### Input:
```python
board = [
    [1, 2, 3],
    [4, 0, 5]
]
```

## Output:
`1`

## 🚀 Approach
This is a **shortest path** problem in a state space.
We use **Breadth-First Search (BFS)** to explore all board configurations, starting from the initial one.

**Key Concepts:**
- Represent the board as a string (e.g. `"123405"`).

- At each step, find all possible states by moving `0` to its valid neighbor positions.

- Use a **queue** to explore level-by-level (BFS).

- Track visited states to avoid cycles.

## ⏱️ Complexity
- **Time Complexity:** `O(N!)` where `N = 6` (number of tiles), but in practice limited to 720 permutations.

- **Space Complexity:** `O(N!)`, for visited states.

## 🏷️ Tags
`bfs`, `graph`, `shortest-path`, `hashset`, `sliding-puzzle`, `leetcode-hard`