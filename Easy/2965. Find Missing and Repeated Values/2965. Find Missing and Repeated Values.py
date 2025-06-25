class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        num_list = [num for row in grid for num in row]
        num_counts = Counter(num_list)
        repeated = missing = -1
        for num in range(1, n * n + 1):
            if num_counts[num] == 2:
                repeated = num
            elif num_counts[num] == 0:
                missing = num
        return [repeated, missing]