# 3330. Find the Original Typed String I

# **Difficulty:** Easy  
# **Link:** [LeetCode 3330](https://leetcode.com/problems/find-the-original-typed-string-i)

# 🧠 Problem Description 
# [Github LeetCode 3330. Find the Original Typed String I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3330.%20Find%20the%20Original%20Typed%20String%20I)

class Solution:
    def possibleStringCount(self, word: str) -> int:
        n, ans = len(word), 1
        for i in range(1, n):
            if word[i - 1] == word[i]:
                ans += 1
        return ans