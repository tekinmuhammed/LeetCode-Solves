# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 1477](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/description/)

# 🧠 Problem Description
# [Github LeetCode 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1477.%20Find%20Two%20Non-overlapping%20Sub-arrays%20Each%20With%20Target%20Sum)

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        pos = {0: -1}
        n = len(arr)
        s = 0
        ans = n + 1
        min_l = n
        for i, x in enumerate(arr):
            s += x
            if s - target in pos:
                j = pos[s - target]
                length = i - j
                ans = min(ans, length + (n if j == -1 else arr[j]))
                min_l = min(min_l, length)
            arr[i] = min_l
            pos[s] = i
        return -1 if ans == n + 1 else ans