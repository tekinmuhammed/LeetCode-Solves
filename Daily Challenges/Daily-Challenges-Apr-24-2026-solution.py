# 2833. Furthest Point From Origin 

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 2833](https://leetcode.com/problems/furthest-point-from-origin/description/)

# 🧠 Problem Description
# [Github LeetCode 2833. Furthest Point From Origin ](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2833.%20Furthest%20Point%20From%20Origin) 

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count("R") - moves.count("L")) + moves.count("_")