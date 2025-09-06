# 🟨 LeetCode 1957 - Delete Characters to Make Fancy String

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 1957](https://leetcode.com/problems/delete-characters-to-make-fancy-string/)

# 🧠 Problem Description
# [Github 1957. Delete Characters to Make Fancy String](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1957.%20Delete%20Characters%20to%20Make%20Fancy%20String)

class Solution(object):
    def makeFancyString(self, s):
        result = []

        for char in s:
            if len(result) < 2 or not (result[-1] == result[-2] == char):
                result.append(char)
        return ''.join(result)
solution = Solution()
s = "leeetcode"
print(solution.makeFancyString(s))