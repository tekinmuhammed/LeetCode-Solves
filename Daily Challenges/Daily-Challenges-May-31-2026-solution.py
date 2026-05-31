# 2126. Destroying Asteroids

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 2126](https://leetcode.com/problems/destroying-asteroids/description/)

# 🧠 Problem Description 
# [Github LeetCode 2126. Destroying Asteroids](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2126.%20Destroying%20Asteroids) 

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()  # Sort by mass in ascending order
        for asteroid in asteroids:
            # Traverse the asteroids in order, attempt to destroy and update mass or return the result
            if mass < asteroid:
                return False
            mass += asteroid
        return True  # Successfully destroy all asteroids