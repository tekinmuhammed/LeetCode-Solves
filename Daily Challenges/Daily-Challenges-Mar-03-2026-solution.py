# 1545. Find Kth Bit in Nth Binary String 

# **Difficulty:** Medium 
# **Problem Link:** [LeetCode 1545](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/)

# 🧠 Problem Description
# [Github LeetCode 1545. Find Kth Bit in Nth Binary String](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1545.%20Find%20Kth%20Bit%20in%20Nth%20Binary%20String-2)

class Solution(object):
    def findKthBit(self, n, k):
        def helper(n, k):
            if n == 1:
                return '0'
            
            mid = 1 << (n - 1)   # 2^(n-1)
            
            if k == mid:
                return '1'
            elif k < mid:
                return helper(n - 1, k)
            else:
                # symmetric position
                mirrored = mid - (k - mid)
                bit = helper(n - 1, mirrored)
                # invert
                return '1' if bit == '0' else '0'
        
        return helper(n, k)