da# 🟧 LeetCode 3203 - Find Minimum Diameter After Merging Two Trees

**Difficulty:** Hard  
**Problem Link:** [LeetCode 3203](https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees)

---

## 📘 Problem Description

You're given the edge lists of two trees, `edges1` and `edges2`.

You can **connect any node** from the first tree to any node from the second tree using **one extra edge**.

Your goal is to **minimize the diameter** of the resulting tree after this connection.

Return the **minimum possible diameter** after merging the two trees optimally.

- The **diameter** of a tree is the number of edges on the longest path between any two nodes.

---

## 🧪 Example

### Input:
```python
edges1 = [[0,1],[1,2]]
edges2 = [[3,4]]
```

### Output:
`3`

### Explanation:

- Tree 1 has diameter = 2 (path: 0-1-2)

- Tree 2 has diameter = 1 (path: 3-4)

- If we connect node 2 (from tree 1) to node 4 (from tree 2), the resulting tree has diameter = 3 (path: 0-1-2-4-3)

### 🚀 Approach

We proceed in two main steps:

1. **Calculate the diameter of both trees independently** using two BFS traversals:

- First BFS from any node to find the farthest node `A`

- Second BFS from node `A` to find the actual diameter (farthest distance from A``)

2. **Determine the optimal way to connect the trees:**

- The optimal connection gives a new diameter:

```scss
max(d1, d2, ceil(d1 / 2) + ceil(d2 / 2) + 1)
```

- This formula connects the midpoints of each tree's diameter path.

### ⏱️ Complexity

- **Time Complexity:** `O(N)`, where N is the total number of nodes in both trees
(Each tree is traversed twice using BFS)

- **Space Complexity:** `O(N)`, for the graph and visited sets

### 🏷️ Tags
`tree`, `graph`, `bfs`, `diameter`, `hard`, `leetcode-graph`, `merge-trees`