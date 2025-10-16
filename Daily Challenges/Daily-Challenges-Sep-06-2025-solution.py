# 3495. Minimum Operations to Make Array Elements Zero

# **Difficulty:** Hard  
# **Link:** [LeetCode 3495](https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/)

# 🧠 Problem Description 
# [Github LeetCode 3495. Minimum Operations to Make Array Elements Zero](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/3495.%20Minimum%20Operations%20to%20Make%20Array%20Elements%20Zero)

class Solution:
    def get(self, num: int) -> int:
        i = 1
        base = 1
        cnt = 0
        while base <= num:
            cnt += ((i + 1) // 2) * (min(base * 2 - 1, num) - base + 1)
            i += 1
            base *= 2
        return cnt

    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0
        for q in queries:
            res += (self.get(q[1]) - self.get(q[0] - 1) + 1) // 2
        return res