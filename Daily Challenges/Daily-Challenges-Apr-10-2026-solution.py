# 3740. Minimum Distance Between Three Equal Elements I

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 3740](https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/description/)

# 🧠 Problem Description
# [Github LeetCode 3740. Minimum Distance Between Three Equal Elements I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3740.%20Minimum%20Distance%20Between%20Three%20Equal%20Elements%20I) 

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[i] != nums[j]:
                    continue
                for k in range(j + 1, n):
                    if nums[j] == nums[k]:
                        ans = min(ans, k - i)
                        break

        return -1 if ans == n + 1 else ans * 2