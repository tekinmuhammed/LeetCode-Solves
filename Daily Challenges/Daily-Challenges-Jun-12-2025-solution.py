# 3423. Maximum Difference Between Adjacent Elements in a Circular Array

# **Problem Link:** [LeetCode 3423](https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/)  
# **Difficulty:** Easy

# 🧠 Problem Description 
# [Github  3423. Maximum Difference Between Adjacent Elements in a Circular Array](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3423.%20Maximum%20Difference%20Between%20Adjacent%20Elements%20in%20a%20Circular%20Array)

class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_diff = 0
        n = len(nums)

        for i in range(n):
            j = (i + 1) % n
            diff = abs(nums[i] - nums[j])
            max_diff = max(max_diff, diff)
        return max_diff