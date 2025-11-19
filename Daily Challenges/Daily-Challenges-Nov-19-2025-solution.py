# 2154. Keep Multiplying Found Values by Two

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 2154](https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/)

# 🧠 Problem Description 
# [Github LeetCode 2154. Keep Multiplying Found Values by Two](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2154.%20Keep%20Multiplying%20Found%20Values%20by%20Two)

class Solution(object):
    def findFinalValue(self, nums, original):
        s = set(nums)   # O(1) arama için
        
        while original in s:
            original *= 2
            
        return original