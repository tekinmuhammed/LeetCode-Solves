from collections import deque
class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        n = len(status)
        visited = [False] * n
        has_key = status[:]
        queue = deque()
        boxes = set(initialBoxes)

        for box in initialBoxes:
            if has_key[box]:
                queue.append(box)
                visited[box] = True

        total = 0
        while queue:
            box = queue.popleft()
            total += candies[box]

            for k in keys[box]:
                has_key[k] = 1
                if k in boxes and not visited[k]:
                    queue.append(k)
                    visited[k] = True
            for b in containedBoxes[box]:
                boxes.add(b)
                if has_key[b] and not visited[b]:
                    queue.append(b)
                    visited[b] = True
        return total