# ⚡ LeetCode 1863 - Sum of All Subset XOR Totals

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 1863](https://leetcode.com/problems/sum-of-all-subset-xor-totals)

# 🧠 Problem Description
# [Github LeetCode 1863 - Sum of All Subset XOR Totals](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1863.%20Sum%20of%20All%20Subset%20XOR%20Totals)

class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.total = 0
        def dfs(index, current_xor):
            if index == len(nums):
                self.total += current_xor
                return
            dfs(index + 1, current_xor)
            dfs(index + 1, current_xor ^ nums[index])
        dfs(0, 0)
        return self.total