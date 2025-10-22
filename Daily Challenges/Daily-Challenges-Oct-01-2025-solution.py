# 1518. Water Bottles

# Difficulty: Easy
# Problem Link:  [LeetCode - 1518. Water Bottles](https://leetcode.com/problems/water-bottles/)  

# 🧠 Problem Description 
# [Github LeetCode 1518. Water Bottles](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1518.%20Water%20Bottles)

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            new_full = empty // numExchange
            total += new_full
            empty = empty % numExchange + new_full
        
        return total