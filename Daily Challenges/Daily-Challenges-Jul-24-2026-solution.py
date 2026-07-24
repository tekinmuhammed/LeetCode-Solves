# 3514. Number of Unique XOR Triplets II

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 3514](https://leetcode.com/problems/number-of-unique-xor-triplets-ii/description/)

# 🧠 Problem Description
# [Github LeetCode 3514. Number of Unique XOR Triplets II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3514.%20Number%20of%20Unique%20XOR%20Triplets%20II)

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        m = max(nums)
        u = 1
        while u <= m:
            u <<= 1
        s = [False] * u
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                s[nums[i] ^ nums[j]] = True
        t = [False] * u
        for x in range(u):
            if not s[x]:
                continue
            for v in nums:
                t[x ^ v] = True
        return sum(1 for b in t if b)