# 2561. Rearranging Fruits

# **Difficulty:** Hard 
# **Problem Link:** [LeetCode 2561](https://leetcode.com/problems/rearranging-fruits/)

# 🧠 Problem Description
# [Github LeetCode 2561. Rearranging Fruits](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/2561.%20Rearranging%20Fruits)

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = Counter()
        m = float("inf")
        for b1 in basket1:
            freq[b1] += 1
            m = min(m, b1)
        for b2 in basket2:
            freq[b2] -= 1
            m = min(m, b2)

        merge = []
        for k, c in freq.items():
            if c % 2 != 0:
                return -1
            merge.extend([k] * (abs(c) // 2))

        if not merge:
            return 0
        merge.sort()
        return sum(min(2 * m, x) for x in merge[: len(merge) // 2])