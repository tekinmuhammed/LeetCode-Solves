## 1877. Minimize Maximum Pair Sum in Array

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 1877](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/)

# 🧠 Problem Description
# [Github LeetCode 1877. Minimize Maximum Pair Sum in Array](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1877.%20Minimize%20Maximum%20Pair%20Sum%20in%20Array)

class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        res = 0
        l, r = 0, len(nums) - 1

        while l < r:
            res = max(res, nums[l] + nums[r])
            l += 1
            r -= 1

        return res