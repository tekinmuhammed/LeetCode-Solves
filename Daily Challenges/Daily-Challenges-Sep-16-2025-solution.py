# 📘 LeetCode 1671 - Minimum Number of Removals to Make Mountain Array

# **Difficulty:** Hard  
# **Problem Link:** [LeetCode 1671](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array)

# 🧠 Problem Description 
# [Github LeetCode 1671 - Minimum Number of Removals to Make Mountain Array](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/2197.%20Replace%20Non-Coprime%20Numbers%20in%20Array)

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        N = len(nums)
        stack = []

        for i in nums:
            stack.append(i)

            while len(stack) >=  2 and gcd(stack[-1], stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()
                
                l = lcm(a, b)
                stack.append(l)
            
        return stack