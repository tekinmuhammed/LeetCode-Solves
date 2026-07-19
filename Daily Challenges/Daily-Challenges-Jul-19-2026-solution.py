# 1081. Smallest Subsequence of Distinct Characters

# **Difficulty:** Medium 
# **Problem Link:** [LeetCode 1081](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/)
 
# 🧠 Problem Description 
# [Github LeetCode 1081. Smallest Subsequence of Distinct Characters](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1081.%20Smallest%20Subsequence%20of%20Distinct%20Characters)
 
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        vis = [0] * 26
        num = [0] * 26

        for ch in s:
            num[ord(ch) - ord("a")] += 1
        stk = []

        for ch in s:
            idx = ord(ch) - ord("a")
            if not vis[idx]:
                while stk and stk[-1] > ch:
                    top_idx = ord(stk[-1]) - ord("a")
                    if num[top_idx] > 0:
                        vis[top_idx] = 0
                        stk.pop()
                    else:
                        break
                vis[idx] = 1
                stk.append(ch)
            num[idx] -= 1

        return "".join(stk)