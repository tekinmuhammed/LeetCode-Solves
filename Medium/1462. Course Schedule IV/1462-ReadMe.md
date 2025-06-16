# 📘 LeetCode 1462 - Course Schedule IV

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1462](https://leetcode.com/problems/course-schedule-iv)

---

## 🧩 Problem Description

You're given:
- `numCourses` labeled from `0` to `numCourses - 1`
- A list of `prerequisites` where `prerequisites[i] = [a, b]` means course `a` is a **direct prerequisite** of course `b`
- A list of `queries` where each query is `[u, v]` asking if course `u` is a **prerequisite** (directly or indirectly) of course `v`.

### Task:
Return a list of booleans where each boolean answers the corresponding query.

---

## 🔍 Example

### Input:
```python
numCourses = 4
prerequisites = [[0,1],[1,2],[2,3]]
queries = [[0,3],[1,3],[3,0]]
```

### Output:
```python
[True, True, False]
```

### 🧠 Approach & Intuition

This is a **transitive closure** problem in graph theory. We are to determine if there's a path from `u` to `v` in a directed graph.

#### 🔧 Strategy:

- Use **Floyd–Warshall algorithm** to compute reachability between all pairs of nodes.

- `reachable[i][j]` will be `True` if `i` is a prerequisite of `j`.

- For each query, simply return `reachable[u][v]`.

### ⏱️ Complexity
- **Time Complexity:** `O(n³)` — due to triple nested loop for Floyd–Warshall

- **Space Complexity:** `O(n²)` — for the reachability matrix

### 🏷️ Tags
`graph`, `floyd-warshall`, `transitive-closure`, `reachability`, `prerequisite-check`

### ✅ Key Insight

By precomputing the transitive closure of the prerequisite graph using Floyd–Warshall, we can answer each query in **constant time**.