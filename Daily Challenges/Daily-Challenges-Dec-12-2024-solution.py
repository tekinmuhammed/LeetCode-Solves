# 🟨 LeetCode 2558 - Take Gifts From the Richest Pile

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 2558](https://leetcode.com/problems/take-gifts-from-the-richest-pile/)

# 🧠 Problem Description 
# [Github LeetCode 2558 - Take Gifts From the Richest Pile](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2558.%20Take%20Gifts%20From%20the%20Richest%20Pile)

import math

class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        for _ in range(k):
            max_index = gifts.index(max(gifts))
            gifts[max_index] = int(math.floor(math.sqrt(gifts[max_index])))
        return sum(gifts)