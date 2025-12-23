# 2054. Two Best Non-Overlapping Events

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 2054](https://leetcode.com/problems/two-best-non-overlapping-events/description/)

# 🧠 Problem Description
# [Github LeetCode 2054. Two Best Non-Overlapping Events](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2054.%20Two%20Best%20Non-Overlapping%20Events-2)

import bisect

class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        # sort by start time
        events.sort()
        n = len(events)

        # suffixMax[i] = max value from events[i:] onwards
        suffixMax = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffixMax[i] = max(suffixMax[i + 1], events[i][2])

        # array of start times for binary search
        starts = [e[0] for e in events]

        ans = 0
        for i in range(n):
            s, e, v = events[i]

            # option 1: take only this event
            ans = max(ans, v)

            # option 2: take this + next non-overlapping event
            # next event must start at >= e + 1
            j = bisect.bisect_left(starts, e + 1)
            if j < n:
                ans = max(ans, v + suffixMax[j])

        return ans