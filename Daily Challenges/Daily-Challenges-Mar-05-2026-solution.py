# 1758. Minimum Changes To Make Alternating Binary String

# 🧠 Problem Description
# [Github LeetCode 1582. Special Positions in a Binary Matrix](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1582.%20Special%20Positions%20in%20a%20Binary%20Matrix)

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1758](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/)
class Solution(object):
    def minOperations(self, s):
        change1 = 0  # pattern starting with '0' -> 010101...
        change2 = 0  # pattern starting with '1' -> 101010...
        
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    change1 += 1
                if s[i] != '1':
                    change2 += 1
            else:
                if s[i] != '1':
                    change1 += 1
                if s[i] != '0':
                    change2 += 1
        
        return min(change1, change2)