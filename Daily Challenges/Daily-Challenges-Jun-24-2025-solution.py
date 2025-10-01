# 2200. Find All K-Distant Indices in an Array

# **Difficulty:** Easy  
# **Link:** [LeetCode Problem 2200](https://leetcode.com/problems/find-all-k-distant-indices-in-an-array)

# 🧠 Problem Description 
# [Github LeetCode 2200. Find All K-Distant Indices in an Array](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2200.%20Find%20All%20K-Distant%20Indices%20in%20an%20Array)

class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        result = set()
        for j, num in enumerate(nums):
            if num == key:
                for i in range(max(0, j - k), min(len(nums), j + k + 1)):
                    result.add(i)
        return sorted(result)