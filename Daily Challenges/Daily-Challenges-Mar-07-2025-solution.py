# 🔢 LeetCode 2965 - Find Missing and Repeated Values

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 2965](https://leetcode.com/problems/find-missing-and-repeated-values)

# 🧠 Problem Description
# [Github LeetCode 2965 - Find Missing and Repeated Values](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2965.%20Find%20Missing%20and%20Repeated%20Values)

class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        num_list = [num for row in grid for num in row]
        num_counts = Counter(num_list)
        repeated = missing = -1
        for num in range(1, n * n + 1):
            if num_counts[num] == 2:
                repeated = num
            elif num_counts[num] == 0:
                missing = num
        return [repeated, missing]