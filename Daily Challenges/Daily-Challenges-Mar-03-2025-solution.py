# 📊 LeetCode 2161 - Partition Array According to Given Pivot

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2161](https://leetcode.com/problems/partition-array-according-to-given-pivot)

# 🧠 Problem Description
# [Github LeetCode 2161 - Partition Array According to Given Pivot](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2161.%20Partition%20Array%20According%20to%20Given%20Pivot)

class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        left = [num for num in nums if num < pivot]
        middle = [num for num in nums if num == pivot]
        right = [num for num in nums if num > pivot]
        return left + middle + right