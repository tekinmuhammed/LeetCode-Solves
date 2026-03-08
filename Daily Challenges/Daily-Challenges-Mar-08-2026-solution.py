# 1980. Find Unique Binary String

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 1980](https://leetcode.com/problems/find-unique-binary-string/description/)

# 🧠 Problem Description
# [Github LeetCode 1980. Find Unique Binary String](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1980.%20Find%20Unique%20Binary%20String)

class Solution(object):
    def findDifferentBinaryString(self, nums):
        res = []
        
        for i in range(len(nums)):
            if nums[i][i] == '0':
                res.append('1')
            else:
                res.append('0')
        
        return "".join(res)