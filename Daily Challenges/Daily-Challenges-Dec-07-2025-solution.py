# 1523. Count Odd Numbers in an Interval Range

# Difficulty: Easy
# Problem Link  [LeetCode - 1518. Water Bottles](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/)  

# 🧠 Problem Description
# [Github LeetCode 1523. Count Odd Numbers in an Interval Range](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1523.%20Count%20Odd%20Numbers%20in%20an%20Interval%20Range)

class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # If both low and high are even → number of odds is (high - low) // 2
        # Otherwise → (high - low) // 2 + 1
        return ((high - low) // 2) + (1 if low % 2 == 1 or high % 2 == 1 else 0)