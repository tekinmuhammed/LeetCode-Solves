# 2839. Check if Strings Can be Made Equal With Operations I

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 2839](https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/description/)

# 🧠 Problem Description
# [Github LeetCode 2839. Check if Strings Can be Made Equal With Operations I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2839.%20Check%20if%20Strings%20Can%20be%20Made%20Equal%20With%20Operations%20I) 

class Solution(object):
    def canBeEqual(self, s1, s2):
        # even indices
        s1_even = sorted([s1[0], s1[2]])
        s2_even = sorted([s2[0], s2[2]])
        
        # odd indices
        s1_odd = sorted([s1[1], s1[3]])
        s2_odd = sorted([s2[1], s2[3]])
        
        return s1_even == s2_even and s1_odd == s2_odd