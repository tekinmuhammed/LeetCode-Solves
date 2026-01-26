## 1200. Minimum Absolute Difference

# **Difficulty:** Easy
# **Link:** [LeetCode 1200](https://leetcode.com/problems/minimum-absolute-difference/description/)

# 🧠 Problem Description 
# [Github LeetCode 1200. Minimum Absolute Difference](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1200.%20Minimum%20Absolute%20Difference)

class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_diff = float('inf')
        result = []

        # Minimum farkı bul
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            min_diff = min(min_diff, diff)

        # Minimum farka sahip çiftleri topla
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_diff:
                result.append([arr[i], arr[i + 1]])

        return result