# 3633. Earliest Finish Time for Land and Water Rides I

**Difficulty:** Medium
**Problem Link:** [LeetCode 3633](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/description/)

---

## Problem
You are given the start times and durations for two types of amusement park rides: Land rides and Water rides. 

Specifically, you are given four integer arrays:
* `landStartTime` and `landDuration` for land rides.
* `waterStartTime` and `waterDuration` for water rides.

You want to go on exactly **one land ride** and exactly **one water ride**. You can go on them in any order (Land then Water, or Water then Land), but you cannot overlap them. If you finish your first ride before the second ride starts, you must wait until the second ride's start time.

Return the **earliest possible time** you can finish both rides.
  
--- 
 
# Approach 

Since this is the "Version I" of the problem (usually implying smaller constraints), a **Brute-Force / Simulation** approach works perfectly. We can simply evaluate every possible pair of one land ride and one water ride.

For every pair `(i, j)` where `i` is the land ride and `j` is the water ride, there are two scenarios:

1. **Land Ride First, then Water Ride:**
   * You finish the land ride at `land_finish = landStartTime[i] + landDuration[i]`.
   * You can only start the water ride after you finish the land ride AND after the water ride actually begins. So your actual start time for the water ride is `max(land_finish, waterStartTime[j])`.
   * Your final finish time is `actual_water_start + waterDuration[j]`.

2. **Water Ride First, then Land Ride:**
   * You finish the water ride at `water_finish = waterStartTime[j] + waterDuration[j]`.
   * Your actual start time for the land ride is `max(water_finish, landStartTime[i])`.
   * Your final finish time is `actual_land_start + landDuration[i]`.

We calculate both scenarios for all pairs and keep track of the absolute minimum finish time using a variable `res` initialized to infinity.
 
--- 
 
# Example Walkthrough

Imagine we are evaluating a specific pair:
* Land Ride: Starts at `2`, Duration `5`
* Water Ride: Starts at `10`, Duration `3`

**Scenario 1: Land -> Water**
* Finish Land: `2 + 5 = 7`.
* Start Water: We must wait until time `10` to start the water ride. `max(7, 10) = 10`.
* Finish Water: `10 + 3 = 13`.

**Scenario 2: Water -> Land**
* Finish Water: `10 + 3 = 13`.
* Start Land: The land ride started at `2`, but we only arrived at `13`. `max(13, 2) = 13`.
* Finish Land: `13 + 5 = 18`.

For this specific pair, the earliest finish time is `min(13, 18) = 13`. The algorithm does this for all pairs and returns the global minimum.
 
--- 
 
# Complexity Analysis

Time Complexity

O(N \times M)

Where `N` is the number of land rides and `M` is the number of water rides. The algorithm uses nested loops to pair every land ride with every water ride, performing constant $O(1)$ mathematical checks for each pair.

Space Complexity

O(1)

We only use a few variables (`n`, `m`, `res`, and temporary calculation variables) regardless of the size of the input arrays, meaning the auxiliary space used is constant.
 
--- 
 
# Code 

```python
from typing import List
from math import inf

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
                # Scenario 1: Land ride first, then Water ride
                land = landStartTime[i] + landDuration[i]
                land_water = max(land, waterStartTime[j]) + waterDuration[j]
                res = min(res, land_water)

                # Scenario 2: Water ride first, then Land ride
                water = waterStartTime[j] + waterDuration[j]
                water_land = max(water, landStartTime[i]) + landDuration[i]
                res = min(res, water_land)
                
        return res
```