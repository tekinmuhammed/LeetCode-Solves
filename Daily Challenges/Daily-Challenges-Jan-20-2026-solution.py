# 🧩 3314. Construct the Minimum Bitwise Array I

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 3314](https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/description/)

# 🧠 Problem Description
# [Github LeetCode 3314. Construct the Minimum Bitwise Array I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3314.%20Construct%20the%20Minimum%20Bitwise%20Array%20I)

class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans = []
        for x in nums:
            if x == 2:
                ans.append(-1)
            else:
                next_val = x + 1
                lowbit = next_val & -next_val
                ans.append(x - (lowbit >> 1))
                
        return ans