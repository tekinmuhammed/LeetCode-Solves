import heapq

class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        m, n = len(moveTime), len(moveTime[0])
        heap = [(0, 0, 0, 0)]
        visited = [[[float('inf')] * 2 for _ in range(n)] for _ in range(m)]
        visited[0][0][0] = 0
        
        dirs = [(-1, 0), (1, 0), (0,  -1), (0, 1)]

        while heap:
            time, r, c, step = heapq.heappop(heap)
            if r == m - 1 and c == n - 1:
                return time

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    wait = max(0, moveTime[nr][nc] - time)
                    move_cost = 1 if step == 0 else 2
                    new_time = time + wait + move_cost
                    next_step = 1 - step
                    
                    if new_time < visited[nr][nc][next_step]:
                        visited[nr][nc][next_step] = new_time
                        heapq.heappush(heap, (new_time, nr, nc, next_step))
        return -1