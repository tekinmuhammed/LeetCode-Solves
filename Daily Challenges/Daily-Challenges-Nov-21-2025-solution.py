# 3304. Find the K-th Character in String Game I

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 3304](https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description/)

# 🧠 Problem Description 
# [Github LeetCode 3304. Find the K-th Character in String Game I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3304.%20Find%20the%20K-th%20Character%20in%20String%20Game%20I)

class Solution(object):
    def kthCharacter(self, k):
        word = "a"
        
        while len(word) < k:
            # Her karakteri bir sonraki harfe çevir
            new_part = ''.join(chr(ord(c) + 1) for c in word)
            # Yeni stringi ekle
            word += new_part
        
        return word[k - 1]