# 🚫 LeetCode 2364 - Count Number of Bad Pairs

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2364](https://leetcode.com/problems/count-number-of-bad-pairs/)

# 🧠 Problem Description
# [Github LeetCode 2364 - Count Number of Bad Pairs](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2364.%20Count%20Number%20of%20Bad%20Pairs)

class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        diff_map = {}
        good_pairs = 0
        for i, num in enumerate(nums):
            diff = i - num
            if diff in diff_map:
                good_pairs += diff_map[diff]
            diff_map[diff] = diff_map.get(diff, 0) + 1
        return total_pairs - good_pairs