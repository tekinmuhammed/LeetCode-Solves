# 2897. Apply Operations on Array to Maximize Sum of Squares

# **Difficulty:** Medium 
# **Problem Link:** [LeetCode 2897](https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/description/)

# 🧠 Problem Description 
# [Github LeetCode 2897. Apply Operations on Array to Maximize Sum of Squares](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/2897.%20Apply%20Operations%20on%20Array%20to%20Maximize%20Sum%20of%20Squares)

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        cnt = [0] * 30

        # Count the number of 1 bits at each position
        for num in nums:
            for i in range(30):
                if num & (1 << i):
                    cnt[i] += 1

        res = 0
        for _ in range(k):
            cur = 0
            # Construct the current number from the most significant bit to the least significant bit
            for j in range(29, -1, -1):
                if cnt[j] > 0:
                    cur |= 1 << j
                    cnt[j] -= 1
            res = (res + cur * cur) % MOD

        return res