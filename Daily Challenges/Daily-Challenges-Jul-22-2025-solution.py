# 1695. Maximum Erasure Value

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1695](https://leetcode.com/problems/maximum-erasure-value/)

# 🧠 Problem Description 
# [Github LeetCode 3136. Valid Word](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1695.%20Maximum%20Erasure%20Value)

class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        left = 0
        curr_sum = max_sum = 0
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            seen.add(nums[right])
            curr_sum += nums[right]
            max_sum = max(max_sum, curr_sum)
        return max_sum