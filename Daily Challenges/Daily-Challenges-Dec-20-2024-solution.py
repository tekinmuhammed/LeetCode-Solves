# 🟨 LeetCode 2415 - Reverse Odd Levels of Binary Tree

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2415](https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/)

# 🧠 Problem Description 
# [Github LeetCode 2415 - Reverse Odd Levels of Binary Tree](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2415.%20Reverse%20Odd%20Levels%20of%20Binary%20Tree)

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(node1, node2, level):
            if not node1 or not node2:
                return
            if level % 2 == 1:
                node1.val, node2.val = node2.val, node1.val
            dfs(node1.left, node2.right, level + 1)
            dfs(node1.right, node2.left, level + 1)
        dfs(root.left, root.right, 1)
        return root