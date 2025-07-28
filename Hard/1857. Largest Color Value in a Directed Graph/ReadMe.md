# 🎨 LeetCode 1857 - Largest Color Value in a Directed Graph

**Difficulty:** Hard  
**Problem Link:** [LeetCode 1857](https://leetcode.com/problems/largest-color-value-in-a-directed-graph)

---

## 📘 Problem Description

You are given a **directed graph** where each node has a color represented by a lowercase letter (`colors[i]`).

- The graph has `n` nodes, labeled from `0` to `n - 1`.
- Each edge is given as a pair `[u, v]` meaning a directed edge from `u` to `v`.

Your task is to **find the maximum number of occurrences** of any single color **along any path** in the graph.

Return `-1` if the graph contains a **cycle**, otherwise return the **maximum color count**.

---

## 🧠 Approach

### Key Ideas:

1. **Topological Sort (Kahn's algorithm)** is used to detect cycles and process nodes in valid order.
2. We maintain a `color_count[node][color]` table to track how many times each color appears on paths reaching `node`.
3. While processing the graph:
   - Update the `color_count` for each neighbor `v` based on the best values from current node `u`.
   - Increment the count of `colors[v]` accordingly.
4. If we are able to visit all nodes, no cycle exists. Otherwise, a cycle is detected.

---

### ⏱️ Complexity

- **Time Complexity:** `O(n + m + 26n)`

- - `n` = number of nodes, `m` = number of edges.

- - 26 = number of lowercase letters.

- **Space Complexity:** `O(n + m + 26n)`

- - Adjacency list + color table.

### ✅ Example
```python
Input:
colors = "abaca"
edges = [[0,1],[0,2],[2,3],[3,4]]

Output: 3

Explanation:
The path 0 → 2 → 3 → 4 has color sequence: "a", "a", "c", "a".
Color 'a' appears 3 times → Maximum = 3.
```

### 🔍 Cycle Detection Note

If not all nodes are visited during topological sort, the graph has a cycle, and we return `-1`.

### 🏷️ Tags

`graph`, `topological-sort`, `dp-on-graph`, `cycle-detection`, `bfs`