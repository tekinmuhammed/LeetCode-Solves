# 🟨 LeetCode 2696 - Minimum String Length After Removing Substrings

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 2696](https://leetcode.com/problems/minimum-string-length-after-removing-substrings)

# 🧠 Problem Description
# [Github LeetCode 2696 - Minimum String Length After Removing Substrings](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2696.%20Minimum%20String%20Length%20After%20Removing%20Substrings)

class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for char in s:
            stack.append(char)
            if len(stack) >= 2 and (stack[-2] + stack[-1] == "AB" or stack[-2] + stack[-1] == "CD"):
                stack.pop()
                stack.pop()
        return len(stack)