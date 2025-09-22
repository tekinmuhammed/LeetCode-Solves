# 🎨 LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 2379](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks)

# 🧠 Problem Description
# [Github LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2379.%20Minimum%20Recolors%20to%20Get%20K%20Consecutive%20Black%20Blocks)

class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        min_recolor = blocks[:k].count('W')
        current_recolor = min_recolor
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current_recolor -= 1
            if blocks[i] == 'W':
                current_recolor += 1
            min_recolor = min(min_recolor, current_recolor)
        return min_recolor