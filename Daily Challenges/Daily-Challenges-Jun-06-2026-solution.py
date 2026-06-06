# 2574. Left and Right Sum Differences

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 2574](https://leetcode.com/problems/left-and-right-sum-differences/description/)

# 🧠 Problem Description  
# [Github LeetCode 2574. Left and Right Sum Differences](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2574.%20Left%20and%20Right%20Sum%20Differences) 

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        left_sum = 0
        for i in range(n):
            ans[i] = left_sum
            left_sum += nums[i]

        right_sum = 0
        for i in range(n - 1, -1, -1):
            ans[i] = abs(ans[i] - right_sum)
            right_sum += nums[i]

        return ans