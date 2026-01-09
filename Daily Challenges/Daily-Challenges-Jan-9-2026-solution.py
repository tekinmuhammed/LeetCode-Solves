# 865. Smallest Subtree with all the Deepest Nodes

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 865](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/)

# 🧠 Problem Description
# [Github LeetCode 865. Smallest Subtree with all the Deepest Nodes](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/865.%20Smallest%20Subtree%20with%20all%20the%20Deepest%20Nodes)

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        def dfs(node):
            if not node:
                return (0, None)

            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)

            if left_depth > right_depth:
                return (left_depth + 1, left_node)
            elif right_depth > left_depth:
                return (right_depth + 1, right_node)
            else:
                return (left_depth + 1, node)

        return dfs(root)[1]