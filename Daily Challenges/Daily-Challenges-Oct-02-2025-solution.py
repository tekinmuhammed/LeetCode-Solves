# 3100. Water Bottles II  

## Difficulty:  Medium  
## Problem Link:  [LeetCode - 3100. Water Bottles II](https://leetcode.com/problems/water-bottles-ii/)  

# 🧠 Problem Description 
# [Github LeetCode 3100. Water Bottles II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3100.%20Water%20Bottles%20II)

class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            empty -= numExchange
            total += 1
            empty += 1
            numExchange += 1
        
        return total