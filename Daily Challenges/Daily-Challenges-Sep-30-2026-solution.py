# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 1111](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/description/)

# 🧠 Problem Description 
# [Github LeetCode 1111. Maximum Nesting Depth of Two Valid Parentheses Strings](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1111.%20Maximum%20Nesting%20Depth%20of%20Two%20Valid%20Parentheses%20Strings)

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        d = 0
        for c in seq:
            if c == "(":
                d += 1
                ans.append(d % 2)
            if c == ")":
                ans.append(d % 2)
                d -= 1
        return ans