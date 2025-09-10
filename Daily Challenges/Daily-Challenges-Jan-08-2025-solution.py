# 🔠 LeetCode 3042 - Count Prefix and Suffix Pairs I

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 3042](https://leetcode.com/problems/count-prefix-and-suffix-pairs-i)

# 🧠 Problem Description 
# [Github LeetCode 3042 - Count Prefix and Suffix Pairs I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3042.%20Count%20Prefix%20and%20Suffix%20Pairs%20I)

class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                        count += 1
        return count