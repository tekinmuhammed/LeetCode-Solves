# 2210. Count Hills and Valleys in an Array

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 2210](https://leetcode.com/problems/count-hills-and-valleys-in-an-array/)

# 🧠 Problem Description 
# [Github LeetCode 3136. Valid Word](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2210.%20Count%20Hills%20and%20Valleys%20in%20an%20Array)

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        j=0 #to point towards the valid left element to be compared
        for i in range(1,n-1):
            if (nums[i]>nums[i+1] and nums[i]>nums[j]) or (nums[i]<nums[i+1] and nums[i]<nums[j]):
                ans+=1
                j=i
        return ans