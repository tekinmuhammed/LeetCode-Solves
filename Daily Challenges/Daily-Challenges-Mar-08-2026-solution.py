# 1980. Find Unique Binary String

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1980](https://leetcode.com/problems/find-unique-binary-string/description/)

# 🧠 Problem Description 
# [Github LeetCode 1888. Minimum Number of Flips to Make the Binary String Alternating](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1888.%20Minimum%20Number%20of%20Flips%20to%20Make%20the%20Binary%20String%20Alternating)

class Solution(object):
    def findDifferentBinaryString(self, nums):
        res = []
        
        for i in range(len(nums)):
            if nums[i][i] == '0':
                res.append('1')
            else:
                res.append('0')
        
        return "".join(res)