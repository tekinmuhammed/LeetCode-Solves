# 3689. Maximum Total Subarray Value I

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 3689](https://leetcode.com/problems/maximum-total-subarray-value-i/description/)

# 🧠 Problem Description  
# [Github LeetCode 3689. Maximum Total Subarray Value I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3689.%20Maximum%20Total%20Subarray%20Value%20I) 

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        m1 = min(nums)
        m2 = max(nums)
        return (m2 - m1) * k