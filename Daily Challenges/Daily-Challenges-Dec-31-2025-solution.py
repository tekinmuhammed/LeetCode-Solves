# 1970. Last Day Where You Can Still Cross

# **Difficulty:** Hard
# **Problem Link:** [LeetCode 1970](https://leetcode.com/problems/last-day-where-you-can-still-cross/description/)

# 🧠 Problem Description
# [Github LeetCode 1970. Last Day Where You Can Still Cross](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/1970.%20Last%20Day%20Where%20You%20Can%20Still%20Cross)

from collections import deque

class Solution(object):
    def latestDayToCross(self, row, col, cells):
        
        def canCross(day):
            grid = [[0] * col for _ in range(row)]
            
            # Flood cells up to 'day'
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1
            
            q = deque()
            visited = [[False]*col for _ in range(row)]
            
            # Start from top row
            for j in range(col):
                if grid[0][j] == 0:
                    q.append((0, j))
                    visited[0][j] = True
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while q:
                x, y = q.popleft()
                
                if x == row - 1:
                    return True
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col:
                        if not visited[nx][ny] and grid[nx][ny] == 0:
                            visited[nx][ny] = True
                            q.append((nx, ny))
            
            return False
        
        left, right = 0, len(cells)
        answer = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canCross(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return answer