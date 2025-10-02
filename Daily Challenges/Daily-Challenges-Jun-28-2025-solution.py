# 2099. Find Subsequence of Length K With the Largest Sum

# **Difficulty:** Easy  
# **Link:** [LeetCode 2099](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/)

# 🧠 Problem Description 
# [Github LeetCode 2099. Find Subsequence of Length K With the Largest Sum](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2099.%20Find%20Subsequence%20of%20Length%20K%20With%20the%20Largest%20Sum)

class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        indexed = list(enumerate(nums))
        indexed.sort(key=lambda x: x[1], reverse=True)
        top_k = sorted(indexed[:k], key=lambda x: x[0])
        return [val for i, val in top_k]