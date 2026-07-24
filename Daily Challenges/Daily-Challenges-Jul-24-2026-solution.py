     
# 🧠 Problem Description
# [Github LeetCode 3513. Number of Unique XOR Triplets I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3513.%20Number%20of%20Unique%20XOR%20Triplets%20I)

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