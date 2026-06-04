# 3751. Total Waviness of Numbers in Range I

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 3751](https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/description/)

# 🧠 Problem Description  
# [Github LeetCode 3751. Total Waviness of Numbers in Range I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3751.%20Total%20Waviness%20of%20Numbers%20in%20Range%20I) 

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n: int) -> int:
            s = str(n)
            return sum(
                (a < b > c) or (a > b < c) for a, b, c in zip(s, s[1:], s[2:])
            )

        return sum(waviness(n) for n in range(num1, num2 + 1))