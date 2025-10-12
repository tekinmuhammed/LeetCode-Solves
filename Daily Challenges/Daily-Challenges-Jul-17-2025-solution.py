# 3202. Find the Maximum Length of Valid Subsequence II 

# **Difficulty:** Medium
# **Link:** [LeetCode 3202](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii)

# 🧠 Problem Description
# [Github LeetCode 3202. Find the Maximum Length of Valid Subsequence II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3202.%20Find%20the%20Maximum%20Length%20of%20Valid%20Subsequence%20II)

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        res = 0
        for num in nums:
            num %= k
            for prev in range(k):
                dp[prev][num] = dp[num][prev] + 1
                res = max(res, dp[prev][num])
        return res