# 🎨 LeetCode 1857 - Largest Color Value in a Directed Graph

# **Difficulty:** Hard  
# **Problem Link:** [LeetCode 1857](https://leetcode.com/problems/largest-color-value-in-a-directed-graph)

# 🧠 Problem Description 
# [Github LeetCode 1857 - Largest Color Value in a Directed Graph](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/1857.%20Largest%20Color%20Value%20in%20a%20Directed%20Graph)

class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict, deque

        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        color_count = [[0] * 26 for _ in range(n)]
        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                color_index = ord(colors[i]) - ord('a')
                color_count[i][color_index] = 1
        
        visited = 0
        max_color_value = 0

        while q:
            u = q.popleft()
            visited+= 1
            max_color_value = max(max_color_value, max(color_count[u]))
            for v in graph[u]:
                for c in range(26):
                    color_count[v][c] = max(
                        color_count[v][c],
                        color_count[u][c] + (1 if ord(colors[v]) - ord('a') == c else 0)
                    )
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        
        return max_color_value if visited == n else -1