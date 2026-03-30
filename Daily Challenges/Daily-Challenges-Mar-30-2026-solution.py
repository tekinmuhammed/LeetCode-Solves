









# 2840. Check if Strings Can be Made Equal With Operations II

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2840](https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/)
class Solution(object):
    def checkStrings(self, s1, s2):
        return (
            sorted(s1[::2]) == sorted(s2[::2]) and
            sorted(s1[1::2]) == sorted(s2[1::2])
        )