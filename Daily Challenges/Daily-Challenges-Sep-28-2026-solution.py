
# 🧠 Problem Description 
# [Github LeetCode 1190. Reverse Substrings Between Each Pair of Parentheses](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1190.%20Reverse%20Substrings%20Between%20Each%20Pair%20of%20Parentheses)
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