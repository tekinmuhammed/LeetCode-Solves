
# 🧠 Problem Description 
# [Github LeetCode 1111. Maximum Nesting Depth of Two Valid Parentheses Strings](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1111.%20Maximum%20Nesting%20Depth%20of%20Two%20Valid%20Parentheses%20Strings)
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