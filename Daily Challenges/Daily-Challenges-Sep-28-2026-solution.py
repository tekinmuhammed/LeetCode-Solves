# 1614. Maximum Nesting Depth of the Parentheses

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 1614](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/)

# 🧠 Problem Description 
# [Github LeetCode 1614. Maximum Nesting Depth of the Parentheses](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1614.%20Maximum%20Nesting%20Depth%20of%20the%20Parentheses)

class Solution:
    def maxDepth(self, s: str) -> int:
        ans, st = 0, []
        for c in s:
            if c == '(':
                st.append(c)
            elif c == ')':
                st.pop()
            ans = max(ans, len(st))
        return ans