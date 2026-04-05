# 657. Robot Return to Origin

**Difficulty:** Easy 
**Problem Link:** [LeetCode 657](https://leetcode.com/problems/robot-return-to-origin/description/)

---

## Problem Description

There is a robot starting at the position `(0, 0)`, the origin, on a 2D plane. Given a sequence of its moves, judge if this robot **ends up at (0, 0)** after it completes all of its moves.

The move sequence is represented by a string, and the character `moves[i]` represents its $i^{th}$ move. Valid moves are:
- `'R'` (Right)
- `'L'` (Left)
- `'U'` (Up)
- `'D'` (Down)

Return `true` if the robot returns to the origin after it finishes all of its moves, or `false` otherwise.

**Note:** The way that the robot is "facing" is irrelevant. `'R'` will always make the robot move to the right once, `'L'` will always make it move left, etc.

---

## Approach: Coordinate Tracking (Simulation)

We can simulate the robot's movement by tracking its position on a 2D Cartesian coordinate system $(x, y)$.

### Key Ideas:
1.  **Starting Point:** Initialize the robot's coordinates at $x = 0$ and $y = 0$.
2.  **Move Mapping:**
    - `'U'` (Up): Increases the $y$ coordinate by 1.
    - `'D'` (Down): Decreases the $y$ coordinate by 1.
    - `'R'` (Right): Increases the $x$ coordinate by 1.
    - `'L'` (Left): Decreases the $x$ coordinate by 1.
3.  **Final Check:** After processing the entire string of moves, if both $x$ and $y$ are back to $0$, it means the robot has returned to its starting position.



---

## Code

```python
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # Starting coordinates
        x = 0
        y = 0
        
        # Iterate through each move and update coordinates
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
        
        # Return True if the robot is back at the origin (0, 0)
        return x == 0 and y == 0
```

---

## Example Walkthrough

**Example 1:**
- **Input:** `moves = "UD"`
- **Step 1 ('U'):** $y$ becomes $1$. Position: $(0, 1)$
- **Step 2 ('D'):** $y$ becomes $0$. Position: $(0, 0)$
- **Result:** `True` (Back to origin)

**Example 2:**
- **Input:** `moves = "LL"`
- **Step 1 ('L'):** $x$ becomes $-1$. Position: $(-1, 0)$
- **Step 2 ('L'):** $x$ becomes $-2$. Position: $(-2, 0)$
- **Result:** `False` (Ending at $(-2, 0)$)

---

## Complexity Analysis

* **Time Complexity:** $O(n)$
    - We traverse the string of moves exactly once, where $n$ is the length of the string.
* **Space Complexity:** $O(1)$
    - We only use two integer variables (`x`, `y`) to store the current position, regardless of the number of moves.

---

## Tags
`String`, `Simulation`, `Coordinate-System`