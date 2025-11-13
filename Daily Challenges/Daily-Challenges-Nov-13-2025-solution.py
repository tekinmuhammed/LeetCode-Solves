# 💡 LeetCode 3228 – Maximum Number of Operations to Move Ones to the End

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 3228](https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/description/)

# 🧠 Problem Description 
# [Github LeetCode 3228 – Maximum Number of Operations to Move Ones to the End](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3228.%20Maximum%20Number%20of%20Operations%20to%20Move%20Ones%20to%20the%20End)

class Solution:
    def maxOperations(self, s: str) -> int:
        count_one = 0
        ans = 0
        i = 0
        while i < len(s):
            if s[i] == "0":
                while i + 1 < len(s) and s[i + 1] == "0":
                    i += 1
                ans += count_one
            else:
                count_one += 1
            i += 1
        return ans