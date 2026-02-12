# 3713. Longest Balanced Substring I

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 3713](https://leetcode.com/problems/longest-balanced-substring-i/description/)

# 🧠 Problem Description
# [Github LeetCode 3713. Longest Balanced Substring I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3713.%20Longest%20Balanced%20Substring%20I)

class Solution(object):
    def longestBalanced(self, s):
        n = len(s)
        ans = 0
        
        for i in range(n):
            freq = [0] * 26
            
            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                freq[idx] += 1
                
                min_freq = float('inf')
                max_freq = 0
                
                for f in freq:
                    if f > 0:
                        min_freq = min(min_freq, f)
                        max_freq = max(max_freq, f)
                
                if min_freq == max_freq:
                    ans = max(ans, j - i + 1)
        
        return ans