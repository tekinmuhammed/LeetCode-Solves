# 3498. Reverse Degree of a String

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 3498](https://leetcode.com/problems/reverse-degree-of-a-string/description/)

# 🧠 Problem Description
# [Github LeetCode 3498. Reverse Degree of a String](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3498.%20Reverse%20Degree%20of%20a%20String)

class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, ch in enumerate(s, start=1):
            ans += (26 - (ord(ch) - ord("a"))) * i
        return ans