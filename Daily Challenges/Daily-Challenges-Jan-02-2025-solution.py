# 🟩 LeetCode 2559 - Count Vowel Strings in Ranges

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2559](https://leetcode.com/problems/count-vowel-strings-in-ranges)

# 🧠 Problem Description 
# [Github LeetCode 2559 - Count Vowel Strings in Ranges](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2559.%20Count%20Vowel%20Strings%20in%20Ranges)

class Solution(object):
    def is_vowel(self, c):
        return c in 'aeiou'

    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(words)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            start = words[i][0]
            end = words[i][-1]
            if self.is_vowel(start) and self.is_vowel(end):
                prefix_sum[i + 1] = 1 + prefix_sum[i]
            else:
                prefix_sum[i + 1] = prefix_sum[i]
        res = []
        for query in queries:
            start, end = query
            count = prefix_sum[end + 1] - prefix_sum[start]
            res.append(count)
        return res