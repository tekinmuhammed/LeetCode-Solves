# 🎨 LeetCode 75 - Sort Colors

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 75](https://leetcode.com/problems/sort-colors/)

# 🧠 Problem Description 
# [Github LeetCode 75 - Sort Colors](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/75.%20Sort%20Colors)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) -1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid +=1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1