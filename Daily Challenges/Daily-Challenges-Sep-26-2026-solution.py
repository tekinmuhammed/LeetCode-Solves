# 1807. Evaluate the Bracket Pairs of a String

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 1807](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/description/)

# 🧠 Problem Description
# [Github LeetCode 1807. Evaluate the Bracket Pairs of a String](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1807.%20Evaluate%20the%20Bracket%20Pairs%20of%20a%20String)

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = dict(knowledge)
        ans, start = [], -1
        for i, c in enumerate(s):
            if c == "(":
                start = i
            elif c == ")":
                ans.append(d.get(s[start + 1 : i], "?"))
                start = -1
            elif start < 0:
                ans.append(c)
        return "".join(ans)