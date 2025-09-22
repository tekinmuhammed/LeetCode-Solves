# 🎨 LeetCode 3208 - Alternating Groups II

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 3208](https://leetcode.com/problems/alternating-groups-ii)

# 🧠 Problem Description
# [Github LeetCode 3208 - Alternating Groups II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3208.%20Alternating%20Groups%20II)

class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        n = len(colors)
        count = 0
        alternating_count = 0
        for i in range(k - 1):
            if colors[i] != colors[i + 1]:
                alternating_count += 1
        if alternating_count == k - 1:
            count += 1
        for i in range(1, n):
            prev_index = (i - 1) % n
            new_index = (i + k - 2) % n
            if colors[prev_index] != colors[(prev_index + 1) % n]:
                alternating_count -= 1
            if colors[new_index] != colors[(new_index + 1) % n]:
                alternating_count += 1
            if alternating_count == k - 1:
                count += 1
        return count