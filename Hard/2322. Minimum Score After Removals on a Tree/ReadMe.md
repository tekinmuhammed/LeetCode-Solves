# 2322. Minimum Score After Removals on a Tree

**Difficulty:** Hard  
**Problem Link:** [LeetCode 2322](https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/)

---

## Problem Description

You are given a tree (an undirected, connected graph with no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and a 0-indexed integer array `nums` of length `n` where `nums[i]` represents the value of the `i-th` node. The tree is represented by a 2D array `edges`, where `edges[i] = [a, b]` denotes an edge between nodes `a` and `b`.

You are allowed to **remove two different edges** from the tree. After the removal, the tree will be split into **three connected components**.

You must choose **two edges to remove** such that the **score** of the resulting configuration is **minimized**.

The **score** of a configuration is defined as the **difference between the maximum and minimum XOR value** of the three components.

Return the **minimum possible score**.

---

### Example

**Input:**
```python
nums = [1,5,5,4,11], 
edges = [[0,1],[1,2],[1,3],[3,4]]
```

### Output:
```python
9
```

### Explanation:

You can remove edges to split the tree into three components with XOR values like: 1, 4, 12 → score = 12 - 1 = 11,
or 5, 5, 9 → score = 9 - 5 = 4 → Best possible score = **4**, etc.

### Approach

This is **a tree-based DFS problem** involving:

1. **XOR accumulation** across subtrees.

2. Two DFS traversals:

- The first DFS computes the XOR value of each subtree.

- The second DFS explores all valid combinations of two edge removals, computing the resulting XOR partitions and updating the minimum score.

### Key Observations:

- Removing two edges divides the tree into **three separate subtrees**.

- The XOR of the entire tree is fixed: `total_xor = nums[0] ^ nums[1] ^ ... ^ nums[n-1]`

- Let’s say after two cuts we obtain three components with XORs: A, B, and C. Then:
`C = total_xor ^ A ^ B`

- To minimize the score `= max(A, B, C) - min(A, B, C)`, we try all valid edge pairs using post-order DFS.

### Complexity

- **Time Complexity:** `O(n²)`
We use two nested DFS traversals to explore possible edge removals.

- **Space Complexity:** `O(n)` for recursion stack and adjacency list.

### Tags
`DFS`, `Tree`, `XOR`, `Greedy`, `Combinatorics`, `LeetCode-Hard`

### Key Insights

- XOR values are well-behaved under tree partitions.

- This problem is solved optimally by considering all valid 2-edge-cut combinations using **careful DFS traversal and greedy score minimization**.