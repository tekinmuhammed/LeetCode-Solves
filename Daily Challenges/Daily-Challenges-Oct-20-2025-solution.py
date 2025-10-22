# ⚙️ 2011. Final Value of Variable After Performing Operations

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 2011](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description)

# 🧠 Problem Description
# [Github LeetCode 2011. Final Value of Variable After Performing Operations](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2011.%20Final%20Value%20of%20Variable%20After%20Performing%20Operations)

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        X = 0
        for op in operations:
            if '+' in op:
                X += 1
            else:
                X -= 1
        return X