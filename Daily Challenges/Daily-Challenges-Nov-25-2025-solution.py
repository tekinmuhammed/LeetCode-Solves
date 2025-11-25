# 1015. Smallest Integer Divisible by K

# **Difficulty:** Medium
# **Link:** [LeetCode 1015](https://leetcode.com/problems/smallest-integer-divisible-by-k/description/)

# 🧠 Problem Description 
# [Github LeetCode 1015. Smallest Integer Divisible by K](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1015.%20Smallest%20Integer%20Divisible%20by%20K)

class Solution(object):
    def smallestRepunitDivByK(self, k):
        # If k is divisible by 2 or 5, no repunit will ever be divisible by it.
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length
        
        return -1