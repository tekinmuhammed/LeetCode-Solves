# 2126. Destroying Asteroids

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2126](https://leetcode.com/problems/destroying-asteroids/description/)

---

## Problem
You are given an integer `mass`, which represents the original mass of a planet. You are further given an integer array `asteroids`, where `asteroids[i]` is the mass of the $i^{th}$ asteroid.

You can arrange for the planet to collide with the asteroids in **any arbitrary order**. If the mass of the planet is **greater than or equal to** the mass of the asteroid, the asteroid is destroyed and the planet **gains** the mass of the asteroid. Otherwise, the planet is destroyed.

Return `true` if all asteroids can be destroyed. Otherwise, return `false`.

---

# Approach

This problem can be perfectly solved using a **Greedy Algorithm**. 

To maximize our chances of destroying every asteroid, our planet should always engage the smallest available asteroid first. By consuming the smallest asteroids, the planet continuously builds up its mass, making it large enough to eventually tackle the massive asteroids that it couldn't have destroyed initially.

Steps:

1. **Sort the Asteroids:** We sort the `asteroids` array in ascending order. This guarantees that we are always dealing with the smallest possible asteroid at any given step.
2. **Simulate Collisions:** We iterate through the sorted array.
   * If our current `mass` is less than the current `asteroid`'s mass, we cannot destroy it. Since the array is sorted, we also won't be able to destroy any of the subsequent asteroids. We return `False`.
   * If our `mass` is greater than or equal to the `asteroid`, we destroy it and absorb its mass (`mass += asteroid`).
3. **Completion:** If the loop successfully finishes without returning `False`, it means our planet grew large enough to destroy every single asteroid in the system. We return `True`.

---

# Example Walkthrough

Consider `mass = 10` and `asteroids = [3, 9, 19, 5, 21]`

1. **Sort the array:**
   `asteroids = [3, 5, 9, 19, 21]`
2. **Iterate and absorb:**
   * **Target 3:** `10 >= 3` (Destroyed!). New mass = `10 + 3 = 13`
   * **Target 5:** `13 >= 5` (Destroyed!). New mass = `13 + 5 = 18`
   * **Target 9:** `18 >= 9` (Destroyed!). New mass = `18 + 9 = 27`
   * **Target 19:** `27 >= 19` (Destroyed!). New mass = `27 + 19 = 46`
   * **Target 21:** `46 >= 21` (Destroyed!). New mass = `46 + 21 = 67`
3. **Result:** Loop finishes. All asteroids destroyed. Return `True`.

---

# Complexity Analysis

Time Complexity

O(N \log N)

Where `N` is the number of asteroids. The dominant operation in this algorithm is the sorting step, which takes $O(N \log N)$ time. The subsequent linear scan through the array takes $O(N)$ time.

Space Complexity

O(1) or O(N)

The space complexity depends on the sorting algorithm used by the language under the hood (e.g., Python's Timsort uses $O(N)$ auxiliary space in the worst case). However, the logic we wrote only requires $O(1)$ extra space beyond the input array.

---

# Code

```python
from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()  # Sort by mass in ascending order
        for asteroid in asteroids:
            # Traverse the asteroids in order, attempt to destroy and update mass or return the result
            if mass < asteroid:
                return False
            mass += asteroid
        return True  # Successfully destroy all asteroids
```