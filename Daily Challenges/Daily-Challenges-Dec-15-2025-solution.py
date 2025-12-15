# 2110. Number of Smooth Descent Periods of a Stock

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 2110](https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/description/)

# 🧠 Problem Description
# [Github LeetCode 2110. Number of Smooth Descent Periods of a Stock](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2110.%20Number%20of%20Smooth%20Descent%20Periods%20of%20a%20Stock)

class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 1        # at least one period (first day)
        length = 1       # current smooth descent length

        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                length += 1
            else:
                length = 1
            total += length

        return total