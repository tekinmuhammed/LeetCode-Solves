# 2348. Number of Zero-Filled Subarrays  

# **Difficulty:** Medium  
# **Link:** [LeetCode 2348](https://leetcode.com/problems/number-of-zero-filled-subarrays/)  

# 🧠 Problem Description 
# [Github LeetCode 2348. Number of Zero-Filled Subarrays  ](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2348.%20Number%20of%20Zero-Filled%20Subarrays)

class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = 0

        for n in nums:
            if n == 0:
                count += 1
                result += count
            else:
                count = 0
        return result