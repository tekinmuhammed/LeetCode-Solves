# 874. Walking Robot Simulation

**Difficulty:** Medium 
**Problem Link:** [LeetCode 874](https://leetcode.com/problems/walking-robot-simulation/description/)

---

## Problem Description

A robot on an infinite XY-plane starts at point `(0, 0)` facing north. The robot can receive three types of commands:
- `-2`: Turn left $90^\circ$.
- `-1`: Turn right $90^\circ$.
- `1 <= k <= 9`: Move forward $k$ units, one unit at a time.

Some grid squares are obstacles. If the robot runs into an obstacle, it stays in its current location and moves on to the next command.

Return the **maximum squared Euclidean distance** that the robot ever gets from the origin (i.e., $x^2 + y^2$).

---

## Approach: Simulation with Coordinate Hashing

To efficiently simulate the robot's movement and handle obstacle detection, we use a direction vector array and a hash set for obstacles.

### Key Ideas:
1.  **Direction Vectors:** We represent directions as a circular array: `[(0, 1), (1, 0), (0, -1), (-1, 0)]` (North, East, South, West).
    - Turning **Right** is `(current_direction + 1) % 4`.
    - Turning **Left** is `(current_direction + 3) % 4`.
2.  **Obstacle Lookup:** Checking for an obstacle in a list is $O(m)$. By converting `(x, y)` coordinates into a unique hash value and storing them in a `set`, we achieve $O(1)$ lookup time.
3.  **Step-by-Step Movement:** For a move command of $k$ units, the robot moves one unit at a time. Before each step, it checks the hash set to see if the next coordinate is blocked.
4.  **Global Maximum:** We track the squared distance ($x^2 + y^2$) at the end of each move command to ensure we capture the furthest point reached during the entire simulation.

---

## Code

```python
class Solution:
    def __init__(self):
        # A multiplier larger than the coordinate range to ensure unique hashes
        self.HASH_MULTIPLIER = 60013 

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        # Store obstacles in a set for efficient O(1) lookup
        obstacle_set = {self._hash_coordinates(x, y) for x, y in obstacles}

        # Direction vectors: 0:North, 1:East, 2:South, 3:West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x, y = 0, 0
        max_distance_squared = 0
        current_direction = 0  # Starts facing North

        for command in commands:
            if command == -1:  # Turn right
                current_direction = (current_direction + 1) % 4
            elif command == -2:  # Turn left
                current_direction = (current_direction + 3) % 4
            else:
                # Move forward 'command' steps
                dx, dy = directions[current_direction]
                for _ in range(command):
                    next_x, next_y = x + dx, y + dy
                    # Check for obstacle
                    if self._hash_coordinates(next_x, next_y) in obstacle_set:
                        break
                    x, y = next_x, next_y
                
                # Update the maximum squared distance reached so far
                max_distance_squared = max(max_distance_squared, x * x + y * y)

        return max_distance_squared

    def _hash_coordinates(self, x: int, y: int) -> int:
        # Simple linear hashing to map (x, y) to a unique integer
        return x + self.HASH_MULTIPLIER * y
```

---

## Example Walkthrough

**Input:** `commands = [4, -1, 3], obstacles = []`

1.  **Initial:** Pos $(0,0)$, Facing North $(0,1)$.
2.  **Move 4:** Move 4 steps North $\rightarrow$ $(0,4)$. $dist^2 = 16$.
3.  **Turn -1:** Turn Right $\rightarrow$ Facing East $(1,0)$.
4.  **Move 3:** Move 3 steps East $\rightarrow$ $(3,4)$. $dist^2 = 3^2 + 4^2 = 25$.
5.  **Result:** `25`.

---

## Complexity Analysis

* **Time Complexity:** $O(n + m + \sum k)$
    - $O(m)$ to process and hash obstacles.
    - $O(n)$ to iterate through commands.
    - $O(\sum k)$ for the total number of steps taken across all move commands.
* **Space Complexity:** $O(m)$
    - To store the hash values of $m$ obstacles in the `obstacle_set`.

---

## Tags
`Simulation`, `Hash-Set`, `Array`, `Math`, `Coordinate-System`