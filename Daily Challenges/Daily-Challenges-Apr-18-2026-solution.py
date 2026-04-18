
# 🧠 Problem Description
# [Github LeetCode 3761. Minimum Absolute Distance Between Mirror Pairs](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3761.%20Minimum%20Absolute%20Distance%20Between%20Mirror%20Pairs) 

class Solution:
    def reverse(self, n: int) -> int:
        res = 0
        while n > 0:
            res = res * 10 + n % 10
            n //= 10
        return res

    def mirrorDistance(self, n: int) -> int:
        return abs(n - self.reverse(n))