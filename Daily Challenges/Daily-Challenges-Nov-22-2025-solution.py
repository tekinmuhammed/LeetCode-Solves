# 3190. Find Minimum Operations to Make All Elements Divisible by Three

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 3190](https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/)

# 🧠 Problem Description 
# [Github LeetCode 3190. Find Minimum Operations to Make All Elements Divisible by Three](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3190.%20Find%20Minimum%20Operations%20to%20Make%20All%20Elements%20Divisible%20by%20Three)

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        for x in nums:
            if x % 3 != 0:
                operations += 1
        return operations