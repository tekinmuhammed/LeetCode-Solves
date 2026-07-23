# 3513. Number of Unique XOR Triplets I

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 3513](https://leetcode.com/problems/number-of-unique-xor-triplets-i/description/)
     
# 🧠 Problem Description
# [Github LeetCode 3513. Number of Unique XOR Triplets I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3513.%20Number%20of%20Unique%20XOR%20Triplets%20I)

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        ans = 1
        while ans <= n:
            ans <<= 1
        return ans