# 📊 LeetCode 2554 - Maximum Number of Integers to Choose From a Range I

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 2554](https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i)

# 🧠 Problem Description
# [Github LeetCode 2554 - Maximum Number of Integers to Choose From a Range I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2554.%20Maximum%20Number%20of%20Integers%20to%20Choose%20From%20a%20Range%20I)

class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        banned_set = set(banned)
        current_sum = 0
        count = 0
        for num in range(1, n + 1):
            if num not in banned_set and current_sum + num <= maxSum:
                current_sum += num
                count += 1
        return count