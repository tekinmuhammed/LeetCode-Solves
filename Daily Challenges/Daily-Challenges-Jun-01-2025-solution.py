# 🍬 LeetCode 2929 - Distribute Candies Among Children II

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2929](https://leetcode.com/problems/distribute-candies-among-children-ii)

# 🧠 Problem Description 
# [Github LeetCode 2929 - Distribute Candies Among Children II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2929.%20Distribute%20Candies%20Among%20Children%20II)

class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        def count_unbounded(k):
            return (k + 2) * (k + 1) // 2 if k >= 0 else 0
        
        total = count_unbounded(n)
        over1 = count_unbounded(n - (limit + 1)) * 3
        over2 = count_unbounded(n - 2 * (limit + 1)) * 3
        over3 = count_unbounded(n - 3 * (limit + 1))

        return total - over1 + over2 - over3