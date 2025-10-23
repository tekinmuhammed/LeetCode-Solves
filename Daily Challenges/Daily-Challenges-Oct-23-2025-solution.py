# 3461. Check If Digits Are Equal in String After Operations I

# **Problem Link:** [LeetCode 3461](https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/)  
# **Difficulty:** Easy

# 🧠 Problem Description
# [Github LeetCode 3461. Check If Digits Are Equal in String After Operations I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3461.%20Check%20If%20Digits%20Are%20Equal%20in%20String%20After%20Operations%20I)

class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while len(s) > 2:
            new_s = []
            for i in range(len(s) - 1):
                new_s.append(str((int(s[i]) + int(s[i + 1])) % 10))
            s = "".join(new_s)
        
        return s[0] == s[1]