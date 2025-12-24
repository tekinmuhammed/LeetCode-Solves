# 3074. Apple Redistribution into Boxes

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 3074](https://leetcode.com/problems/apple-redistribution-into-boxes/description/)

# 🧠 Problem Description
# [Github LeetCode 3074. Apple Redistribution into Boxes](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3074.%20Apple%20Redistribution%20into%20Boxes)

class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total_apples = sum(apple)

        capacity.sort(reverse=True)

        curr = 0
        count = 0

        for cap in capacity:
            curr += cap
            count += 1
            if curr >= total_apples:
                return count