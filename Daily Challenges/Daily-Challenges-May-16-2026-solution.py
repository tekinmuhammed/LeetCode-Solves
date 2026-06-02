# 154. Find Minimum in Rotated Sorted Array II

# **Difficulty:** Hard
# **Problem Link:** [LeetCode 154](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/)

# 🧠 Problem Description 
# [Github LeetCode 154. Find Minimum in Rotated Sorted Array II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/154.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array%20II) 

class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            
            elif nums[mid] < nums[right]:
                right = mid
            
            else:
                right -= 1
        
        return nums[left]