# 3761. Minimum Absolute Distance Between Mirror Pairs

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 3761](https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/description/)

# 🧠 Problem Description
# [Github LeetCode 3761. Minimum Absolute Distance Between Mirror Pairs](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3761.%20Minimum%20Absolute%20Distance%20Between%20Mirror%20Pairs) 

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        prev = dict()
        ans = inf
        for i, num in enumerate(nums):
            if num in prev:
                ans = min(ans, i - prev[num])
            prev[int(str(num)[::-1])] = i
        return -1 if ans == inf else ans