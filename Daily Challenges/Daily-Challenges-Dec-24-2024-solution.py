# 🟧 LeetCode 3203 - Find Minimum Diameter After Merging Two Trees

# **Difficulty:** Hard  
# **Problem Link:** [LeetCode 3203](https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees)

# 🧠 Problem Description 
# [Github LeetCode 3203 - Find Minimum Diameter After Merging Two Trees](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/3203.%20Find%20Minimum%20Diameter%20After%20Merging%20Two%20Trees)

from collections import defaultdict
from math import ceil

class Solution(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: int
        """
        def tree_diameter(edges):
            if not edges:
                return 0
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            def bfs(start):
                visited = set()
                queue = deque([(start, 0)])
                visited.add(start)
                farthest_node, max_distence = start, 0
                while queue:
                    node, distence = queue.popleft()
                    if distence > max_distence:
                        max_distence = distence
                        farthest_node = node
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append((neighbor, distence + 1))
                return farthest_node, max_distence
            first_node = next(iter(graph))
            farthest_node, _ = bfs(first_node)
            _, diameter = bfs(farthest_node)
            return diameter
        diameter1 = tree_diameter(edges1)
        diameter2 = tree_diameter(edges2)
        return max(diameter1, diameter2, (diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1)