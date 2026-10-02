# 22. Generate Parentheses

**Difficulty:** Medium  
**Problem Link:** [LeetCode 22](https://leetcode.com/problems/generate-parentheses/description/)

# 🧠 Problem Description 
# [Github LeetCode 1111. Maximum Nesting Depth of Two Valid Parentheses Strings](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1111.%20Maximum%20Nesting%20Depth%20of%20Two%20Valid%20Parentheses%20Strings)

class Solution:
    def func(self, result, ch, index, open, close):
        if open == 0 and close == 0:
            result.append("".join(ch))
            return

        if open > 0:
            ch[index] = '('
            self.func(result, ch, index + 1, open - 1, close)

        if close > open:
            ch[index] = ')'
            self.func(result, ch, index + 1, open, close - 1)

    def generateParenthesis(self, n):
        result = []
        ch = [' '] * (2 * n)

        self.func(result, ch, 0, n, n)

        return result