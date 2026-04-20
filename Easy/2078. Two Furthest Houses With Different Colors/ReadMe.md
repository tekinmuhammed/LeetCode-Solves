# 2078. Two Furthest Houses With Different Colors

**Difficulty:** Easy
**Problem Link:** [LeetCode 2078](https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/)

---

## Problem Description

There are `n` houses evenly lined up on a street, and each house is painted with a specific color. You are given a 0-indexed integer array `colors` of length `n`, where `colors[i]` represents the color of the $i^{th}$ house.

Return the **maximum distance** between two houses with **different colors**.

The distance between the $i^{th}$ and $j^{th}$ houses is $|i - j|$.

---

## Approach: Brute Force Pairwise Comparison

The goal is to find two indices $i$ and $j$ such that $colors[i] \neq colors[j]$ and the value $j - i$ is maximized. 

### Key Ideas:
1.  **Nested Iteration:** We iterate through every possible pair of houses using two loops.
2.  **Color Check:** For each pair $(i, j)$, we check if the colors are different.
3.  **Maximum Tracking:** If the colors are different, we calculate the distance $j - i$ and update our result if this distance is larger than any we have seen so far.
4.  **Simplicity:** While there are more optimal $O(n)$ greedy solutions, this brute force approach is very straightforward and passes easily within the given constraints ($n \le 100$).

---

## Code

```python
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        res = 0  # Initialize the maximum distance
        
        # Traverse every pair (i, j) to find different colors
        for i in range(n):
            for j in range(i + 1, n):
                # If colors are different, calculate distance and update res
                if colors[i] != colors[j]:
                    res = max(res, j - i)
                    
        return res
```

---

## Example Walkthrough

**Input:** `colors = [1, 1, 1, 6, 1, 1, 1]`

1.  **i = 0, j = 3:** `colors[0] = 1`, `colors[3] = 6`. 
    - Colors are different. Distance: $3 - 0 = 3$. `res = 3`.
2.  **i = 3, j = 4:** `colors[3] = 6`, `colors[4] = 1`. 
    - Colors are different. Distance: $4 - 3 = 1$. `res` stays `3`.
3.  **i = 3, j = 6:** `colors[3] = 6`, `colors[6] = 1`. 
    - Colors are different. Distance: $6 - 3 = 3$. `res` stays `3`.

**Output:** `3`

---

## Complexity Analysis

* **Time Complexity:** $O(n^2)$
    - We use two nested loops, where $n$ is the number of houses. In the worst case, we check all $\frac{n(n-1)}{2}$ pairs.
* **Space Complexity:** $O(1)$
    - We only use a few constant-sized integer variables (`res`, `i`, `j`).

---

## Tags
`Array`, `Greedy`, `Brute-Force`, `Enumeration`