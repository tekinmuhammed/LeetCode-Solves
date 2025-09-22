# ⚙️ LeetCode 3191 - Minimum Operations to Make Binary Array Elements Equal to One I

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 3191](https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i)

# 🧠 Problem Description
# [Github LeetCode 3191 - Minimum Operations to Make Binary Array Elements Equal to One I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3191.%20Minimum%20Operations%20to%20Make%20Binary%20Array%20Elements%20Equal%20to%20One%20I)

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                count += 1
        if all(num == 1 for num in nums):
            return count
        else:
            return -1