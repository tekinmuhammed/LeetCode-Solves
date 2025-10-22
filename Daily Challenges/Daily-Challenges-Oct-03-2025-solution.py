# 407. Trapping Rain Water II

## Difficulty: Hard
## Problem Link: [LeetCode - 407. Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/)  

# 🧠 Problem Description 
# [Github LeetCode 407. Trapping Rain Water II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/407.%20Trapping%20Rain%20Water%20II)

import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        
        # Put all border cells into heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        trapped = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while heap:
            height, x, y = heapq.heappop(heap)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    trapped += max(0, height - heightMap[nx][ny])
                    heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
        
        return trapped