# 3459. Length of Longest V-Shaped Diagonal Segment  

**Difficulty:** Hard  
**Link:** [LeetCode 3459](https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/)  

---

## Problem Description  

You are given a 2D grid consisting of values `1` and `2`.  
We want to find the **longest "V-shaped" diagonal segment** in the grid.  

- A "V-shape" starts from a cell with value **1**.  
- From there, we move diagonally (↘, ↙, ↖, ↗) to neighboring cells.  
- Each step must alternate between values `1` and `2`.  
- At most **one 90° turn** is allowed (to create the "V" shape).  
- The length of a segment is the total number of visited cells.  

The task is to return the **maximum length** of such a segment.  

---

## Example  

### Example 1  

**Input:**  
```python
grid = [
  [1, 2, 1],
  [2, 1, 2],
  [1, 2, 1]
]
```

**Output:**
```python
3
```

### Explanation:

- Starting from `(0,0)` = 1 → `(1,1)` = 1 not valid,

- But `(0,0)` = 1 → `(1,1)` = 2 → `(2,2)` = 1 gives a valid segment of length 3.

### Example 2

**Input:**
```python
grid = [
  [1, 2],
  [2, 1]
]
```

**Output:**
```python
2
```

### Explanation:

- Only `(0,0) → (1,1)` works with length 2.

### Constraints

- `2 <= m, n <= 500`

- `grid[i][j] ∈ {1, 2}`

### Approach
**Key Ideas:**

1. Each segment starts from a `1`.

2. We explore diagonally in **four directions**:

- - `(1, 1)` ↘

- - `(1, -1)` ↙

- - `(-1, -1)` ↖

- - `(-1, 1)` ↗

3. While traversing:

- - Values must alternate between `1` and `2`.

- - At most one **90° clockwise turn** is allowed to form the "V".

4. We use **DFS with memoization** (`@cache`) to avoid recomputation.

- - State = `(x, y, direction, turn_available, target_value)`

- - Each call returns the max path length from this state.

5. Keep track of the maximum length found.

### Time and Space Complexity

- **Time Complexity:**

- - Each state `(x, y, direction, turn, target)` is computed once.

- - At most `O(m * n * 4 * 2 * 2)` states.

- - So overall complexity is **O(m * n)**.

- **Space Complexity:**

- - `O(m * n * 4 * 2 * 2)` for memoization.

- - Plus recursion stack up to grid size.

### Tags

`DFS`, `Memoization`, `Dynamic-Programming`, `Grid`, `Geometry`

### Notes

- The `@cache` decorator is critical for efficiency; otherwise, DFS would recompute paths many times.

- The trickiest part is allowing one turn: we model this with a boolean flag `turn`.