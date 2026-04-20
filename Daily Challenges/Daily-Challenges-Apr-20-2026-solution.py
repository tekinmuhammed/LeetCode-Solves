# 2078. Two Furthest Houses With Different Colors

**Difficulty:** Easy
**Problem Link:** [LeetCode 2078](https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/)

# 🧠 Problem Description
# [Github LeetCode 1855. Maximum Distance Between a Pair of Values](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1855.%20Maximum%20Distance%20Between%20a%20Pair%20of%20Values) 

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