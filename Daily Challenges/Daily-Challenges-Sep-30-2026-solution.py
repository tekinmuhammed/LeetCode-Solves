# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1111](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/description/)
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