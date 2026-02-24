# 1022. Sum of Root To Leaf Binary Numbers

# **Difficulty:** Easy
# **Link:** [LeetCode 1022](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/)

# 🧠 Problem Description
# [Github LeetCode 1022. Sum of Root To Leaf Binary Numbers](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1022.%20Sum%20of%20Root%20To%20Leaf%20Binary%20Numbers)

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