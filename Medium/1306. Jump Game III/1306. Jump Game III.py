class Solution(object):
    def canReach(self, arr, start):
        visited = set()
        stack = [start]

        while stack:
            i = stack.pop()

            if i < 0 or i >= len(arr) or i in visited:
                continue

            if arr[i] == 0:
                return True

            visited.add(i)

            stack.append(i + arr[i])
            stack.append(i - arr[i])

        return False