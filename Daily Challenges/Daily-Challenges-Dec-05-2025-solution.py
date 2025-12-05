# 3432. Count Partitions with Even Sum Difference

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 3423](https://leetcode.com/problems/count-partitions-with-even-sum-difference/description/)  

# 🧠 Problem Description
# [Github LeetCode 3432. Count Partitions with Even Sum Difference](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3432.%20Count%20Partitions%20with%20Even%20Sum%20Difference)

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        return len(nums) - 1 if totalSum % 2 == 0 else 0