# 110. Balanced Binary Tree

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 110](https://leetcode.com/problems/balanced-binary-tree/description/)

# 🧠 Problem Description
# [Github LeetCode 110. Balanced Binary Tree](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/110.%20Balanced%20Binary%20Tree)

class Solution(object):
    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            if left == -1:
                return -1

            right = height(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return height(root) != -1