# 3653. XOR After Range Multiplication Queries I

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 3653](https://leetcode.com/problems/xor-after-range-multiplication-queries-i/)

# 🧠 Problem Description
# [Github LeetCode 3653. XOR After Range Multiplication Queries I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3653.%20XOR%20After%20Range%20Multiplication%20Queries%20I) 

class Solution:
    MOD = 10**9 + 7

    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % self.MOD

        res = 0
        for x in nums:
            res ^= x

        return res