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