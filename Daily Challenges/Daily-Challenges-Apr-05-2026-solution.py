
# 🧠 Problem Description
# [Github LeetCode 2075. Decode the Slanted Ciphertext](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2075.%20Decode%20the%20Slanted%20Ciphertext) 
# 657. Robot Return to Origin

**Difficulty:** Easy  
**Problem Link:** [LeetCode 657](https://leetcode.com/problems/robot-return-to-origin/)
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