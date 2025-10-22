# 3186. Maximum Total Damage With Spell Casting

## Difficulty: Medium
## Problem Link: [LeetCode - 3186. Maximum Total Damage With Spell Casting](https://leetcode.com/problems/maximum-total-damage-with-spell-casting/)  

# 🧠 Problem Description
# [Github LeetCode 3186. Maximum Total Damage With Spell Casting](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2221.%20Find%20Triangular%20Sum%20of%20an%20Array)

from collections import Counter

class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        count = Counter(power)
        unique = sorted(count.keys())

        n = len(unique)
        dp = [0] * n

        for i in range(n):
            damage = unique[i] * count[unique[i]]
            
            # Eğer bu hasar değeri öncekiyle 3 veya daha fazla fark ediyorsa, çakışmaz
            j = i - 1
            while j >= 0 and unique[i] - unique[j] <= 2:
                j -= 1
            
            if i == 0:
                dp[i] = damage
            else:
                dp[i] = max(dp[i-1], damage + (dp[j] if j >= 0 else 0))

        return dp[-1]