# 🛣️ LeetCode 3243 - Shortest Distance After Road Addition Queries I

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 3243](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i)

# 🧠 Problem Description
# [Github LeetCode 3243 - Shortest Distance After Road Addition Queries I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3243.%20Shortest%20Distance%20After%20Road%20Addition%20Queries%20I)


from collections import defaultdict
import heapq


class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def dijkstra(start, end):
            distances = [float('inf')] * n
            distances[start] = 0
            pq = [(0, start)]

            while pq:
                curr_dist, curr_node = heapq.heappop(pq)

                if curr_dist > distances[curr_node]:
                    continue
                for neighbor, weight in graph[curr_node]:
                    distance = curr_dist + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(pq, (distance, neighbor))
            return distances[end]
        graph = defaultdict(list)
        for i in range(n -1):
            graph[i].append((i + 1, 1))
        result = []
        for u, v in queries:
            graph[u].append((v, 1))
            shortest_path = dijkstra(0, n - 1)
            result.append(shortest_path)
        return result