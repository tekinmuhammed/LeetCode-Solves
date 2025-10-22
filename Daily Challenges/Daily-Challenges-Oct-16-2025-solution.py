# 🧩 2598. Smallest Missing Non-negative Integer After Operations

# **Difficulty:** Medium
# Problem Link  [LeetCode 2598. Smallest Missing Non-negative Integer After Operations](https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/description/)  

# 🧠 Problem Description
# [Github LeetCode 2598. Smallest Missing Non-negative Integer After Operations](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2598.%20Smallest%20Missing%20Non-negative%20Integer%20After%20Operations)

class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        from collections import Counter
        
        # Her sayıyı 'value' ile mod al (negatifler için normalize et)
        count = Counter(x % value for x in nums)
        
        # MEX hesapla
        mex = 0
        while True:
            remainder = mex % value
            if count[remainder] > 0:
                count[remainder] -= 1
                mex += 1
            else:
                return mex