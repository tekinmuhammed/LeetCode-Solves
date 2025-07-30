# 🟧 LeetCode 2872 - Maximum Number of K-Divisible Components

**Difficulty:** Hard  
**Problem Link:** [LeetCode 2872](https://leetcode.com/problems/maximum-number-of-k-divisible-components/)

---

## 📘 Problem Description

You are given:
- An integer `n` representing the number of nodes in a tree (0-indexed),
- A list of edges `edges` representing the undirected edges of the tree,
- A list `values` of integers where `values[i]` is the value of node `i`,
- An integer `k`.

Your task is to **remove some edges** from the tree such that each resulting connected component has a **sum of node values divisible by `k`**.

Return the **maximum number of such components** you can form.

---

## 🧪 Example

### Input:
```python
n = 5
edges = [[0,1],[1,2],[1,3],[3,4]]
values = [2,3,3,2,2]
k = 3
```

### Output:
`2`

### Explanation:

- After removing the edge between nodes 1 and 3, the components `[0,1,2]` and `[3,4]` have sums 8 and 4.

- Only the subtree `[0,1,2]` has a total sum divisible by 3.

- But if we remove edge [1,0] and [1,3], we get components with sums 3 (just node 1), 8 (0+2+3), and 4 (2+2), only one of which is divisible by 3.

- The optimal strategy gives 2 such divisible components.

### 🚀 Approach

We solve this using **DFS traversal** of the tree:

- Construct an adjacency list for the tree.

- Perform DFS from the root node:

- - At each node, calculate the **subtree sum**.

- - If a **subtree's sum is divisible** by `k`, we **cut it off** and increment the result counter.

- - Otherwise, the sum is passed up to the parent node.

- Finally, if the total tree sum is divisible by `k`, count the full tree as a component.

The core idea is: **divide the tree greedily wherever subtree sum is divisible by** `k`.

### ⏱️ Complexity

- **Time Complexity:** `O(n)`
One DFS traversal of the tree.

- **Space Complexity:** `O(n)`
For adjacency list and recursion stack.

### 🏷️ Tags

`tree`, `dfs`, `recursion`, `modulo`, `graph`, `leetcode-hard`