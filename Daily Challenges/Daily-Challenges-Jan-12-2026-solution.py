# 1266. Minimum Time Visiting All Points

# **Difficulty:** Easy
# **Link:** [LeetCode 1266](https://leetcode.com/problems/minimum-time-visiting-all-points/description/)

# 🧠 Problem Description
# [Github LeetCode 1266. Minimum Time Visiting All Points](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1266.%20Minimum%20Time%20Visiting%20All%20Point)

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        total_time = 0
        
        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]
            
            total_time += max(abs(x2 - x1), abs(y2 - y1))
        
        return total_time