# 🌳 LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1123](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves)

# 🧠 Problem Description
# [Github LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves](https://github.com/tekinmuhammed/LeetCode-Solves/edit/main/Medium/1123.%20Lowest%20Common%20Ancestor%20of%20Deepest%20Leaves/ReadMe.md)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if not node:
                return (0, None)

            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            if left_depth > right_depth:
                return (left_depth + 1, left_lca)

            elif left_depth < right_depth:
                return (right_depth + 1, right_lca)

            else:
                return (left_depth + 1, node)

        return dfs(root)[1]