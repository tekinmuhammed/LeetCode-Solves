# 1498. Number of Subsequences That Satisfy the Given Sum Condition

# **Difficulty:** Medium  
# **Link:** [LeetCode 1498](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)

# 🧠 Problem Description 
# [Github LeetCode 1498. Number of Subsequences That Satisfy the Given Sum Condition](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1498.%20Number%20of%20Subsequences%20That%20Satisfy%20the%20Given%20Sum%20Condition)

class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        res = 0

        left, right = 0, n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                res += pow2[right - left]
                res %= MOD
                left += 1
            else:
                right -= 1
        return res