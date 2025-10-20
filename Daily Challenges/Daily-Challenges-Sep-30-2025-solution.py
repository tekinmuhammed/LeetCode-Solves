# 2221. Find Triangular Sum of an Array  

# **Difficulty:** Easy  
# Problem Link  [LeetCode - 2221. Find Triangular Sum of an Array](https://leetcode.com/problems/find-triangular-sum-of-an-array/)  

# 🧠 Problem Description 
# [Github LeetCode 2221. Find Triangular Sum of an Array  ](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2221.%20Find%20Triangular%20Sum%20of%20an%20Array)

class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
            newNums = []
            for i in range(len(nums) - 1):
                newNums.append((nums[i] + nums[i+1]) % 10)
            nums = newNums
        return nums[0]