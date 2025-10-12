# 1957. Delete Characters to Make Fancy String

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 1957](https://leetcode.com/problems/delete-characters-to-make-fancy-string/)

# 🧠 Problem Description 
# [Github LeetCode 3136. Valid Word](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1957.%20Delete%20Characters%20to%20Make%20Fancy%20String%20II)

class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for c in s:
            if len(res) >= 2 and res[-1] == res[-2] == c:
                continue
            res.append(c)
        return ''.join(res)