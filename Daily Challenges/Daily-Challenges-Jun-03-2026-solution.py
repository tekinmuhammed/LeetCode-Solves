# 3635. Earliest Finish Time for Land and Water Rides II

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 3635](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/)

# 🧠 Problem Description  
# [Github LeetCode 3635. Earliest Finish Time for Land and Water Rides II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3635.%20Earliest%20Finish%20Time%20for%20Land%20and%20Water%20Rides%20II) 

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        def solve(start1, duration1, start2, duration2):
            finish1 = inf
            for i in range(len(start1)):
                finish1 = min(finish1, start1[i] + duration1[i])
            finish2 = inf
            for i in range(len(start2)):
                finish2 = min(finish2, max(start2[i], finish1) + duration2[i])
            return finish2

        land_water = solve(
            landStartTime, landDuration, waterStartTime, waterDuration
        )
        water_land = solve(
            waterStartTime, waterDuration, landStartTime, landDuration
        )
        return min(land_water, water_land)