# 1925. Count Square Sum Triples 

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 1863](https://leetcode.com/problems/count-square-sum-triples/description/)

# 🧠 Problem Description
# [Github LeetCode 1925. Count Square Sum Triples](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1925.%20Count%20Square%20Sum%20Triples)

class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c2 = a*a + b*b
                c = int(c2**0.5)
                
                if c <= n and c*c == c2:
                    count += 1
                    
        return count