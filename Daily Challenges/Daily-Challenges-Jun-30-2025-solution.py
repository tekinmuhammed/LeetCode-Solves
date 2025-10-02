# 594. Longest Harmonious Subsequence

# **Difficulty:** Easy  
# **Link:** [LeetCode 594](https://leetcode.com/problems/longest-harmonious-subsequence)

# 🧠 Problem Description 
# [Github LeetCode 594. Longest Harmonious Subsequence](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/594.%20Longest%20Harmonious%20Subsequence)

from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        max_len = 0

        for num in count:
            if num + 1 in count:
                max_len = max(max_len, count[num] + count[num + 1])

        return max_len