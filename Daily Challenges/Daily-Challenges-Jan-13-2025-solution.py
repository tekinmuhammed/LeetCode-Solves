# ✂️ LeetCode 3223 - Minimum Length of String After Operations

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 3223](https://leetcode.com/problems/minimum-length-of-string-after-operations/)

# 🧠 Problem Description 
# [Github LeetCode 3223 - Minimum Length of String After Operations](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3223.%20Minimum%20Length%20of%20String%20After%20Operations)

class Solution:
    def minimumLength(self, s: str) -> int:
        f = collections.Counter(s)
        for k in f.keys():
            while f[k] >= 3:
                f[k] -= 2
        return sum(f.values())