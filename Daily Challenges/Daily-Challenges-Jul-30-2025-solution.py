# 2419. Longest Subarray With Maximum Bitwise AND

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2419](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and)

# 🧠 Problem Description 
# [Github LeetCode 2419. Longest Subarray With Maximum Bitwise AND](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2419.%20Longest%20Subarray%20With%20Maximum%20Bitwise%20AND)


class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = max(nums)
        max_len = 0
        current_len = 0

        for num in nums:
            if num == max_val:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 0
        return max_len