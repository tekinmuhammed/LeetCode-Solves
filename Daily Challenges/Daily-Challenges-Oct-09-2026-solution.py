# 1541. Minimum Insertions to Balance a Parentheses String

# **Difficulty:** Medium 
# **Problem Link:** [LeetCode 1541](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description/)

# 🧠 Problem Description 
# [Github LeetCode 1541. Minimum Insertions to Balance a Parentheses Strin](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1541.%20Minimum%20Insertions%20to%20Balance%20a%20Parentheses%20String)
class Solution:
    def minInsertions(self, s: str) -> int:
        length = len(s)
        insertions = left_count = index = 0

        while index < length:
            if s[index] == "(":
                left_count += 1
                index += 1
            else:
                if left_count > 0:
                    left_count -= 1
                else:
                    insertions += 1
                if index < length - 1 and s[index + 1] == ")":
                    index += 2
                else:
                    insertions += 1
                    index += 1

        insertions += left_count * 2
        return insertions