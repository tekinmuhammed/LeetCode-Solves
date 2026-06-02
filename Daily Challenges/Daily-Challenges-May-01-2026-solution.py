# 396. Rotate Function 

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 396](https://leetcode.com/problems/rotate-function/description/)

# 🧠 Problem Description
# [Github LeetCode 396. Rotate Function](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/396.%20Rotate%20Function) 

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f, n, numSum = 0, len(nums), sum(nums)
        for i, num in enumerate(nums):
            f += i * num
        res = f
        for i in range(n - 1, 0, -1):
            f = f + numSum - n * nums[i]
            res = max(res, f)
        return res