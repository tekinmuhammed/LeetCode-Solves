class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        ans = 1
        while ans <= n:
            ans <<= 1
        return ans
     
# 🧠 Problem Description 
# [Github LeetCode 3501. Maximize Active Section with Trade II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/3501.%20Maximize%20Active%20Section%20with%20Trade%20II)
