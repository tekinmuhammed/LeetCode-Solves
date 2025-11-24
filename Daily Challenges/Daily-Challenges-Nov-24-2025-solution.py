# 1018. Binary Prefix Divisible By 5

# **Difficulty:** Easy
# **Link:** [LeetCode 1018](https://leetcode.com/problems/binary-prefix-divisible-by-5/description/)

# 🧠 Problem Description 
# [Github LeetCode 1018. Binary Prefix Divisible By 5](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1018.%20Binary%20Prefix%20Divisible%20By%205)

class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        result = []
        current = 0
        
        for bit in nums:
            # keep prefix mod 5 only
            current = (current * 2 + bit) % 5
            result.append(current == 0)
        
        return result