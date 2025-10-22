# 🧩 2273. Find Resultant Array After Removing Anagrams

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 2273](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/)

# 🧠 Problem Description
# [Github LeetCode 2273. Find Resultant Array After Removing Anagrams](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2273.%20Find%20Resultant%20Array%20After%20Removing%20Anagrams)

class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = [words[0]]
        
        for i in range(1, len(words)):
            # Eğer mevcut kelime öncekiyle anagram değilse ekle
            if sorted(words[i]) != sorted(result[-1]):
                result.append(words[i])
        
        return result