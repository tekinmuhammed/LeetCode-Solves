# 1021. Remove Outermost Parentheses

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 1021](https://leetcode.com/problems/remove-outermost-parentheses/description/)

# 🧠 Problem Description
# [Github LeetCode 1021. Remove Outermost Parentheses](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1021.%20Remove%20Outermost%20Parentheses)

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, stack = [], []
        for c in s:
            if c == ")":
                stack.pop()
            if stack:
                res.append(c)
            if c == "(":
                stack.append(c)
        return "".join(res)