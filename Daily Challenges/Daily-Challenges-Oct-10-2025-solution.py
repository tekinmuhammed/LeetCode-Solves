# 3147. Taking Maximum Energy From the Mystic Dungeon

## Difficulty: Medium
## Problem Link: [LeetCode - 3147. Taking Maximum Energy From the Mystic Dungeon](https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/)  

# 🧠 Problem Description
# [Github LeetCode 3147. Taking Maximum Energy From the Mystic Dungeon](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3147.%20Taking%20Maximum%20Energy%20From%20the%20Mystic%20Dungeon)

class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(energy)
        dp = [0] * n
        
        # dp[i] = i'den başlayıp i+k, i+2k ... ilerleyerek toplanabilecek maksimum enerji
        # Son elemanlardan başa doğru hesaplanır.
        for i in range(n - 1, -1, -1):
            if i + k < n:
                dp[i] = energy[i] + dp[i + k]
            else:
                dp[i] = energy[i]
        
        # En yüksek enerjiyi döndür
        return max(dp)