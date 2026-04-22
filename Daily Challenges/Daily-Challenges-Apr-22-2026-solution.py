# 2452. Words Within Two Edits of Dictionary

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 2452](https://leetcode.com/problems/words-within-two-edits-of-dictionary/description/)

# 🧠 Problem Description
# [Github LeetCode 2452. Words Within Two Edits of Dictionary](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2452.%20Words%20Within%20Two%20Edits%20of%20Dictionary) 

class Solution:
    def twoEditWords(self, queries, dictionary):
        ans = []
        for query in queries:
            for s in dictionary:
                dis = 0
                for i in range(len(query)):
                    if query[i] != s[i]:
                        dis += 1
                if dis <= 2:
                    ans.append(query)
                    break
        return ans