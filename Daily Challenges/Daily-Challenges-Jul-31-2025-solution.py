# 898. Bitwise ORs of Subarrays

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 898](https://leetcode.com/problems/bitwise-ors-of-subarrays/)

# 🧠 Problem Description 
# [Github LeetCode 898. Bitwise ORs of Subarrays](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/898.%20Bitwise%20ORs%20of%20Subarrays)

class Solution(object):
    def subarrayBitwiseORs(self, arr):
        result = set()
        prev = set()

        for num in arr:
            curr = {num}
            for val in prev:
                curr.add(num | val)
            prev = curr
            result.update(curr)

        return len(result)