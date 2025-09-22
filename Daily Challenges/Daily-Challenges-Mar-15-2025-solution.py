# 🏚️ LeetCode 2560 - House Robber IV

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2560](https://leetcode.com/problems/house-robber-iv)

# 🧠 Problem Description
# [Github LeetCode 2560 - House Robber IV](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2560.%20House%20Robber%20IV)

class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def canRob(mid):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= mid:
                    count += 1
                    i += 1
                i += 1
            return count >= k
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if canRob(mid):
                right = mid
            else:
                left = mid + 1
        return left