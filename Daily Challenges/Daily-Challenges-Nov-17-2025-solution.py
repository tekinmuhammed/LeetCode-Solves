# 1437. Check If All 1's Are at Least Length K Places Away — Explanation & Analysis

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 1437](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/)

# 🧠 Problem Description 
# [Github LeetCode 1437. Check If All 1's Are at Least Length K Places Away — Explanation & Analysis](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1437.%20Check%20If%20All%201's%20Are%20at%20Least%20Length%20K%20Places%20Away)

class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        prev = -1  # previous 1's index

        for i, val in enumerate(nums):
            if val == 1:
                if prev != -1 and i - prev - 1 < k:
                    return False
                prev = i

        return True