# 🍬 LeetCode 135 - Candy

# **Difficulty:** Hard  
# **Problem Link:** [LeetCode 135](https://leetcode.com/problems/candy)

# 🧠 Problem Description 
# [Github LeetCode 135 - Candy](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/135.%20Candy)

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i+ 1] + 1)
        return sum(candies)