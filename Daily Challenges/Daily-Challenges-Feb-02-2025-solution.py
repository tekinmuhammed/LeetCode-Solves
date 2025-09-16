# 🔁 LeetCode 1752 - Check if Array Is Sorted and Rotated

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 1752](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/)

# 🧠 Problem Description
# [Github LeetCode 1752 - Check if Array Is Sorted and Rotated](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1752.%20Check%20if%20Array%20Is%20Sorted%20and%20Rotated)

class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i +1) % n]:
                count += 1
        return count <= 1