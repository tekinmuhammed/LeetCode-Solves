# 3719. Longest Balanced Subarray I

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 3719](https://leetcode.com/problems/longest-balanced-subarray-i/description/)

# 🧠 Problem Description
# [Github LeetCode 3719. Longest Balanced Subarray I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3719.%20Longest%20Balanced%20Subarray%20I)

class Solution(object):
    def longestBalanced(self, nums):
        n = len(nums)
        ans = 0

        for i in range(n):
            evens = set()
            odds = set()

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    evens.add(nums[j])
                else:
                    odds.add(nums[j])

                if len(evens) == len(odds):
                    ans = max(ans, j - i + 1)

        return ans