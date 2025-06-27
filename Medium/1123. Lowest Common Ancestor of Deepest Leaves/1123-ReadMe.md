# 🌳 LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1123](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves)

---

## 🧩 Problem Description

Given the `root` of a binary tree, return the **lowest common ancestor** (LCA) of its **deepest leaves**.

A **leaf** is a node with no children.  
The **depth** of a node is the number of edges from the root to the node.

---

## 💡 Intuition

- The **deepest leaves** are the ones furthest from the root.
- The **LCA** of these leaves is the **lowest** node in the tree that is an ancestor of **all deepest leaves**.
- If both left and right subtrees have leaves at the same deepest level, the current node is the LCA.
- If one side is deeper, propagate that side upward.

---

## 🚀 Approach

Use **DFS (post-order traversal)**:
1. For each node, recursively compute:
   - The **depth** of its left and right subtrees.
   - The **LCA** of the deepest leaves in each subtree.
2. Compare left and right depths:
   - If equal: return `(depth + 1, current node)`
   - If unequal: return the deeper one.

---

### 🧪 Example
```makefile
Input: root = [1,2,3,4]
Tree:
       1
      / \
     2   3
    /
   4

Deepest leaves: 4 and 3 (depth = 2)
LCA = 1

Output: TreeNode(1)
```

### 🕵️ Complexity

- **Time Complexity:** `O(n)` – We visit each node once.

- **Space Complexity:** `O(h)` – Call stack space for recursion (h = height of the tree).

### 🏷️ Tags
`binary-tree`, `DFS`, `lowest-common-ancestor`, `recursion`