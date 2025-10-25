# 🏦 LeetCode 1716. Calculate Money in Leetcode Bank  

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 1716](https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/)

# 🧠 Problem Description
# [Github LeetCode 1716. Calculate Money in Leetcode Bank ](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1716.%20Calculate%20Money%20in%20Leetcode%20Bank)

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