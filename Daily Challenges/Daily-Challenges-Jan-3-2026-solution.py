# 1411. Number of Ways to Paint N × 3 Grid

# **Difficulty:** Hard  
# **Problem Link:** [LeetCode 1411](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description/)

# 🧠 Problem Description
# [Github LeetCode 1411. Number of Ways to Paint N × 3 Grid](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/1411.%20Number%20of%20Ways%20to%20Paint%20N%20%C3%97%203%20Grid)

class Solution(object):
    def numOfWays(self, n):
        MOD = 10**9 + 7
        
        # For row 1
        typeA = 6  # ABA
        typeB = 6  # ABC
        
        for _ in range(2, n + 1):
            newA = (typeA * 3 + typeB * 2) % MOD
            newB = (typeA * 2 + typeB * 2) % MOD
            typeA, typeB = newA, newB
        
        return (typeA + typeB) % MOD