# 🔀 LeetCode 2425 - Bitwise XOR of All Pairings

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2425](https://leetcode.com/problems/bitwise-xor-of-all-pairings)

# 🧠 Problem Description 
# [Github LeetCode 2425 - Bitwise XOR of All Pairings](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2425.%20Bitwise%20XOR%20of%20All%20Pairings)

class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        xor1, xor2 = 0, 0
        for num in nums1:
            xor1 ^= num
        for num in nums2:
            xor2 ^= num
        len1, len2 = len(nums1), len (nums2)

        result = 0
        if len2 % 2 == 1:
            result ^= xor1
        if len1 % 2 == 1:
            result ^= xor2
        return result