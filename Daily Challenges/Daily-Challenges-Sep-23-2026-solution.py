# 1658. Minimum Operations to Reduce X to Zero

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1658](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/)

# 🧠 Problem Description
# [Github LeetCode 1658. Minimum Operations to Reduce X to Zero](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1658.%20Minimum%20Operations%20to%20Reduce%20X%20to%20Zero)

class Solution:
    def minOperations(self, A: List[int], x: int) -> int:
        k = sum(A) - x
        if k < 0: return -1 
        best = -1
        
        s = i = 0
        
        for j, num in enumerate(A):
            s += num
            while s > k:
                s -= A[i]
                i += 1  
            if s == k:
                best = max(best, j - i + 1)

        return -1 if best < 0 else len(A) - best
