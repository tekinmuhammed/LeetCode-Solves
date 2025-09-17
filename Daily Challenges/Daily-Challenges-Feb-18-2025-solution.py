# 🔢 LeetCode 2375 - Construct Smallest Number From DI String

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2375](https://leetcode.com/problems/construct-smallest-number-from-di-string)

# 🧠 Problem Description
# [Github LeetCode 2375 - Construct Smallest Number From DI String](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2375.%20Construct%20Smallest%20Number%20From%20DI%20String)

class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        stack = []
        result = []
        num = 1
        for char in pattern + "I":
            stack.append(str(num))
            num += 1
            if char == "I":
                while stack:
                    result.append(stack.pop())
        return "".join(result)