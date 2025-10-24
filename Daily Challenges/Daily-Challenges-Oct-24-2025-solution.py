# 🧩 LeetCode 2048. Next Greater Numerically Balanced Number

# **Difficulty:** Medium
# **Link:** [LeetCode 2048](https://leetcode.com/problems/next-greater-numerically-balanced-number/description/)  

# 🧠 Problem Description
# [Github LeetCode 2048. Next Greater Numerically Balanced Number](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2048.%20Next%20Greater%20Numerically%20Balanced%20Number)

class Solution:
    
    def isBalance(self, num: int) -> bool:
        count = [0] * 10
        temp_num = num
        
        while temp_num > 0:
            digit = temp_num % 10
            if digit == 0:
                return False
            
            count[digit] += 1
            temp_num //= 10
        for d in range(1, 10):
            if count[d] > 0 and count[d] != d:
                return False
                
        return True

    def nextBeautifulNumber(self, n: int) -> int:
        current_num = n + 1
        while True:
            if self.isBalance(current_num):
                return current_num
            current_num += 1