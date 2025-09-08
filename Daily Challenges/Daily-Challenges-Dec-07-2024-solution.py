# 🎯 LeetCode 1760 - Minimum Limit of Balls in a Bag

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1760](https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/)

# 🧠 Problem Description
# [Github LeetCode 1760 - Minimum Limit of Balls in a Bag](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1760.%20Minimum%20Limit%20of%20Balls%20in%20a%20Bag)

class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        def canDivide(maxPenalty):
            operations = 0
            for num in nums:
                if num > maxPenalty:
                    operations += (num - 1) // maxPenalty
            return operations <= maxOperations

        left, right = 1, max(nums)
        result = right
        while left <= right:
            mid = (left + right) // 2
            if canDivide(mid):
                result = mid
                right = mid -1
            else:
                left = mid + 1
        return result