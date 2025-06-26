import math
class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        def canRepairAll(time):
            repaired = 0
            for r in ranks:
                repaired += int(math.sqrt(time // r))
            return repaired >= cars
        left, right = 1, min(ranks) * cars * cars
        while left < right:
            mid = (left + right) // 2
            if canRepairAll(mid):
                right = mid
            else:
                left = mid + 1
        return left