# 796. Rotate String 

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 796](https://leetcode.com/problems/rotate-string/description/)

# 🧠 Problem Description
# [Github LeetCode 796. Rotate String](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/796.%20Rotate%20String) 

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        length = len(s)

        # Try all possible rotations of the string 
        for _ in range(length):
            # Perform one rotation 
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False