# 🧩 2975. Maximum Square Area by Removing Fences From a Field

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2975](https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/description/)

# 🧠 Problem Description
# [Github LeetCode 2975. Maximum Square Area by Removing Fences From a Field](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2975.%20Maximum%20Square%20Area%20by%20Removing%20Fences%20From%20a%20Field)

class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        MOD = 10**9 + 7

        # Add fixed boundary fences
        h = sorted([1] + hFences + [m])
        v = sorted([1] + vFences + [n])

        # All possible horizontal gaps
        h_gaps = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_gaps.add(h[j] - h[i])

        # All possible vertical gaps
        v_gaps = set()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                v_gaps.add(v[j] - v[i])

        # Find common gaps
        common = h_gaps & v_gaps
        if not common:
            return -1

        side = max(common)
        return (side * side) % MOD