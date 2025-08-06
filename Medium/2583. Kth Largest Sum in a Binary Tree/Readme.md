# 2583. Kth Largest Sum in a Binary Tree Level

This solution constructs a binary tree using level-order insertion and computes the sum of node values at each level. It then returns the `k`th largest among these level sums.

## 🧠 Algorithm

1. Build the binary tree from a list using BFS.
2. Traverse the tree level by level and calculate the sum of values at each level.
3. Sort the list of level sums in descending order.
4. Return the `k`th largest sum, or -1 if `k` exceeds the number of levels.

## 📌 Input
```python
root_values = [5, 8, 9, 2, 1, 3, 7, 4, 6]
k = 2
```
## ✅ Output
```python
13
```

 ---

## 📚 Dependencies

`from collections import deque`

---

## 🧪 Complexity

**Time:** O(n log n), where n is the number of nodes (due to sorting level sums)

**Space:** O(n) for storing the tree and the level sums