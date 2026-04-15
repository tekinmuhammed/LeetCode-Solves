# 2515. Shortest Distance to Target String in a Circular Array

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 2515](https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description/)

# 🧠 Problem Description
# [Github LeetCode 2515. Shortest Distance to Target String in a Circular Array](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2515.%20Shortest%20Distance%20to%20Target%20String%20in%20a%20Circular%20Array) 

class Solution:
    def closestTarget(
        self, words: List[str], target: str, startIndex: int
    ) -> int:
        ans = n = len(words)
        for i, word in enumerate(words):
            if word == target:
                ans = min(ans, abs(i - startIndex), n - abs(i - startIndex))
        return ans if ans < n else -1