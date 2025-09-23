# 🔠 LeetCode 2131 - Longest Palindrome by Concatenating Two Letter Words

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2131](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words)

# 🧠 Problem Description 
# [Github LeetCode 2131 - Longest Palindrome by Concatenating Two Letter Words](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2131.%20Longest%20Palindrome%20by%20Concatenating%20Two%20Letter%20Words)

class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from collections import Counter

        count = Counter(words)
        length = 0
        central_used = False

        for word in count:
            rev = word[::-1]
            if word == rev:
                pairs = count[word] // 2
                length += pairs * 4
                if count[word] % 2 == 1 and not central_used:
                    length += 2
                    central_used = True
            else:
                if rev in count:
                    pair_count = min(count[word], count[rev])
                    length += pair_count * 4
                    count[word] = 0
                    count[rev] = 0
        return length