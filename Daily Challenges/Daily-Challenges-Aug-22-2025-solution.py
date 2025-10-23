# 3195. Find the Minimum Area to Cover All Ones I

# **Difficulty:** Medium  
# **Link:** [LeetCode 3195](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/)  

# 🧠 Problem Description 
# [Github LeetCode 3195. Find the Minimum Area to Cover All Ones I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3195.%20Find%20the%20Minimum%20Area%20to%20Cover%20All%20Ones%20I)

class Solution:
    def minimumArea(self, g: List[List[int]]) -> int:
        f = lambda g,q:next(k for k in range(len(g))[::q] if any(g[k]))
        return (f(g,-1)-f(g,1)+1)*(f(g:=[*zip(*g)],-1)-f(g,1)+1)