# 🛣️ LeetCode 3243 - Shortest Distance After Road Addition Queries I

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3243](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i)

---

## 📘 Problem Description

You are given a linear road with `n` nodes (from `0` to `n - 1`), where initially every node `i` is connected to `i + 1` with an edge of weight 1.

You receive a list of `queries`, where each query `[u, v]` adds a new **directed edge** from node `u` to node `v` with a weight of 1.

After each query, return the **shortest distance** from node `0` to node `n - 1`.

---

## 🧪 Example

### Input:
```python
n = 5
queries = [[0, 2], [2, 4], [1, 3]]
```

## Output:
```python
[3, 2, 2]
```

## 🚀 Approach
We simulate each query one-by-one:

- Initialize the graph as a path: `0 -> 1 -> 2 -> ... -> n-1` with edge weight 1.

- For every query `[u, v]`, add a directed edge `u → v` with weight 1.

- After each addition, use Dijkstra's algorithm to compute the shortest path from node `0` to node `n - 1`.

> Although this solution recalculates Dijkstra from scratch after each query, it's acceptable given the problem constraints for Part I.

## ⏱️ Complexity

- **Time Complexity (per query):** O(E log N), where E is the number of edges at that point (could grow linearly with number of queries)

- **Space Complexity:** O(N + Q), where Q is the number of queries and N is the number of nodes

## 🏷️ Tags

`dijkstra`, `shortest-path`, `graph`, `heapq`, `bfs`, `leetcode-medium`