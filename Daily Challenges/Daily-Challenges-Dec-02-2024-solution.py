# 📝 LeetCode 1455 - Check If a Word Occurs As a Prefix of Any Word in a Sentence

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 1455](https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence)

# 🧠 Problem Description
# [Github LeetCode 1455 - Check If a Word Occurs As a Prefix of Any Word in a Sentence](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1455.%20Check%20If%20a%20Word%20Occurs%20As%20a%20Prefix%20of%20Any%20Word%20in%20a%20Sentence)

class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split()
        for index, word in enumerate(words):
            if word.startswith(searchWord):
                return index + 1
        return -1