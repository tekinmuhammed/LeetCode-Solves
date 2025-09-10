# 🧩 LeetCode 2116 - Check if a Parentheses String Can Be Valid

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2116](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid)

# 🧠 Problem Description 
# [Github LeetCode 2116 - Check if a Parentheses String Can Be Valid](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2116.%20Check%20if%20a%20Parentheses%20String%20Can%20Be%20Valid)

class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False

        open_count = 0
        for i in range(len(s)):
            if locked[i] == '0' or s[i] == '(':
                open_count += 1
            else:
                open_count -= 1
            if open_count < 0:
                return False
        close_count = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0' or s[i] == ')':
                close_count += 1
            else:
                close_count -= 1
            if close_count < 0:
                return False
        return True