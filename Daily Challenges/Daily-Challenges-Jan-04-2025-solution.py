# 🟨 LeetCode 1930 - Unique Length-3 Palindromic Subsequences

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1930](https://leetcode.com/problems/unique-length-3-palindromic-subsequences)

# 🧠 Problem Description 
# [Github LeetCode 1930 - Unique Length-3 Palindromic Subsequences](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1930.%20Unique%20Length-3%20Palindromic%20Subsequences)

class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique_palindromes = set()
        for char in set(s):
            first_index = s.find(char)
            last_index = s.rfind(char)
            if last_index - first_index > 1:
                middle_characters = set(s[first_index + 1:last_index])
                for mid_char in middle_characters:
                    unique_palindromes.add(char + mid_char + char)
        return len(unique_palindromes)