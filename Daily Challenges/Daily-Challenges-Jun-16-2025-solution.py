# 2016. Maximum Difference Between Increasing Elements

# **Link:** [LeetCode 2016](https://leetcode.com/problems/maximum-difference-between-increasing-elements/)  
# **Difficulty:** Easy

# 🧠 Problem Description 
# [Github  LeetCode 2016. Maximum Difference Between Increasing Elements](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2016.%20Maximum%20Difference%20Between%20Increasing%20Elements)

class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = nums[0]
        max_diff = -1

        for j in range(1, len(nums)):
            if nums[j] > min_val:
                max_diff = max(max_diff, nums[j] - min_val)
            else:
                min_val = nums[j]
        return max_diff