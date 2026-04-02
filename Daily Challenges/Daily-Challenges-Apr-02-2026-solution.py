# 3418. Maximum Amount of Money Robot Can Earn
 
# **Difficulty:** Medium
# **Problem Link:** [LeetCode 3418](https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/)
 
# 🧠 Problem Description
# [Github LeetCode 3418. Maximum Amount of Money Robot Can Earn](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3418.%20Maximum%20Amount%20of%20Money%20Robot%20Can%20Earn) 

class Solution(object):
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])
        
        # dp[i][j][k]: max coins at (i,j) using k neutralizations
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # start
        for k in range(3):
            if coins[0][0] < 0 and k > 0:
                dp[0][0][k] = 0
            else:
                dp[0][0][k] = coins[0][0]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                for k in range(3):
                    val = coins[i][j]
                    
                    # from top
                    if i > 0:
                        # normal take
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + val)
                        
                        # neutralize
                        if val < 0 and k > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1])
                    
                    # from left
                    if j > 0:
                        # normal take
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + val)
                        
                        # neutralize
                        if val < 0 and k > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1])
        
        return max(dp[m-1][n-1])