# 1848. Minimum Distance to the Target Element

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 1848](https://leetcode.com/problems/minimum-distance-to-the-target-element/)

# 🧠 Problem Description
# [Github LeetCode 1848. Minimum Distance to the Target Element](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1848.%20Minimum%20Distance%20to%20the%20Target%20Element) 

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = len(nums)
        for i, num in enumerate(nums):
            if num == target:
                res = min(res, abs(i - start))
        return res
