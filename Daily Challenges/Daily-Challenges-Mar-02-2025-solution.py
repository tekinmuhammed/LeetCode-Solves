# 🔄 LeetCode 2460 - Apply Operations to an Array

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 2460](https://leetcode.com/problems/apply-operations-to-an-array)

# 🧠 Problem Description
# [Github LeetCode 2460 - Apply Operations to an Array](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2460.%20Apply%20Operations%20to%20an%20Array)

class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        result = [num for num in nums if num != 0]
        result.extend([0] * (len(nums) - len(result)))
        return result