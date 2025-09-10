# 🟨 LeetCode 2270 - Number of Ways to Split Array

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 2270](https://leetcode.com/problems/number-of-ways-to-split-array)

# 🧠 Problem Description 
# [Github LeetCode 2270 - Number of Ways to Split Array](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2270.%20Number%20of%20Ways%20to%20Split%20Array)

class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0
        count = 0
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum = total_sum - left_sum
            if left_sum >= right_sum:
                count += 1
        return count