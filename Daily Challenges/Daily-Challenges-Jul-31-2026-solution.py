# 3016. Minimum Number of Pushes to Type Word II

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 3016](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/)

# 🧠 Problem Description
# [Github LeetCode 3016. Minimum Number of Pushes to Type Word II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3016.%20Minimum%20Number%20of%20Pushes%20to%20Type%20Word%20II)

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Frequency list to store count of each letter
        frequency = [0] * 26

        # Count occurrences of each letter
        for c in word:
            frequency[ord(c) - ord("a")] += 1
        # Sort frequencies in descending order
        frequency.sort(reverse=True)

        total_pushes = 0

        # Calculate total number of presses
        for i in range(26):
            if frequency[i] == 0:
                break
            total_pushes += (i // 8 + 1) * frequency[i]

        return total_pushes