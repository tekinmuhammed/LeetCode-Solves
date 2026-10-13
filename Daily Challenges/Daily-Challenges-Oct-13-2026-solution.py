# 3727. Maximum Alternating Sum of Squares

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 3727](https://leetcode.com/problems/maximum-alternating-sum-of-squares/)

# 🧠 Problem Description 
# [Github LeetCode 3727. Maximum Alternating Sum of Squares](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3727.%20Maximum%20Alternating%20Sum%20of%20Squares)

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] *= nums[i]
        nums.sort()
        return -sum(nums[: n // 2]) + sum(nums[n // 2 :])