# 2311. Longest Binary Subsequence Less Than or Equal to K

# **Difficulty:** Medium  
# **Link:** [LeetCode 2311](https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/)

# 🧠 Problem Description 
# [Github LeetCode 2311. Longest Binary Subsequence Less Than or Equal to K](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2311.%20Longest%20Binary%20Subsequence%20Less%20Than%20or%20Equal%20to%20K)

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        N, res, current_num = len(s), s.count('0'), 0
        for i in range(N):
            if s[N - 1 - i] == '1':
                current_num |= 1 << i
                if current_num > k: break
                res += 1
        return res