# 🟦 LeetCode 1861 - Rotating the Box

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1861](https://leetcode.com/problems/rotating-the-box)

# 🧠 Problem Description
# [Github LeetCode 1861 - Rotating the Box](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1861.%20Rotating%20the%20Box)

class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        for row in box:
            empty = len(row) - 1
            for col in range(len(row) -1, -1, -1):
                if row[col] == "*":
                    empty = col - 1
                elif row[col] == "#":
                    row[col], row[empty] = ".", "#"
                    empty -= 1
        rotated = list(zip(*box[::-1]))
        return[list(row) for row in rotated]                