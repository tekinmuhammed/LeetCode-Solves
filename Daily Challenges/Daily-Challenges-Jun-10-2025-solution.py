# 3442. Maximum Difference Between Even and Odd Frequency I

# **Problem Link:** [LeetCode 3442](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/)  
# **Difficulty:** Easy

# 🧠 Problem Description 
# [Github  LeetCode 3442. Maximum Difference Between Even and Odd Frequency I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3442.%20Maximum%20Difference%20Between%20Even%20and%20Odd%20Frequency%20I)

from collections import Counter

class Solution(object):

    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)
        max_diff = float('-inf')

        odd_freq = []
        even_freq = []

        for count in freq.values():
            if count % 2 == 0:
                even_freq.append(count)
            else:
                odd_freq.append(count)

        for odd in odd_freq:
            for even in even_freq:
                max_diff = max(max_diff, odd - even)
        return max_diff