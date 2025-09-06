# 🟨 LeetCode 1652 - Defuse the Bomb

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 1652](https://leetcode.com/problems/defuse-the-bomb/)

# 🧠 Problem Description
# [Github LeetCode 1652 - Defuse the Bomb](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1652.%20Defuse%20the%20Bomb)

class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        if k == 0:
            return [0] * n
        result = [0] * n
        if k > 0:
            for i in range(n):
                result[i] = sum(code[(i + j) % n] for j in range(1, k + 1))
        else:
            for i in range(n):
                result[i] = sum(code[(i + j) % n] for j in range(k, 0))
        return result
        