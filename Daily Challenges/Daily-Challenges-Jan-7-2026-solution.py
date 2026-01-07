# 1339. Maximum Product of Splitted Binary Tree

# **Difficulty:** Medium  
# **Link:** [LeetCode 1339](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/)  

# 🧠 Problem Description
# [Github LeetCode 1339. Maximum Product of Splitted Binary Tree](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1339.%20Maximum%20Product%20of%20Splitted%20Binary%20Tree)

class Solution(object):
    def maxProduct(self, root):
        MOD = 10**9 + 7
        subtree_sums = []

        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            subtree_sums.append(s)
            return s

        total_sum = dfs(root)
        max_product = 0

        for s in subtree_sums:
            max_product = max(max_product, s * (total_sum - s))

        return max_product % MOD