class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 1 + 4 * ((n - 1) * n) // 2