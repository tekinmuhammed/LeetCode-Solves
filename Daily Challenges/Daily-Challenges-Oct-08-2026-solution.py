
# 🧠 Problem Description 
# [Github LeetCode 921. Minimum Add to Make Parentheses Valid](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/921.%20Minimum%20Add%20to%20Make%20Parentheses%20Valid)
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