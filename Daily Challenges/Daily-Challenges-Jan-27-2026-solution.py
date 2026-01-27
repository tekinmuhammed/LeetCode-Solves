## 3650. Minimum Cost Path with Edge Reversals

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 3650](https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/description/)

# 🧠 Problem Description
# [Github LeetCode 3650. Minimum Cost Path with Edge Reversals](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3650.%20Minimum%20Cost%20Path%20with%20Edge%20Reversals)

import heapq

class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        # Grafı oluştur (Adjacency List)
        # Her kenar [u, v, w] için:
        # 1. Normal geçiş: u -> v maliyet w
        # 2. Ters geçiş (Switch): v -> u maliyet 2 * w
        
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            # Normal yol
            adj[u].append((v, w))
            # Ters yol (Reverse edge) - Switch kullanarak
            adj[v].append((u, 2 * w))
            
        # Dijkstra Algoritması
        # (maliyet, düğüm)
        pq = [(0, 0)]
        
        # min_dist[i]: 0'dan i'ye olan minimum maliyet
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        
        while pq:
            d, u = heapq.heappop(pq)
            
            # Eğer hedef düğüme ulaştıysak ve bu en kısa yolsa, sonucu döndür
            if u == n - 1:
                return d
            
            # Eğer bu düğüme daha kısa bir yoldan zaten ulaşıldıysa atla
            if d > min_dist[u]:
                continue
            
            # Komşuları gez
            for v, weight in adj[u]:
                if min_dist[u] + weight < min_dist[v]:
                    min_dist[v] = min_dist[u] + weight
                    heapq.heappush(pq, (min_dist[v], v))
                    
        # Eğer n-1 düğümüne ulaşılamıyorsa
        return -1 if min_dist[n-1] == float('inf') else min_dist[n-1]