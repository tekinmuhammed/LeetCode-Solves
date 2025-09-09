# 🟨 LeetCode 3264 - Final Array State After K Multiplication Operations I

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 3264](https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/)

# 🧠 Problem Description 
# [Github LeetCode 3264 - Final Array State After K Multiplication Operations I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3264.%20Final%20Array%20State%20After%20K%20Multiplication%20Operations%20I)

class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        for _ in range(k):
            min_index = nums.index(min(nums))
            nums[min_index] *= multiplier
        return nums