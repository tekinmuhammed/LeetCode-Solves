# 3498. Reverse Degree of a String

**Difficulty:** Easy 
**Problem Link:** [LeetCode 3498](https://leetcode.com/problems/reverse-degree-of-a-string/description/)

class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, ch in enumerate(s, start=1):
            ans += (26 - (ord(ch) - ord("a"))) * i
        return ans