# 788. Rotated Digits

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 788](https://leetcode.com/problems/rotated-digits/description/)

# 🧠 Problem Description
# [Github LeetCode 788. Rotated Digits](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/788.%20Rotated%20Digits) 

class Solution(object):
    def rotatedDigits(self, n):
        good = 0
        
        for num in range(1, n + 1):
            s = str(num)
            valid = True
            changed = False
            
            for ch in s:
                if ch in '347':
                    valid = False
                    break
                if ch in '2569':
                    changed = True
            
            if valid and changed:
                good += 1
        
        return good