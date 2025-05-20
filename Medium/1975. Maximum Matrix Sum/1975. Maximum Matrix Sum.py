class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total_sum = 0
        min_abs = float('inf')
        negative_count = 0

        for row in matrix:
            for num in row:
                total_sum += abs(num)
                min_abs = min(min_abs, abs(num))
                if num < 0:
                    negative_count += 1
        if negative_count % 2 == 0:
            return total_sum
        else:
            return total_sum - 2 * min_abs