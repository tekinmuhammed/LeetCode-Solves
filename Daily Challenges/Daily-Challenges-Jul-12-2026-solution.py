# 1331. Rank Transform of an Array 
 
# **Difficulty:** Easy 
# **Problem Link:** [LeetCode 1331](https://leetcode.com/problems/rank-transform-of-an-array/description/)
 
# 🧠 Problem Description 
# [Github LeetCode 1331. Rank Transform of an Array ](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1331.%20Rank%20Transform%20of%20an%20Array)

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Store the rank for each number in arr 
        num_to_rank = {}
        sorted_arr = sorted(arr)
        rank = 1
        for i in range(len(sorted_arr)):
            if i > 0 and sorted_arr[i] > sorted_arr[i - 1]:
                rank += 1
            num_to_rank[sorted_arr[i]] = rank
        for i in range(len(arr)):
            arr[i] = num_to_rank[arr[i]]
        return arr