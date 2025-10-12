# 3487. Maximum Unique Subarray Sum After Deletion

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 3487](https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/)

# 🧠 Problem Description
# [Github LeetCode 3136. Valid Word](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3487.%20Maximum%20Unique%20Subarray%20Sum%20After%20Deletion)

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positiveNumsSet = set([num for num in nums if num > 0])
        return max(nums) if len(positiveNumsSet) == 0 else sum(positiveNumsSet)