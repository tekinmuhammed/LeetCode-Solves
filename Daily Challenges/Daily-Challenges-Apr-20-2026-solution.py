# 2078. Two Furthest Houses With Different Colors

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 2078](https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/)

# 🧠 Problem Description
# [Github LeetCode 2078. Two Furthest Houses With Different Colors](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2078.%20Two%20Furthest%20Houses%20With%20Different%20Colors) 

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        res = 0  # the maximum distance between two houses of different colors
        # traverse the indices of two houses and maintain the maximum distance
        for i in range(n):
            for j in range(i + 1, n):
                if colors[i] != colors[j]:
                    res = max(res, j - i)
        return res