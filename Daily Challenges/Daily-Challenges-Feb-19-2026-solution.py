# 696. Count Binary Substrings

# **Difficulty:** Easy  
# **Link:** [LeetCode 696](https://leetcode.com/problems/count-binary-substrings/description/)

# 🧠 Problem Description
# [Github LeetCode 696. Count Binary Substrings](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/696.%20Count%20Binary%20Substrings)

class Solution(object):
    def countBinarySubstrings(self, s):
        prev = 0
        curr = 1
        result = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                result += min(prev, curr)
                prev = curr
                curr = 1

        result += min(prev, curr)
        return result