from collections import defaultdict

class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        visited = set()
        self.components = 0
        def dfs(node):
            visited.add(node)
            total_sum = values[node]
            for neighbor in tree[node]:
                if neighbor not in visited:
                    subtree_sum = dfs(neighbor)
                    if subtree_sum % k == 0:
                        self.components += 1
                    else:
                        total_sum += subtree_sum
            return total_sum
        total_tree_sum = dfs(0)
        if total_tree_sum % k == 0:
            self.components += 1
        return self.components