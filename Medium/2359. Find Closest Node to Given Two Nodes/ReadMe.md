# 🔍 LeetCode 2359 - Find Closest Node to Given Two Nodes

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2359](https://leetcode.com/problems/find-closest-node-to-given-two-nodes)

---

## 📘 Problem Description

You are given a **directed graph** represented by an integer array `edges`, where:
- `edges[i]` is the node that node `i` points to (or `-1` if `i` has no outgoing edge).

You are also given two nodes: `node1` and `node2`.

Return the **index of the node** that is reachable from both `node1` and `node2`, such that the **maximum** of the distances from `node1` and `node2` to that node is **minimized**.

If there are multiple such nodes, return the **node with the smallest index**. If no such node exists, return `-1`.

---

## ✅ Example

```python
Input:
edges = [2,2,3,-1], node1 = 0, node2 = 1

Output:
2

Explanation:
- From node 0, path is: 0 → 2 → 3
- From node 1, path is: 1 → 2 → 3
- Node 2 is reachable from both and has the smallest maximum distance (1 from both).
```

### 💡 Approach

- Define a helper function `get_distances(start)` to calculate distance from a given node to all other nodes using traversal.

- Get distances from `node1` and `node2` to all other nodes.

- Iterate over all nodes and find the node that:

- - Is reachable from both `node1` and `node2`

- - Has the **smallest maximum** distance from both nodes

- - If tie, choose the one with **smaller index**

### ⏱️ Complexity

- **Time Complexity:** `O(n)` – Each traversal from node1 and node2 is linear.

- **Space Complexity:** `O(n)` – For storing distances and visited arrays.

### 🏷️ Tags

`graph`, `dfs`, `bfs`, `greedy`, `distance`