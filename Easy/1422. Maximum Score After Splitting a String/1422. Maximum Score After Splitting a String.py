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