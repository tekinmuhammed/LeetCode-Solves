# 2410. Maximum Matching of Players With Trainers

# **Difficulty:** Medium  
# **Link:** [LeetCode 2410](https://leetcode.com/problems/maximum-matching-of-players-with-trainers)

# 🧠 Problem Description 
# [Github LeetCode 2410. Maximum Matching of Players With Trainers](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2410.%20Maximum%20Matching%20of%20Players%20With%20Trainers)

class Solution:
    def matchPlayersAndTrainers(
        self, players: List[int], trainers: List[int]
    ) -> int:
        players.sort()
        trainers.sort()
        m, n = len(players), len(trainers)
        i = j = count = 0

        while i < m and j < n:
            while j < n and players[i] > trainers[j]:
                j += 1
            if j < n:
                count += 1
            i += 1
            j += 1

        return count