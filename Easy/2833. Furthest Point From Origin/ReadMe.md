# 2833. Furthest Point From Origin

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2833](https://leetcode.com/problems/furthest-point-from-origin/)

---

## Problem Description

You are given a string `moves` of length `n` consisting only of characters `'L'`, `'R'`, and `'_'`. The string represents a series of moves on a number line, where the robot starts at the origin `0`.
- `'L'` means move one unit to the left.
- `'R'` means move one unit to the right.
- `'_'` means you can choose to move either one unit to the left or one unit to the right.

Return the **furthest distance** from the origin the robot can be after making `n` moves.

---

## Approach: Greedy Calculation

To reach the furthest point from the origin, we want to maximize the absolute value of our final position. The fixed moves ('L' and 'R') will dictate our "base" position, and the flexible moves ('_') should all be used in the direction that takes us even further away.

### Key Ideas:
1.  **Fixed Displacement:** First, we calculate the net displacement caused by the mandatory moves: `count('R') - count('L')`.
2.  **Greedy Choice for Underscores:** - If our net displacement is positive (more 'R' than 'L'), we should use all `'_'` moves to go Right.
    - If our net displacement is negative (more 'L' than 'R'), we should use all `'_'` moves to go Left.
    - In both cases, the absolute value of our final position will be the absolute difference of fixed moves plus the total count of flexible moves.
3.  **Simplified Formula:** The maximum distance is simply `abs(count('R') - count('L')) + count('_')`.

---

## Code

```python
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        """
        :type moves: str
        :rtype: int
        """
        # Calculate the base displacement from fixed moves
        fixed_displacement = moves.count("R") - moves.count("L")
        
        # Add the total number of flexible moves to the magnitude of base displacement
        return abs(fixed_displacement) + moves.count("_")
```

---

## Example Walkthrough

**Input:** `moves = "L_RL__R"`

1.  **Counts:**
    - `'L'`: 2
    - `'R'`: 2
    - `'_'`: 3
2.  **Fixed Displacement:** `2 (R) - 2 (L) = 0`.
3.  **Maximum Distance:** `abs(0) + 3 = 3`.
    - *Explanation:* We could treat all `_` as 'L' to reach -3, or all as 'R' to reach 3. Furthest distance is 3.

---

## Complexity Analysis

* **Time Complexity:** $O(n)$
    - We traverse the string `moves` three times (or once if optimized) to count the characters. In Python, `count()` is highly optimized $O(n)$.
* **Space Complexity:** $O(1)$
    - We only use a few integer variables to store counts and the final result.

---

## Tags
String, Greedy, Math, Enumeration