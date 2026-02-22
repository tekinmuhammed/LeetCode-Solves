# 868. Binary Gap

# **Difficulty:** Easy  
# **Link:** [LeetCode 868](https://leetcode.com/problems/binary-gap/description/)

# 🧠 Problem Description
# [Github LeetCode 868. Binary Gap](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/868.%20Binary%20Gap)

class Solution(object):
    def binaryGap(self, n):
        b = bin(n)[2:]   # binary string
        last = -1
        max_gap = 0

        for i in range(len(b)):
            if b[i] == '1':
                if last != -1:
                    max_gap = max(max_gap, i - last)
                last = i

        return max_gap