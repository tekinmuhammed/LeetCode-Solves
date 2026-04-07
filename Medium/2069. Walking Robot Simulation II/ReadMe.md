# 2069. Walking Robot Simulation II

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2069](https://leetcode.com/problems/walking-robot-simulation-ii/)

---

## Problem Description

A robot is located on a grid of `width x height`. The robot starts at `(0, 0)` facing **"East"**. It moves in a counter-clockwise direction along the **outer boundary** of the grid. If the robot attempts to move beyond the boundary, it turns $90^\circ$ counter-clockwise and continues moving.

Implement the `Robot` class:
- `Robot(int width, int height)`: Initializes the grid and the robot's starting position.
- `step(int num)`: Moves the robot `num` steps forward.
- `getPos()`: Returns the current $(x, y)$ coordinates.
- `getDir()`: Returns the current direction ("East", "North", "West", or "South").

---

## Approach: Circular Path Pre-computation

Since the robot only moves along the perimeter of the grid, we can treat the entire boundary as a single **linear path mapped to a circle**.

### Key Ideas:
1.  **Perimeter Mapping:** The total number of unique cells on the boundary is $2 \times (width + height) - 4$. We pre-calculate every coordinate and the direction the robot *would* be facing at that coordinate.
2.  **Order of Traversal:** We follow the counter-clockwise path:
    - **Bottom Edge:** $(0,0)$ to $(W-1, 0)$ (Facing East)
    - **Right Edge:** $(W-1, 1)$ to $(W-1, H-1)$ (Facing North)
    - **Top Edge:** $(W-2, H-1)$ to $(0, H-1)$ (Facing West)
    - **Left Edge:** $(0, H-2)$ to $(0, 1)$ (Facing South)
3.  **Modular Arithmetic:** Moving `num` steps is equivalent to `(current_index + num) % path_length`. This makes the `step` operation extremely fast ($O(1)$).
4.  **The (0,0) Edge Case:** - Initially, the robot is at `(0,0)` facing **"East"**.
    - After any number of steps that return the robot to `(0,0)`, it will be facing **"South"** (because it arrived from the top at $(0,1)$ and turned). 
    - We use a `moved` flag to distinguish between the initial state and any state after movement.

---

## Code

```python
class Robot:
    TO_DIR = {
        0: "East",
        1: "North",
        2: "West",
        3: "South",
    }

    def __init__(self, width: int, height: int):
        self.moved = False
        self.idx = 0
        self.pos = []
        self.dirs = []

        # Pre-compute all positions and directions along the boundary
        # Bottom side: (0, 0) -> (W-1, 0)
        for i in range(width):
            self.pos.append((i, 0))
            self.dirs.append(0) # East
        
        # Right side: (W-1, 1) -> (W-1, H-1)
        for i in range(1, height):
            self.pos.append((width - 1, i))
            self.dirs.append(1) # North
            
        # Top side: (W-2, H-1) -> (0, H-1)
        for i in range(width - 2, -1, -1):
            self.pos.append((i, height - 1))
            self.dirs.append(2) # West
            
        # Left side: (0, H-2) -> (0, 1)
        for i in range(height - 2, 0, -1):
            self.pos.append((0, i))
            self.dirs.append(3) # South

        # Correction for (0,0): After one full lap, the robot faces South at (0,0)
        self.dirs[0] = 3

    def step(self, num: int) -> None:
        self.moved = True
        # Use modulo to handle multiple laps efficiently
        self.idx = (self.idx + num) % len(self.pos)

    def getPos(self) -> List[int]:
        return list(self.pos[self.idx])

    def getDir(self) -> str:
        # Special case for the very first call before any movement
        if not self.moved and self.idx == 0:
            return "East"
        return Robot.TO_DIR[self.dirs[self.idx]]
```

---

## Example Walkthrough

**Input:** `Robot(6, 3)`, `step(2)`, `step(2)`, `step(10)`

1.  **Init:** Perimeter length = $2 \times (6+3) - 4 = 14$. 
2.  **step(2):** `idx` becomes $2$. Pos: $(2,0)$, Dir: "East".
3.  **step(2):** `idx` becomes $4$. Pos: $(4,0)$, Dir: "East".
4.  **step(10):** `idx` becomes $(4+10) \% 14 = 0$. 
    - Pos: `(0,0)`.
    - Dir: Since `moved` is true, returns `dirs[0]` which is "South".

---

## Complexity Analysis

* **Time Complexity:**
    - **Initialization:** $O(W + H)$ to build the perimeter path.
    - **step:** $O(1)$ constant time.
    - **getPos / getDir:** $O(1)$ constant time.
* **Space Complexity:** $O(W + H)$
    - To store the coordinates and directions of the perimeter cells.

---

## Tags
Design, Simulation, Matrix, Math, Modulo-Arithmetic