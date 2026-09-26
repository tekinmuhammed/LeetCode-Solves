# 1807. Evaluate the Bracket Pairs of a String

**Difficulty:** Medium 
**Problem Link:** [LeetCode 1807](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/description/)
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