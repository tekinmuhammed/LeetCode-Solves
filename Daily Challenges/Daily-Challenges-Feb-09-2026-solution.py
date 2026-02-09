# 1382. Balance a Binary Search Tree

# **Difficulty:** Medium  
# **Link:** [LeetCode 1382](https://leetcode.com/problems/balance-a-binary-search-tree/description/)

# 🧠 Problem Description
# [Github LeetCode 1382. Balance a Binary Search Tree](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1382.%20Balance%20a%20Binary%20Search%20Tree)

class Solution(object):
    def balanceBST(self, root):
        # Step 1: Inorder traversal to get sorted values
        values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        # Step 2: Build balanced BST from sorted array
        def build(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            node = TreeNode(values[mid])
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node

        return build(0, len(values) - 1)