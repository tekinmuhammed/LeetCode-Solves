# 2566. Maximum Difference by Remapping a Digit

# **Problem Link:** [LeetCode 2566](https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/)  
# **Difficulty:** Easy

# 🧠 Problem Description 
# [Github  Maximum Difference by Remapping a Digit](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2566.%20Maximum%20Difference%20by%20Remapping%20a%20Digit)

class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)

        for d in s:
            if d != '9':
                max_val = int(s.replace(d, '9'))
                break
        else:
            max_val = num
        
        for d in s:
            if d != '0':
                min_val = int(s.replace(d, '0'))
                break
        else:
            min_val = num
        return max_val - min_val