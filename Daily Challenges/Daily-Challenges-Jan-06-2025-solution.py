# 📦 LeetCode 1769 - Minimum Number of Operations to Move All Balls to Each Box

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1769](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box)

# 🧠 Problem Description 
# [Github LeetCode 1769 - Minimum Number of Operations to Move All Balls to Each Box](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1769.%20Minimum%20Number%20of%20Operations%20to%20Move%20All%20Balls%20to%20Each%20Box)

class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        a = len(boxes)
        answer = [0] * a

        moves = 0
        count = 0
        for i in range(a):
            answer[i] += moves
            if boxes[i] == '1':
                count += 1
            moves += count
        moves = 0
        count = 0
        for i in range(a - 1, -1, -1):
            answer[i] += moves
            if boxes[i] == '1':
                count += 1
            moves += count
        return answer