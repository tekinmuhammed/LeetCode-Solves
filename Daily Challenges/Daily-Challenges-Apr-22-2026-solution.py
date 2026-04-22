# 2452. Words Within Two Edits of Dictionary

**Difficulty:** Medium
**Problem Link:** [LeetCode 2452](https://leetcode.com/problems/words-within-two-edits-of-dictionary/description/)

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