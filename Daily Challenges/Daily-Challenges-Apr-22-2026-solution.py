# 2452. Words Within Two Edits of Dictionary

**Difficulty:** Medium
**Problem Link:** [LeetCode 2452](https://leetcode.com/problems/words-within-two-edits-of-dictionary/description/)

# 🧠 Problem Description
# [Github LeetCode 1722. Minimize Hamming Distance After Swap Operations](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1722.%20Minimize%20Hamming%20Distance%20After%20Swap%20Operations) 

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

https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2452.%20Words%20Within%20Two%20Edits%20of%20Dictionary