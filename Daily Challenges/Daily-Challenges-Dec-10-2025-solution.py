# 3577. Count the Number of Computer Unlocking Permutations

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 3577](https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/)

# 🧠 Problem Description
# [Github LeetCode 3577. Count the Number of Computer Unlocking Permutations](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3577.%20Count%20the%20Number%20of%20Computer%20Unlocking%20Permutations)

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0

        ans, mod = 1, 10**9 + 7
        for i in range(2, n):
            ans = ans * i % mod
        return ans