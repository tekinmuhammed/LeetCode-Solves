# 2770. Maximum Number of Jumps to Reach the Last Index

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 2770](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/description/)

# 🧠 Problem Description
# [Github LeetCode 2770. Maximum Number of Jumps to Reach the Last Index](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2770.%20Maximum%20Number%20of%20Jumps%20to%20Reach%20the%20Last%20Index) 

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i: int):
            if i == len(nums) - 1:
                return 0

            res = -inf
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) <= target:
                    res = max(res, dfs(j) + 1)
            return res

        ans = dfs(0)
        return -1 if ans < 0 else ans