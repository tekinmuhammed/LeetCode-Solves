# 2144. Minimum Cost of Buying Candies With Discount

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 2144](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/)

# 🧠 Problem Description  
# [Github LeetCode 2144. Minimum Cost of Buying Candies With Discount](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2144.%20Minimum%20Cost%20of%20Buying%20Candies%20With%20Discount) 

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(key=lambda x: -x)
        res = 0
        n = len(cost)
        for i in range(n):
            if i % 3 != 2:
                res += cost[i]
        return res