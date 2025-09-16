# 📈 LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 3105](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/)

# 🧠 Problem Description
# [Github LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3105.%20Longest%20Strictly%20Increasing%20or%20Strictly%20Decreasing%20Subarray)

class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        inc_length = dec_length = 1
        max_length = 1
        for i in range(1, n):
            if nums[i] > nums [i - 1]:
                inc_length += 1
                dec_length = 1
            elif nums[i] < nums[i - 1]:
                dec_length += 1
                inc_length = 1
            else:
                inc_length = dec_length = 1
            max_length = max(max_length, inc_length, dec_length)
        return max_length