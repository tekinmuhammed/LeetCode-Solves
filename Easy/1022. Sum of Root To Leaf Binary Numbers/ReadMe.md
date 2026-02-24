# 1022. Sum of Root To Leaf Binary Numbers

**Difficulty:** Easy
**Link:** [LeetCode 1022](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/)

---

## Problem

You are given the `root` of a binary tree where each node has a value `0` or `1`.

Each **root-to-leaf path** represents a binary number.

Return the **sum of all these binary numbers in decimal form**.

A leaf is a node with no children.

### Example

Input
```
        1
       / \
      0   1
     / \ / \
    0  1 0  1
```

Paths and values

```
100 = 4
101 = 5
110 = 6
111 = 7
```

Output

```
22
```

---

# Approach

We traverse the tree using **Depth-First Search (DFS)**.

While moving from the root to a node, we keep building the binary number.

At each step:

1. Shift the current value left by one bit.
2. Add the current node value.

This is equivalent to constructing a binary number.

Example

```
current = (current << 1) | node.val
```

If we reach a leaf node, the constructed number is complete, so we return it.

Otherwise, we continue exploring the left and right children and sum their results.

---

# Code

```python
class Solution(object):
    def sumRootToLeaf(self, root):
        def dfs(node, current):
            if not node:
                return 0

            current = (current << 1) | node.val

            if not node.left and not node.right:
                return current

            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)
```

---

# Step-by-Step Example

Tree

```
    1
   / \
  0   1
```

Start

```
current = 0
```

Visit root

```
current = (0 << 1) | 1 = 1
```

Go left

```
current = (1 << 1) | 0 = 2
```

Leaf reached → value = 2

Go right

```
current = (1 << 1) | 1 = 3
```

Leaf reached → value = 3

Final sum

```
2 + 3 = 5
```

---

# Complexity Analysis

Time Complexity

```
O(n)
```

Every node is visited once.

Space Complexity

```
O(h)
```

Where `h` is the height of the tree (recursion stack).

Worst case

```
O(n)
```

Best case (balanced tree)

```
O(log n)
```

---

# Key Insight

Instead of storing the entire path, we **build the binary number during traversal using bit operations**, which is both faster and memory-efficient.