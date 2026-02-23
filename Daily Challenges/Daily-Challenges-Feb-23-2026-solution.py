# 1461. Check If a String Contains All Binary Codes of Size K

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1461](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/)

# 🧠 Problem Description
# [Github LeetCode 1461. Check If a String Contains All Binary Codes of Size K](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1461.%20Check%20If%20a%20String%20Contains%20All%20Binary%20Codes%20of%20Size%20K)

class Solution(object):
    def hasAllCodes(self, s, k):
        need = 1 << k          # total binary codes
        seen = set()

        num = 0
        mask = need - 1        # keep last k bits

        for i in range(len(s)):
            num = ((num << 1) & mask) | int(s[i])

            if i >= k - 1:
                seen.add(num)
                if len(seen) == need:
                    return True

        return False