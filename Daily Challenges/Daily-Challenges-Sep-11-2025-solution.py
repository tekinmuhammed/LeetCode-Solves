# 2785. Sort Vowels in a String

# **Difficulty:** Medium  
# **Link:** [LeetCode 2785](https://leetcode.com/problems/sort-vowels-in-a-string/)

# 🧠 Problem Description 
# [Github LeetCode 2785. Sort Vowels in a String](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2785.%20Sort%20Vowels%20in%20a%20String)

class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")

        # 1. Seslileri topla
        vowel_list = [ch for ch in s if ch in vowels]

        # 2. ASCII değerlerine göre sırala
        vowel_list.sort()

        # 3. Yeni stringi oluştur
        result = []
        idx = 0
        for ch in s:
            if ch in vowels:
                result.append(vowel_list[idx])
                idx += 1
            else:
                result.append(ch)

        return "".join(result)