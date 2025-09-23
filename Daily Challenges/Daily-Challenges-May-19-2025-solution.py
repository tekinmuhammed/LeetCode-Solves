# 🔺 LeetCode 3024 - Type of Triangle

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 3024](https://leetcode.com/problems/type-of-triangle)

# 🧠 Problem Description 
# [Github LeetCode 3024 - Type of Triangle](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3024.%20Type%20of%20Triangle)

class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        a, b, c = sorted(nums)

        if a + b <= c:
            return "none"
        
        if a == b == c:
            return "equilateral"

        if a == b or b == c or a == c:
            return "isosceles"
        
        return "scalene"