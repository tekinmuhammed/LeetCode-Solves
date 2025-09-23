# 🔄 LeetCode 3355 - Zero Array Transformation I

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 3355](https://leetcode.com/problems/zero-array-transformation-i)

# 🧠 Problem Description 
# [Github LeetCode 3355 - Zero Array Transformation I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3355.%20Zero%20Array%20Transformation%20I)

class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict

        n = len(nums)
        ops = [0] * (n + 1)

        for l, r in queries:
            ops[l] += 1
            if r + 1 < len(ops):
                ops[r + 1] -= 1
        
        for i in range(1, n):
            ops[i] += ops[i - 1]
        
        for i in range(n):
            if nums[i] > ops[i]:
                return False

        return True