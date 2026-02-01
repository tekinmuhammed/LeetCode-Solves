## 3010. Divide an Array Into Subarrays With Minimum Cost I

# **Difficulty:** Easy  
# **Link:** [LeetCode 3010](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description/)  

# 🧠 Problem Description
# [Github LeetCode 3010. Divide an Array Into Subarrays With Minimum Cost I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3010.%20Divide%20an%20Array%20Into%20Subarrays%20With%20Minimum%20Cost%20I)

class Solution(object):
    def minimumCost(self, nums):
        rest = nums[1:]
        rest.sort()
        return nums[0] + rest[0] + rest[1]