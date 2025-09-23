# 🔤 LeetCode 1408 - String Matching in an Array

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 1408](https://leetcode.com/problems/string-matching-in-an-array/)

# 🧠 Problem Description 
# [Github LeetCode 1408 - String Matching in an Array](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1408.%20String%20Matching%20in%20an%20Array)

class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break
        return result