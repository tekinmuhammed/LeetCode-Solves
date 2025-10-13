# 2106. Maximum Fruits Harvested After at Most K Steps

# **Difficulty:** Hard  
# **Problem Link:** [LeetCode 2106](https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps)

# 🧠 Problem Description 
# [Github LeetCode 2106. Maximum Fruits Harvested After at Most K Steps](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/2106.%20Maximum%20Fruits%20Harvested%20After%20at%20Most%20K%20Steps)

class Solution:
    def maxTotalFruits(
        self, fruits: List[List[int]], startPos: int, k: int
    ) -> int:
        n = len(fruits)
        sum_ = [0] * (n + 1)
        indices = [0] * n

        for i in range(n):
            sum_[i + 1] = sum_[i] + fruits[i][1]
            indices[i] = fruits[i][0]

        ans = 0
        for x in range(k // 2 + 1):
            # move left x steps, then right (k - 2x) steps
            y = k - 2 * x
            left = startPos - x
            right = startPos + y
            start = bisect_left(indices, left)
            end = bisect_right(indices, right)
            ans = max(ans, sum_[end] - sum_[start])

            # move right x steps, then left (k - 2x) steps
            y = k - 2 * x
            left = startPos - y
            right = startPos + x
            start = bisect_left(indices, left)
            end = bisect_right(indices, right)
            ans = max(ans, sum_[end] - sum_[start])

        return ans