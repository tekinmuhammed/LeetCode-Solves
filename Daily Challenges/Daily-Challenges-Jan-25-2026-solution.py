## 1984. Minimum Difference Between Highest and Lowest of K Scores

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 1984](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/)

# 🧠 Problem Description
# [Github LeetCode 1984. Minimum Difference Between Highest and Lowest of K Scores](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1984.%20Minimum%20Difference%20Between%20Highest%20and%20Lowest%20of%20K%20Scores)

class Solution(object):
    def minimumDifference(self, nums, k):
        if k == 1:
            return 0

        nums.sort()
        res = float('inf')

        for i in range(len(nums) - k + 1):
            res = min(res, nums[i + k - 1] - nums[i])

        return res