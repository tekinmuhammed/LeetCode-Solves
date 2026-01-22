## 3507. Minimum Pair Removal to Sort Array I

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 3507](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description/)

# 🧠 Problem Description
# [Github LeetCode 3507. Minimum Pair Removal to Sort Array I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3507.%20Minimum%20Pair%20Removal%20to%20Sort%20Array%20I)

class Solution(object):
    def minimumPairRemoval(self, nums):
        ops = 0

        def is_sorted(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True

        while not is_sorted(nums):
            min_sum = float('inf')
            idx = 0

            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            nums = nums[:idx] + [min_sum] + nums[idx + 2:]
            ops += 1

        return ops