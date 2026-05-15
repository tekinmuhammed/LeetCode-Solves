
# 🧠 Problem Description
# [Github LeetCode 2784. Check if Array is Good](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2784.%20Check%20if%20Array%20is%20Good) 
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