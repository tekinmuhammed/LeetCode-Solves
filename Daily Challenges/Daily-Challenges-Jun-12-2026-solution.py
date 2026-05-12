# 1665. Minimum Initial Energy to Finish Tasks

# **Difficulty:** Hard  
# **Problem Link:** [LeetCode 1665](https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/description/)

# 🧠 Problem Description
# [Github LeetCode 1665. Minimum Initial Energy to Finish Tasks](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/1665.%20Minimum%20Initial%20Energy%20to%20Finish%20Tasks) 

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0])
        ans = 0
        for task in tasks:
            ans = max(ans + task[0], task[1])
        return ans