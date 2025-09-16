# 🔼 LeetCode 1800 - Maximum Ascending Subarray Sum

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 1800](https://leetcode.com/problems/maximum-ascending-subarray-sum/)

# 🧠 Problem Description
# [Github LeetCode 1800 - Maximum Ascending Subarray Sum](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1800.%20Maximum%20Ascending%20Subarray%20Sum)

class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = 0
        current_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]
        max_sum = max(max_sum, current_sum)
        return max_sum