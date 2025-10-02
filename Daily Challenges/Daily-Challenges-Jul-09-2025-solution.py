# 3439. Reschedule Meetings for Maximum Free Time I

# **Difficulty:** Medium  
# **Link:** [LeetCode 3439](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i)

# 🧠 Problem Description 
# [Github LeetCode 3439. Reschedule Meetings for Maximum Free Time I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3439.%20Reschedule%20Meetings%20for%20Maximum%20Free%20Time%20I)

class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        n = len(startTime)
        res = 0
        total = [0] * (n + 1)
        for i in range(n):
            total[i + 1] = total[i] + endTime[i] - startTime[i]
        for i in range(k - 1, n):
            right = eventTime if i == n - 1 else startTime[i + 1]
            left = 0 if i == k - 1 else endTime[i - k]
            res = max(res, right - left - (total[i + 1] - total[i - k + 1]))
        return res