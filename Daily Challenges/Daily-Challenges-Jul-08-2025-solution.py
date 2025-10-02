# 1751. Maximum Number of Events That Can Be Attended II

# **Difficulty:** Hard  
# **Link:** [LeetCode 1751](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/)

# 🧠 Problem Description 
# [Github LeetCode 1751. Maximum Number of Events That Can Be Attended II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/1751.%20Maximum%20Number%20of%20Events%20That%20Can%20Be%20Attended%20II)

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:        
        events.sort()
        n = len(events)
        starts = [start for start, end, value in events]
        dp = [[-1] * n for _ in range(k + 1)]
        
        def dfs(cur_index, count):
            if count == 0 or cur_index == n:
                return 0
            if dp[count][cur_index] != -1:
                return dp[count][cur_index]

            # Find the nearest available event after attending event 0.

            next_index = bisect_right(starts, events[cur_index][1])
            dp[count][cur_index] = max(dfs(cur_index + 1, count), events[cur_index][2] + dfs(next_index, count - 1))
            return dp[count][cur_index]
        
        return dfs(0, k)