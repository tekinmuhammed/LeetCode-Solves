# 🌟 LeetCode 2401 - Longest Nice Subarray

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2401](https://leetcode.com/problems/longest-nice-subarray)

# 🧠 Problem Description
# [Github LeetCode 2401 - Longest Nice Subarray](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2401.%20Longest%20Nice%20Subarray)

class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        left = 0
        bitmask = 0
        
        for right in range(len(nums)):
            while(bitmask & nums[right]) != 0:
                bitmask ^= nums[left]
                left += 1
            bitmask |= nums[right]
            max_len = max(max_len, right - left + 1)
        return max_len