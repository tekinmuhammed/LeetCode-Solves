# 3727. Maximum Alternating Sum of Squares

# 🧠 Problem Description 
# [Github LeetCode 2897. Apply Operations on Array to Maximize Sum of Squares](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/2897.%20Apply%20Operations%20on%20Array%20to%20Maximize%20Sum%20of%20Squares)

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3727](https://leetcode.com/problems/maximum-alternating-sum-of-squares/)
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] *= nums[i]
        nums.sort()
        return -sum(nums[: n // 2]) + sum(nums[n // 2 :])