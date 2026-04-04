 # 2075. Decode the Slanted Ciphertext 

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2075](https://leetcode.com/problems/decode-the-slanted-ciphertext/)

# 🧠 Problem Description 
# [Github LeetCode 3661. Maximum Walls Destroyed by Robots](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/3661.%20Maximum%20Walls%20Destroyed%20by%20Robots) 

class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        
        res = []
        
        for start_col in range(cols):
            i, j = 0, start_col
            
            while i < rows and j < cols:
                res.append(encodedText[i * cols + j])
                i += 1
                j += 1
        
        return "".join(res).rstrip()