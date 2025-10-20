# 976. Largest Perimeter Triangle

# **Difficulty:** Easy
# **Link:** [LeetCode 976](https://leetcode.com/problems/largest-perimeter-triangle/)

# 🧠 Problem Description 
# [Github LeetCode 976. Largest Perimeter Triangle](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/976.%20Largest%20Perimeter%20Triangle)

class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)  # Büyükten küçüğe sırala
        for i in range(len(nums) - 2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0