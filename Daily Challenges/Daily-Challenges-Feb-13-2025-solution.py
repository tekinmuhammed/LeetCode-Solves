# 🔺 LeetCode 3066 - Minimum Operations to Exceed Threshold Value II

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 3066](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii)

# 🧠 Problem Description
# [Github LeetCode 3066 - Minimum Operations to Exceed Threshold Value II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3066.%20Minimum%20Operations%20to%20Exceed%20Threshold%20Value%20II)

import heapq
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        operations = 0
        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new_value = x * 2 + y
            heapq.heappush(nums, new_value)
            operations += 1
        if nums[0] < k:
            return -1
        return operations