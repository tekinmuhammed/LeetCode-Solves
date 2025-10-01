# 3443. Maximum Manhattan Distance After K Changes

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 3443](https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes)

# 🧠 Problem Description 
# [Github LeetCode 3443. Maximum Manhattan Distance After K Changes](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3443.%20Maximum%20Manhattan%20Distance%20After%20K%20Changes)

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        latitude = 0
        longitude = 0
        ans = 0
        n = len(s)
        for i in range(n):
            if s[i] == "N":
                latitude += 1
            elif s[i] == "S":
                latitude -= 1
            elif s[i] == "E":
                longitude += 1
            elif s[i] == "W":
                longitude -= 1
            ans = max(ans, min(abs(latitude) + abs(longitude) + k * 2, i + 1))
        return ans