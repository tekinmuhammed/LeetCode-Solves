# 1935. Maximum Number of Words You Can Type

# **Difficulty:** Easy  
# **Link:** [LeetCode 1935](https://leetcode.com/problems/maximum-number-of-words-you-can-type/)

# 🧠 Problem Description 
# [Github LeetCode 1935. Maximum Number of Words You Can Type](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1935.%20Maximum%20Number%20of%20Words%20You%20Can%20Type)

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        broken = set(brokenLetters)   # Bozuk tuşları kümeye alıyoruz
        words = text.split()          # Metni kelimelere ayırıyoruz
        
        count = 0
        for word in words:
            if not any(ch in broken for ch in word):  # Eğer kelimede bozuk harf yoksa
                count += 1
        return count