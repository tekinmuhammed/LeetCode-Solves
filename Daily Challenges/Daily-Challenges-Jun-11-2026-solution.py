# 2553. Separate the Digits in an Array

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 2553](https://leetcode.com/problems/separate-the-digits-in-an-array/description/)

# 🧠 Problem Description
# [Github LeetCode 2553. Separate the Digits in an Array](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2553.%20Separate%20the%20Digits%20in%20an%20Array) 

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            tmp = []
            while x > 0:
                tmp.append(x % 10)
                x //= 10
            res.extend(tmp[::-1])
        return res