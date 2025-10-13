# 3477. Fruits Into Baskets II

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 3477](https://leetcode.com/problems/fruits-into-baskets-ii) *(contest problem)*

# 🧠 Problem Description 
# [Github LeetCode 3477. Fruits Into Baskets II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3477.%20Fruits%20Into%20Baskets%20II)

class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(fruits)
        used = [False] * n
        unplaced = 0

        for i in range(n):
            placed = False
            for j in range(n):
                if not used[j] and baskets[j] >= fruits[i]:
                    used[j] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1
        return unplaced