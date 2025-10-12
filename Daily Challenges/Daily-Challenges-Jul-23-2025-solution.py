# 1717. Maximum Score From Removing Substrings

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 1717](https://leetcode.com/problems/maximum-score-from-removing-substrings/)

# 🧠 Problem Description
# [Github LeetCode 1717. Maximum Score From Removing Substrings](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1717.%20Maximum%20Score%20From%20Removing%20Substrings)

class Solution(object):
    def maximumGain(self, s, x, y):
        def remove_pattern(s, a, b, point):
            stack = []
            score = 0
            for ch in s:
                if stack and stack[-1] == a and ch == b:
                    stack.pop()
                    score += point
                else:
                    stack.append(ch)
            return "".join(stack), score

        total_score = 0

        # Önce en yüksek puanlı işlemi yap
        if x > y:
            s, score1 = remove_pattern(s, 'a', 'b', x)
            s, score2 = remove_pattern(s, 'b', 'a', y)
        else:
            s, score1 = remove_pattern(s, 'b', 'a', y)
            s, score2 = remove_pattern(s, 'a', 'b', x)

        return score1 + score2