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