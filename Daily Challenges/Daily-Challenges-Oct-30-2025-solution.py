# 🔢 LeetCode 1526 — Minimum Number of Increments on Subarrays to Form a Target Array

# **Difficulty:** Hard  
# **Problem Link:** [LeetCode 1526](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/description/)

# 🧠 Problem Description
# [Github LeetCode 1526 — Minimum Number of Increments on Subarrays to Form a Target Array](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/1526.%20Minimum%20Number%20of%20Increments%20on%20Subarrays%20to%20Form%20a%20Target%20Array)

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        ans = target[0]
        for i in range(1, n):
            ans += max(target[i] - target[i - 1], 0)
        return ans