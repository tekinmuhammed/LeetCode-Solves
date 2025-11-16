# 1513. Number of Substrings With Only 1s — README

# **Difficulty:** Medium  
# **Link:** [LeetCode 1513](https://leetcode.com/problems/number-of-substrings-with-only-1s/description/)  

# 🧠 Problem Description 
# [Github LeetCode 1513. Number of Substrings With Only 1s](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1513.%20Number%20of%20Substrings%20With%20Only%201s)

class Solution:
    def numSub(self, s: str) -> int:
        total, consecutive = 0, 0
        length = len(s)
        for i in range(length):
            if s[i] == "0":
                total += consecutive * (consecutive + 1) // 2
                consecutive = 0
            else:
                consecutive += 1

        total += consecutive * (consecutive + 1) // 2
        total %= 10**9 + 7
        return total