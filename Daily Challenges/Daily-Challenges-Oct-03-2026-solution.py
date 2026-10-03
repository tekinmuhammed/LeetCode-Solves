# 32. Longest Valid Parentheses

# **Difficulty:** Hard
# **Problem Link:** [LeetCode 32](https://leetcode.com/problems/longest-valid-parentheses/description/)

# 🧠 Problem Description 
# [Github LeetCode 32. Longest Valid Parentheses](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/32.%20Longest%20Valid%20Parentheses)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, maxi = 0, 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxi = max(maxi, 2 * right)
            elif right > left:
                left = right = 0
        left = right = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxi = max(maxi, 2 * left)
            elif left > right:
                left = right = 0
        return maxi