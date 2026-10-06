# 921. Minimum Add to Make Parentheses Valid

**Difficulty:** Medium
**Problem Link:** [LeetCode 921](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/)
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        min_adds_required = 0

        for c in s:
            if c == "(":
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    min_adds_required += 1

        # Add the remaining open brackets as closing brackets would be required.
        return min_adds_required + open_brackets