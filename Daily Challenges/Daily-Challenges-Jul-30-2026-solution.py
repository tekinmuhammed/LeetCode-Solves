# 3014. Minimum Number of Pushes to Type Word I

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 3014](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description/)

# 🧠 Problem Description
# [Github LeetCode 3014. Minimum Number of Pushes to Type Word I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3014.%20Minimum%20Number%20of%20Pushes%20to%20Type%20Word%20I)
 
class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(i // 8 + 1 for i in range(len(word)))