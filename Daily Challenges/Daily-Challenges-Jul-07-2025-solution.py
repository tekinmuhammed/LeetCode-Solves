# 1353. Maximum Number of Events That Can Be Attended

# **Difficulty:** Medium  
# **Link:** [LeetCode 1353](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/)

# 🧠 Problem Description 
# [Github LeetCode 1353. Maximum Number of Events That Can Be Attended](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1353.%20Maximum%20Number%20of%20Events%20That%20Can%20Be%20Attended)

import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        min_heap = []
        day = 0
        i = 0
        n = len(events)
        attended = 0

        while i < n  or min_heap:

            if not min_heap:
                day = events[i][0]
            while i < n and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])
                i += 1
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            if min_heap:
                heapq.heappop(min_heap)
                attended += 1
            day += 1
        return attended