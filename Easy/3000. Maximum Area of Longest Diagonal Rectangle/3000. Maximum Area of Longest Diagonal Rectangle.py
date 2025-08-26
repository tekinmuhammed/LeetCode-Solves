import math

class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        max_diag = 0
        max_area = 0

        for l, w in dimensions:
            diag = math.sqrt(l*l + w*w)
            area = l * w

            if diag > max_diag:
                max_diag = diag
                max_area = area
            elif diag == max_diag:
                max_area = max(max_area, area)

        return max_area