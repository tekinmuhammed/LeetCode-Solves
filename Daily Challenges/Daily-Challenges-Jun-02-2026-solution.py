# 3633. Earliest Finish Time for Land and Water Rides I

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 3633](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/description/)

# 🧠 Problem Description  
# [Github LeetCode 3633. Earliest Finish Time for Land and Water Rides I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3633.%20Earliest%20Finish%20Time%20for%20Land%20and%20Water%20Rides%20I) 

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        res = inf
        for i in range(n):
            for j in range(m):
                land = landStartTime[i] + landDuration[i]
                land_water = max(land, waterStartTime[j]) + waterDuration[j]
                res = min(res, land_water)

                water = waterStartTime[j] + waterDuration[j]
                water_land = max(water, landStartTime[i]) + landDuration[i]
                res = min(res, water_land)
        return res