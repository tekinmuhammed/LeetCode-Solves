# 2784. Check if Array is Good

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 2784](https://leetcode.com/problems/check-if-array-is-good/description/)

# 🧠 Problem Description
# [Github LeetCode 2784. Check if Array is Good](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2784.%20Check%20if%20Array%20is%20Good) 

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        count = [0] * n
        for a in nums:
            if a >= n:
                return False
            if a < n - 1 and count[a] > 0:
                return False
            if a == n - 1 and count[a] > 1:
                return False
            count[a] += 1
        return True