# 407. Trapping Rain Water II  

## Difficulty: Hard  

## Problem Link  
[LeetCode - 407. Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/)  

## Tags  
`Heap` `Priority Queue` `BFS` `Matrix`  

---

## Problem Description  
Given an `m x n` 2D elevation map `heightMap` representing the height of each cell, compute how much water it is able to trap after raining.  

Water can only be trapped if surrounded by higher boundaries. This problem is the 2D extension of **Trapping Rain Water (Problem 42)**.  

---

## Approach  

We use a **Priority Queue (Min-Heap)** and a **BFS-like traversal**:  

1. **Initialize:**  
   - Push all border cells into a min-heap (since water can only be trapped inside, not outside).  
   - Mark them as visited.  

2. **Process with heap:**  
   - Repeatedly pop the cell with the lowest height.  
   - For each neighbor (up, down, left, right):  
     - If not visited:  
       - Water trapped = `max(0, currentHeight - neighborHeight)`  
       - Push neighbor into heap with `max(currentHeight, neighborHeight)` as its effective boundary.  
       - Mark as visited.  

3. **Accumulate total trapped water**.  

This ensures we always expand from the lowest boundary outward, correctly simulating water filling.  

---

## Code Implementation  

```python
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
```

### Complexity Analysis

**Time Complexity:** `𝑂(𝑚⋅𝑛⋅log(𝑚⋅𝑛))` due to heap operations.

**Space Complexity:** `𝑂(𝑚⋅𝑛)` for the visited matrix and heap.

## Example

### Input:
```python
heightMap = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
```

### Output:
```python
4
```

Explanation:
The low-height inner cells trap 4 units of water total.