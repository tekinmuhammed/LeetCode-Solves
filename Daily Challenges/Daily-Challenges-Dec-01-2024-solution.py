# 🔍 LeetCode 1346 - Check If N and Its Double Exist

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 1346](https://leetcode.com/problems/check-if-n-and-its-double-exist)

# 🧠 Problem Description
# [Github LeetCode 1346 - Check If N and Its Double Exist](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1346.%20Check%20If%20N%20and%20Its%20Double%20Exist)

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()
        for num in arr:
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False