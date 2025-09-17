# 🔡 LeetCode 3174 - Clear Digits

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 3174](https://leetcode.com/problems/clear-digits)

# 🧠 Problem Description
# [Github LeetCode 3174 - Clear Digits](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3174.%20Clear%20Digits)

class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if char.isdigit():
                if stack and stack[-1].isalpha():
                    stack.pop()
            else:
                stack.append(char)
        return "".join(stack)