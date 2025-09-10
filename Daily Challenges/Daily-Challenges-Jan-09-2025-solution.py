# 🔤 LeetCode 2185 - Counting Words With a Given Prefix

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 2185](https://leetcode.com/problems/counting-words-with-a-given-prefix)

# 🧠 Problem Description 
# [Github LeetCode 2185 - Counting Words With a Given Prefix](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2185.%20Counting%20Words%20With%20a%20Given%20Prefix)

class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count