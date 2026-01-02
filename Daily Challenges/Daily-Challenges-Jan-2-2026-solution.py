# 961. N-Repeated Element in Size 2N Array

# **Difficulty:** Easy  
# **Link:** [LeetCode 961](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/)

# 🧠 Problem Description
# [Github LeetCode 961. N-Repeated Element in Size 2N Array](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/961.%20N-Repeated%20Element%20in%20Size%202N%20Array)

class Solution(object):
    def repeatedNTimes(self, nums):
        seen = set()
        
        for num in nums:
            if num in seen:
                return num
            seen.add(num)