# 🔐 LeetCode 1400 - Construct K Palindrome Strings

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1400](https://leetcode.com/problems/construct-k-palindrome-strings)

# 🧠 Problem Description 
# [Github LeetCode 1400 - Construct K Palindrome Strings](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1400.%20Construct%20K%20Palindrome%20Strings)

from collections import Counter

class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if k > len(s):
            return False
        
        char_counts = Counter(s)
        odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)
        return odd_count <= k