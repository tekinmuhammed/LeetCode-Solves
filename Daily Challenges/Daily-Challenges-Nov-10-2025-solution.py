# ⚙️ 3542. Minimum Operations to Convert All Elements to Zero

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 3542](https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/description/)

# 🧠 Problem Description 
# [Github LeetCode 3542. Minimum Operations to Convert All Elements to Zero](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3542.%20Minimum%20Operations%20to%20Convert%20All%20Elements%20to%20Zero)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = []
        res = 0
        for a in nums:
            while s and s[-1] > a:
                s.pop()
            if a == 0:
                continue
            if not s or s[-1] < a:
                res += 1
                s.append(a)
        return res