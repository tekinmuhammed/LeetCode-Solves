# 1306. Jump Game III

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 1306](https://leetcode.com/problems/jump-game-iii/description/)

# 🧠 Problem Description
# [Github LeetCode 1306. Jump Game III](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1306.%20Jump%20Game%20III) 

class Solution(object):
    def canReach(self, arr, start):
        visited = set()
        stack = [start]

        while stack:
            i = stack.pop()

            if i < 0 or i >= len(arr) or i in visited:
                continue

            if arr[i] == 0:
                return True

            visited.add(i)

            stack.append(i + arr[i])
            stack.append(i - arr[i])

        return False