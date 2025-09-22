# 🔧 LeetCode 2594 - Minimum Time to Repair Cars

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2594](https://leetcode.com/problems/minimum-time-to-repair-cars)

# 🧠 Problem Description
# [Github LeetCode 2594 - Minimum Time to Repair Cars](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2594.%20Minimum%20Time%20to%20Repair%20Cars)

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