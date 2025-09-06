# 🟨 LeetCode 1671 - Minimum Number of Removals to Make Mountain Array

# **Difficulty:** Hard  
# **Problem Link:** [LeetCode 1671](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array)

# 🧠 Problem Description
# [Github LeetCode 1671 - Minimum Number of Removals to Make Mountain Array](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/1671.%20Minimum%20Number%20of%20Removals%20to%20Make%20Mountain%20Array)

class Solution(object):
    def minimumMountainRemovals(self, nums):
        n = len(nums)
        left = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    left[i] = max(left[i], left[j] + 1)
        right = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    right[i] = max(right[i], right[j] + 1)
        max_mountain = 0
        for i in range(1, n - 1):
            if left[i] > 1 and right[i] > 1:
                max_mountain = max(max_mountain, left[i] + right[i] - 1)
        return n - max_mountain