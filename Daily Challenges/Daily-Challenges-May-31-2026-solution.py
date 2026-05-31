
# 🧠 Problem Description 
# [Github LeetCode 3161. Block Placement Queries](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/3161.%20Block%20Placement%20Queries) 

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()  # Sort by mass in ascending order
        for asteroid in asteroids:
            # Traverse the asteroids in order, attempt to destroy and update mass or return the result
            if mass < asteroid:
                return False
            mass += asteroid
        return True  # Successfully destroy all asteroids