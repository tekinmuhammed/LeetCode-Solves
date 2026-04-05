# 657. Robot Return to Origin

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 657](https://leetcode.com/problems/robot-return-to-origin/)

# 🧠 Problem Description
# [Github LeetCode 657. Robot Return to Origin](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/657.%20Robot%20Return%20to%20Origin) 

class Solution(object):
    def judgeCircle(self, moves):
        x = 0
        y = 0
        
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
        
        return x == 0 and y == 0