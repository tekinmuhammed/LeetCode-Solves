# 1888. Minimum Number of Flips to Make the Binary String Alternating

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1888](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/)

# 🧠 Problem Description 
# [Github LeetCode 1888. Minimum Number of Flips to Make the Binary String Alternating](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1888.%20Minimum%20Number%20of%20Flips%20to%20Make%20the%20Binary%20String%20Alternating)

class Solution(object):
    def minFlips(self, s):
        n = len(s)
        s = s + s
        
        alt1 = ""
        alt2 = ""
        
        for i in range(2 * n):
            alt1 += "0" if i % 2 == 0 else "1"
            alt2 += "1" if i % 2 == 0 else "0"
        
        diff1 = diff2 = 0
        res = float('inf')
        left = 0
        
        for right in range(2 * n):
            if s[right] != alt1[right]:
                diff1 += 1
            if s[right] != alt2[right]:
                diff2 += 1
            
            if right - left + 1 > n:
                if s[left] != alt1[left]:
                    diff1 -= 1
                if s[left] != alt2[left]:
                    diff2 -= 1
                left += 1
            
            if right - left + 1 == n:
                res = min(res, diff1, diff2)
        
        return res