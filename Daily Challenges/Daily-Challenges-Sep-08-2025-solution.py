# 1317. Convert Integer to the Sum of Two No-Zero Integers

# **Difficulty:** Easy  
# **Link:** [LeetCode 1317](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/)

# 🧠 Problem Description 
# [Github LeetCode 1317. Convert Integer to the Sum of Two No-Zero Integers](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1317.%20Convert%20Integer%20to%20the%20Sum%20of%20Two%20No-Zero%20Integers)

class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def has_zero(x):
            return '0' in str(x)
        
        for a in range(1, n):
            b = n - a
            if not has_zero(a) and not has_zero(b):
                return [a, b]