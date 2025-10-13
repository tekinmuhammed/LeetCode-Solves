# LeetCode 3363 - Find the Maximum Number of Fruits Collected

# **Difficulty:** Hard
# **Problem Link:** [LeetCode 3363](https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/description/)

# 🧠 Problem Description 
# [Github LeetCode 3363 - Find the Maximum Number of Fruits Collected](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/3363.%20Find%20the%20Maximum%20Number%20of%20Fruits%20Collected)

class Solution:
    def maxCollectedFruits(self, fruits):
        n = len(fruits)
        ans = sum(fruits[i][i] for i in range(n))

        def dp():
            prev = [float("-inf")] * n
            curr = [float("-inf")] * n
            prev[n - 1] = fruits[0][n - 1]
            for i in range(1, n - 1):
                for j in range(max(n - 1 - i, i + 1), n):
                    best = prev[j]
                    if j - 1 >= 0:
                        best = max(best, prev[j - 1])
                    if j + 1 < n:
                        best = max(best, prev[j + 1])
                    curr[j] = best + fruits[i][j]
                prev, curr = curr, prev
            return prev[n - 1]

        ans += dp()

        for i in range(n):
            for j in range(i):
                fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]

        ans += dp()
        return ans