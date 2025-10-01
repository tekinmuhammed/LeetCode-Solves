# 2966. Divide Array Into Arrays With Max Difference

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2966](https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/)

# 🧠 Problem Description 
# [Github LeetCode 2966. Divide Array Into Arrays With Max Difference](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2966.%20Divide%20Array%20Into%20Arrays%20With%20Max%20Difference)

class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(0, len(nums), 3):
            group = nums[i:i+3]
            if len(group) < 3 or group[-1] - group[0] > k:
                return []
            result.append(group)
        return result