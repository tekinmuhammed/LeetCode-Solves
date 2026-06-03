# 3635. Earliest Finish Time for Land and Water Rides II

**Difficulty:** Medium
**Problem Link:** [LeetCode 3635](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/)

---

## Problem
You are given the start times and durations for two types of amusement park rides: Land rides and Water rides. 

Specifically, you are given four integer arrays:
* `landStartTime` and `landDuration` for land rides.
* `waterStartTime` and `waterDuration` for water rides.

You want to go on exactly **one land ride** and exactly **one water ride** in any order (Land then Water, or Water then Land). You cannot overlap them. If you finish your first ride before the second ride starts, you must wait until the second ride's start time.

Return the **earliest possible time** you can finish both rides.

*(Note: In Version II of this problem, the constraints are much larger, making a brute-force $O(N \times M)$ approach result in a Time Limit Exceeded error.)*

---

# Approach

To optimize this from $O(N \times M)$ to **O(N + M)**, we can use a **Greedy decoupling** strategy.

The key insight is that the optimal choice for the *first* ride is completely independent of the *second* ride. To finish the second ride as early as possible, we simply need to be available as early as possible. Therefore, we just need to find the absolute minimum finish time for the first ride category, and use that single value as our "availability time" to find the best second ride.

Steps:

1. **Helper Function `solve(start1, duration1, start2, duration2)`:**
   * This function calculates the earliest finish time assuming we take Ride Type 1 first, and Ride Type 2 second.
2. **Minimize First Ride (`finish1`):**
   * We iterate through all rides of Type 1.
   * We find the absolute earliest time we can finish *any* ride of Type 1: `finish1 = min(start1[i] + duration1[i])`.
3. **Minimize Second Ride (`finish2`):**
   * Now that we know we are available at exactly `finish1`, we iterate through all rides of Type 2.
   * For each Type 2 ride, our actual start time is `max(start2[i], finish1)`.
   * We calculate the final finish time for this ride: `actual_start + duration2[i]`.
   * We keep track of the minimum `finish2` across all Type 2 rides.
4. **Evaluate Both Orderings:**
   * Since we can do Land $\rightarrow$ Water OR Water $\rightarrow$ Land, we call our `solve` function for both permutations.
   * Finally, we return the minimum of these two global possibilities.

---

# Example Walkthrough

Assume Land rides are `Type 1` and Water rides are `Type 2`.

* `start1 = [2, 5]`, `duration1 = [5, 1]`
* `start2 = [10, 15]`, `duration2 = [3, 2]`

**Scenario: Land First -> Water Second**
1. **Find `finish1`:**
   * Land Ride 0: finishes at `2 + 5 = 7`
   * Land Ride 1: finishes at `5 + 1 = 6`
   * Minimum `finish1` = `6`. (We are free at time 6).
2. **Find `finish2` (Available at 6):**
   * Water Ride 0: starts at `10`. `max(6, 10) = 10`. Finishes at `10 + 3 = 13`.
   * Water Ride 1: starts at `15`. `max(6, 15) = 15`. Finishes at `15 + 2 = 17`.
   * Minimum `finish2` = `13`.

The algorithm does the exact same process for Water $\rightarrow$ Land, taking $O(N)$ for the first pass and $O(M)$ for the second pass, avoiding nested loops entirely.

---

# Complexity Analysis

Time Complexity

O(N + M)

Where `N` is the number of land rides and `M` is the number of water rides. Instead of nested loops, we use two separate linear passes inside the `solve` function. The first pass takes $O(N)$ and the second takes $O(M)$ (or vice versa). We do this twice (once for each order), so the overall time is $2 \times (O(N) + O(M))$, which simplifies to **O(N + M)**.

Space Complexity

O(1)

The algorithm calculates minimums on the fly using just a few integer variables (`finish1`, `finish2`, `land_water`, `water_land`). No extra arrays or data structures are created, making the auxiliary space strictly constant.

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
        def solve(start1, duration1, start2, duration2):
            finish1 = inf
            # Step 1: Find the absolute earliest finish time for the first ride
            for i in range(len(start1)):
                finish1 = min(finish1, start1[i] + duration1[i])
                
            finish2 = inf
            # Step 2: Use finish1 as availability to find the earliest finish for the second ride
            for i in range(len(start2)):
                finish2 = min(finish2, max(start2[i], finish1) + duration2[i])
                
            return finish2

        # Scenario A: Land first, Water second
        land_water = solve(
            landStartTime, landDuration, waterStartTime, waterDuration
        )
        
        # Scenario B: Water first, Land second
        water_land = solve(
            waterStartTime, waterDuration, landStartTime, landDuration
        )
        
        return min(land_water, water_land)
```