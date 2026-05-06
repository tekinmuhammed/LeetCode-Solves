# 1861. Rotating the Box 

**Difficulty:** Medium=
**Problem Link:** [LeetCode 1861](https://leetcode.com/problems/rotating-the-box/description/)

---

## Problem 
You are given an `m x n` matrix of characters `box` representing a side-view of a box. Each cell of the box is one of the following:
* A stone `'#'`
* A stationary obstacle `'*'`
* An empty space `'.'`

The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions.

Return an `n x m` matrix representing the box after the rotation and after gravity has taken effect.

---

# Approach 

The problem essentially requires two main operations: rotating the matrix and simulating gravity. 

Instead of doing both at the same time, we can break the problem into clear, manageable steps:

1. **Rotate 90 Degrees Clockwise:** 
   * First, we create an empty `n x m` result matrix.
   * We get the transpose of the input `box` (rows become columns).
   * Then, we reverse each row of the transposed matrix. This standard mathematical trick perfectly achieves a 90-degree clockwise rotation.
2. **Apply Gravity:**
   * Gravity pulls items downwards. In our new matrix, "down" means moving towards the highest row index for each column.
   * We iterate through each column. Inside each column, we scan from the bottom to the top.
   * Whenever we find an empty space (`"."`), we look directly above it to find a stone (`"#"`).
   * If we hit an obstacle (`"*"`), we stop looking further up for that specific empty space, because stones cannot fall through obstacles.
   * If we find a stone before an obstacle, we "drop" the stone into the empty space by swapping their positions.

---

# Example Walkthrough 

Consider a 1x3 box:
`box = [["#", ".", "*"]]`

**Step 1: Rotate 90° Clockwise**   
The 1x3 box becomes a 3x1 box.
Transposed and reversed:
```
[
  ["#"],
  ["."],
  ["*"]
]
```

**Step 2: Apply Gravity**   
We check the only column (j = 0) from bottom (i = 2) to top (i = 0).
* `i = 2`: Found `*`. It's an obstacle, ignore.
* `i = 1`: Found `.`. Look up.
* Upwards search (`k = 0`): Found `#`. 
* Swap them! The stone falls into the empty space.

Final Result:
```
[
  ["."],
  ["#"],
  ["*"]
]
```

---

# Complexity Analysis 

Time Complexity

O(m * n^2)

Creating the rotated matrix takes O(m * n) time. During the gravity phase, we iterate through `m` columns. For each column, we scan `n` rows, and for each empty cell, we might scan up to `n` elements upwards in the worst case (e.g., all empty cells and stones at the very top). This results in an O(n^2) operation per column, leading to a total time complexity of O(m * n^2).

Space Complexity

O(m * n)

We allocate a new `n x m` grid (`result`) to store the rotated box and perform the gravity operations.

---

# Code 
```python
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        result = [["" for _ in range(m)] for _ in range(n)]

        # Create the transpose of the input grid in `result`
        for i in range(n):
            for j in range(m):
                result[i][j] = box[j][i]

        # Reverse each row in the transpose grid to complete the 90° rotation
        for i in range(n):
            result[i].reverse()

        # Apply gravity to let stones fall to the lowest possible empty cell in each column
        for j in range(m):
            # Process each cell in column `j` from bottom to top
            for i in range(n - 1, -1, -1):
                if (
                    result[i][j] == "."
                ):  # Found an empty cell; check if a stone can fall into it
                    next_row_with_stone = -1

                    # Look for a stone directly above the empty cell `result[i][j]`
                    for k in range(i - 1, -1, -1):
                        if result[k][j] == "*":
                            break  # Obstacle blocks any stones above
                        if (
                            result[k][j] == "#"
                        ):  # Stone found with no obstacles in between
                            next_row_with_stone = k
                            break

                    # If a stone was found above, let it fall into the empty cell `result[i][j]`
                    if next_row_with_stone != -1:
                        result[next_row_with_stone][j] = "."
                        result[i][j] = "#"

        return result
```
