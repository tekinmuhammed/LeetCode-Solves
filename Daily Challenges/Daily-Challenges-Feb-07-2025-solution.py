# 🧮 LeetCode 1726 - Tuple with Same Product

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1726](https://leetcode.com/problems/tuple-with-same-product/)

# 🧠 Problem Description
# [Github LeetCode 1726 - Tuple with Same Product](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1726.%20Tuple%20with%20Same%20Product)

from collections import defaultdict
class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product_map = defaultdict(int)
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                result += 8 * product_map[product]
                product_map[product] += 1
        return result