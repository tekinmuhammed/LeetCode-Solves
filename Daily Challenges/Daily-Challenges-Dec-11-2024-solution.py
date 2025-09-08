# 🔁 LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2981](https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i)

# 🧠 Problem Description 
# [Github LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2981.%20Find%20Longest%20Special%20Substring%20That%20Occurs%20Thrice%20I)

class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_length = -1
        for length in range(1, n + 1):
            count = {}
            for i in range(n - length + 1):
                substring = s[i:i + length]
                if len(set(substring)) == 1:
                    count[substring] = count.get(substring, 0) + 1
            for key in count:
                if count[key] >= 3:
                    max_length = max(max_length, length)
        return max_length