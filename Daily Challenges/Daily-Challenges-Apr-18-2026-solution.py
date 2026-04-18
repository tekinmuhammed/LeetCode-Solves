# 3783. Mirror Distance of an Integer

# **Difficulty:** Easy 
# **Problem Link:** [LeetCode 3783](https://leetcode.com/problems/mirror-distance-of-an-integer/description/)

# 🧠 Problem Description
# [Github LeetCode 3783. Mirror Distance of an Integer](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3783.%20Mirror%20Distance%20of%20an%20Integer) 

class Solution:
    def reverse(self, n: int) -> int:
        res = 0
        while n > 0:
            res = res * 10 + n % 10
            n //= 10
        return res

    def mirrorDistance(self, n: int) -> int:
        return abs(n - self.reverse(n))