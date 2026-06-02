# 2540. Minimum Common Value

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 2540](https://leetcode.com/problems/minimum-common-value/description/)

# 🧠 Problem Description
# [Github LeetCode 2540. Minimum Common Value](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2540.%20Minimum%20Common%20Value) 

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Add the elements from nums1 to set1
        set1 = set(nums1)

        # Search for each element of nums2 in set1
        # Return the first common element found
        for num in nums2:
            if num in set1:
                return num

        # Return -1 if there are no common elements
        return -1