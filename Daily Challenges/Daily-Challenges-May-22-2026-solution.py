# 33. Search in Rotated Sorted Array

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 33](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)

# 🧠 Problem Description
# [Github LeetCode 33. Search in Rotated Sorted Array](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/33.%20Search%20in%20Rotated%20Sorted%20Array) 

class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            if nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] > target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
        