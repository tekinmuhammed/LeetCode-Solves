# 3524. Find X Value of Array I

# **Difficulty:** Medium 
# **Problem Link:** [LeetCode 3524](https://leetcode.com/problems/find-x-value-of-array-i/description/)

# 🧠 Problem Description
# [Github LeetCode 3524. Find X Value of Array I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3524.%20Find%20X%20Value%20of%20Array%20I)

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [0] * k
        # Initial state: no elements have been processed, so no non-empty subarray exists.
        dp = [0] * k

        for i in range(n):
            ndp = [0] * k  # Current state (rolling array).

            ndp[nums[i] % k] += 1

            for r in range(k):
                ndp[(r * nums[i]) % k] += dp[r]

            dp = ndp  # Update the state.

            # Accumulate the answer.
            for r in range(k):
                result[r] += dp[r]
        return result