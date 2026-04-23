# 2615. Sum of Distances

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 2615](https://leetcode.com/problems/sum-of-distances/description/)

# 🧠 Problem Description
# [Github LeetCode 2615. Sum of Distances](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2615.%20Sum%20of%20Distances) 

class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        n = len(nums)
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)
        res = [0] * n
        for group in groups.values():
            total = sum(group)
            prefix_total = 0
            sz = len(group)
            for i, idx in enumerate(group):
                res[idx] = total - prefix_total * 2 + idx * (2 * i - sz)
                prefix_total += idx
        return res