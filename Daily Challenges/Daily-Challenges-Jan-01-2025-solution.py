# 🟩 LeetCode 1422 - Maximum Score After Splitting a String

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 1422](https://leetcode.com/problems/maximum-score-after-splitting-a-string)

# 🧠 Problem Description 
# [Github LeetCode 1422 - Maximum Score After Splitting a String](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1422.%20Maximum%20Score%20After%20Splitting%20a%20String)

class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_score = 0
        for i in range(1, len(s)):
            left_zeros = s[:i].count('0')
            right_ones = s[i:].count('1')
            score = left_zeros + right_ones
            max_score = max(max_score, score)
        return max_score