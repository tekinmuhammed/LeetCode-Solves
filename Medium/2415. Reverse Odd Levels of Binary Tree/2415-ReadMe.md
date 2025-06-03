# 🟨 LeetCode 2415 - Reverse Odd Levels of Binary Tree

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2415](https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/)

---

## 📘 Problem Description

Given the `root` of a **perfect binary tree**, reverse the values of the nodes at **each odd level** of the tree.

- A binary tree is **perfect** if all leaf nodes are on the same level, and every parent has two children.
- The **root is at level 0**.

Return the root of the modified tree.

---

## 🧪 Example

### Input:
     2
   /   \
  3     5
 / \   / \
8  13 21 34

### Output:
     2
   /   \
  5     3
 / \   / \
8 13 21 34

### Explanation:
- Level 1 values are reversed: `[3, 5]` → `[5, 3]`
- Other levels remain unchanged.

---

## 🚀 Approach

We use a **Depth-First Search (DFS)** approach:

- Since the tree is perfect, at each recursive step we can access symmetric pairs of nodes.
- If we are on an **odd level**, we swap the values of the corresponding nodes.
- We recursively continue on the children, mirroring traversal: `(left.left, right.right)` and `(left.right, right.left)`.

This technique ensures **in-place reversal** of odd levels without needing extra space for storing levels.

---

### ⏱️ Complexity

- **Time Complexity:** `O(n)`
We visit each node once.

- **Space Complexity:** `O(h)`
For recursion stack, where h is the height of the tree.

### 🏷️ Tags
`binary tree`, `tree traversal`, `depth-first search`, `leetcode-medium`, `recursion`