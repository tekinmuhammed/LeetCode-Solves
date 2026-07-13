 # 1291. Sequential Digits 
 
# **Difficulty:** Medium 
# **Problem Link:** [LeetCode 1291](https://leetcode.com/problems/sequential-digits/description/)
 
# 🧠 Problem Description 
# [Github LeetCode 1291. Sequential Digits](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1291.%20Sequential%20Digits)
 
class Solution:
    q = [*range(1, 10)]

    for x in q:
        d = x % 10
        if d < 9:
            q.append(x * 10 + d + 1)

    def sequentialDigits(self, l: int, h: int) -> list[int]:
        return [x for x in self.q if l <= x <= h]