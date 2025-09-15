# ✨ LeetCode 3151 - Special Array I

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 3151](https://leetcode.com/problems/special-array-i)

# 🧠 Problem Description
# [Github LeetCode 3151 - Special Array I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3151.%20Special%20Array%20I)

class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)- 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True