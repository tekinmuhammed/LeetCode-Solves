# 153. Find Minimum in Rotated Sorted Array

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

# 🧠 Problem Description
# [Github LeetCode 153. Find Minimum in Rotated Sorted Array](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array) 

class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]